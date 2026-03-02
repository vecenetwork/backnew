import logging
import re
import secrets
from typing import TYPE_CHECKING, Optional
from datetime import date, datetime, timedelta

from app.core.permissions import UserPermissions, UserViewLevel
from app.exceptions import WrongPassword, Unauthorized, Missing, ConfigurationError, PermissionDenied, Duplicate, InvalidToken
from app.schema.user import (
    UserResponse,
    UserUpdateInternal,
    UserUpdate,
    UserSettings,
    UserSettingsUpdate,
    SimilaritySortEnum,
    ConnectionFilterEnum,
    TimeRangeEnum,
    GenderEnum,
)
from app.schema import similarity as schema
from app.core.security import get_password_hash, verify_password
from infrastructure.api.auth import jwt_utils
from infrastructure.repository.user_settings import UserSettingsRepository

if TYPE_CHECKING:
    from app.schema.user import UserCreate, User
    from app.services.email.verification import VerificationService
    from infrastructure.repository.user import UserRepository
    from infrastructure.repository.pending_registration import PendingRegistrationRepository
    from infrastructure.repository.similarity.repo import SimilarityRepository
    from infrastructure.repository.subscriptions import SubscriptionRepository

logger = logging.getLogger(__name__)


class UserAlreadyExistsException(Duplicate):
    pass


# Default values for registration (user can update in profile)
DEFAULT_BIRTHDAY = date(2000, 1, 1)
DEFAULT_COUNTRY_ID = 1
DEFAULT_GENDER = GenderEnum.other


class UserService:
    def __init__(
        self,
        repo: "UserRepository",
        settings_repo: "UserSettingsRepository",
        verification: "VerificationService",
        similarity_repo: "SimilarityRepository",
        subscription_repo: "SubscriptionRepository",
        pending_repo: "PendingRegistrationRepository",
    ):
        self.repo = repo
        self.settings_repo = settings_repo
        self.verification = verification
        self.similarity_repo = similarity_repo
        self.subscription_repo = subscription_repo
        self.pending_repo = pending_repo
        self.permissions = UserPermissions()

    async def register_user(self, user_data: "UserCreate") -> "UserResponse":
        if await self.repo.user_exists_by_username_or_email(
            user_data.username, user_data.email
        ):
            msg = f"User with username {user_data.username} or email {user_data.email} already exist"
            logger.error(msg)
            raise UserAlreadyExistsException(msg=msg)

        hashed_password = get_password_hash(user_data.password)
        new_user = await self.repo.create_user(user_data, hashed_password)

        await self.verification.send_verification_email(
            new_user.email, new_user.name or new_user.username
        )

        return UserResponse.from_user(new_user)

    async def verify_user_email(self, verification_token: str) -> str:
        email = await self.verification.verify_token(verification_token)
        await self.repo.verify_user_email(email)
        return email

    async def verify_token_for_redirect(self, token: str) -> str:
        """Validate token and return email. Does not modify DB."""
        return await self.verification.verify_token(token)

    async def email_registered(self, email: str) -> bool:
        """Check if email is already registered."""
        try:
            await self.repo.get_by_email(email)
            return True
        except Missing:
            return False

    async def request_email_activation(self, email: str, username: str, password: str) -> None:
        """Store registration in pending, send activation email. Email and username must be unique."""
        if await self.email_registered(email):
            raise UserAlreadyExistsException(msg=f"Email {email} is already registered")
        if await self.repo.user_exists_by_username_or_email(username, ""):
            raise UserAlreadyExistsException(msg=f"Username {username} is already taken")

        token = secrets.token_urlsafe(32)
        expires_at = datetime.now() + timedelta(hours=24)
        hashed_password = get_password_hash(password)
        await self.pending_repo.create(
            email=email,
            username=username,
            password_hash=hashed_password,
            token=token,
            expires_at=expires_at,
        )

        from settings.general import BASE_URL
        verification_link = f"{BASE_URL}/verify-email?token={token}"
        await self.verification.send_activation_email_with_link(email, verification_link)

    async def activate_from_pending(self, token: str) -> str:
        """Create user from pending registration, return username. Raises InvalidToken if not found."""
        pending = await self.pending_repo.get_by_token(token)
        if not pending:
            raise InvalidToken("Invalid or expired activation link")

        if await self.repo.user_exists_by_username_or_email(pending.username, pending.email):
            await self.pending_repo.delete_by_token(token)
            raise UserAlreadyExistsException(msg="Email or username already registered")

        user_data = UserCreate(
            username=pending.username,
            email=pending.email,
            password="",  # Not used, we have hashed
            birthday=DEFAULT_BIRTHDAY,
            country_id=DEFAULT_COUNTRY_ID,
            gender=DEFAULT_GENDER,
        )
        new_user = await self.repo.create_user_simple(
            user_data, pending.password_hash, is_verified=True
        )
        await self.pending_repo.delete_by_token(token)
        return new_user.username

    def _generate_username(self, email: str) -> str:
        """Generate unique username from email prefix + random suffix."""
        prefix = re.sub(r"[^a-zA-Z0-9]", "", email.split("@")[0])[:20] or "user"
        return f"{prefix}_{uuid4().hex[:6]}"

    async def complete_registration(
        self,
        email: str,
        password: str,
        verification_token: str,
        country_id: int,
        birthday: date,
        gender: GenderEnum,
        name: Optional[str] = None,
        surname: Optional[str] = None,
    ) -> "User":
        """Create user after email activation. Validates token matches email. Username is auto-generated."""
        verified_email = await self.verification.verify_token(verification_token)
        if verified_email.lower() != email.lower():
            raise InvalidToken("Email does not match activation link")

        if await self.repo.user_exists_by_username_or_email("", email):
            raise UserAlreadyExistsException(msg=f"Email {email} already exists")

        username = self._generate_username(email)
        hashed_password = get_password_hash(password)
        user_data = UserCreate(
            username=username,
            email=email,
            password=password,
            birthday=birthday,
            country_id=country_id,
            gender=gender,
            name=name,
            surname=surname,
        )
        new_user = await self.repo.create_user_simple(
            user_data, hashed_password, is_verified=True
        )
        return new_user

    async def get_current_user(self, token: str) -> "User":
        """Decode an OAuth access <token> and return the UserResponse."""
        username = jwt_utils.get_username_from_token(token)
        user = await self.repo.get_by_username(username)  # Subscription status not needed for self
        return user

    async def authenticate_user(self, username_or_email: str, password: str) -> "User":
        """login_id can be username or email"""
        user = await self.repo.get_by_username_or_email(
            username_or_email, username_or_email
        )
        if not verify_password(password, user.password_hash):
            raise WrongPassword("Provided password is incorrect.")
        return user

    async def get_user_by_email(self, email: str) -> "User":
        user = await self.repo.get_by_email(email)
        return user

    async def reset_password(self, token: str, new_password: str):
        email = await self.verification.verify_token(token)
        user = await self.repo.get_by_email(email)
        password_hash = get_password_hash(new_password)
        update = UserUpdateInternal(password_hash=password_hash)
        await self.repo.update_user(user.id, update)

    async def get_user_by_id(self, user_id: int, current_user: "User") -> UserResponse:
        self.permissions.setup(current_user)

        view_level = self.permissions.get_user_view_level(user_id)
        target_user = await self.repo.get_user_by_id(
            user_id,
            current_user.id if current_user.id != user_id else None
        )

        # Calculate similarity and mutuality if viewing another user
        similarity = None
        mutuality = None
        if current_user.id != user_id:
            try:
                similarity = await self.similarity_repo.get_similarity(current_user.id, user_id)
                mutuality = await self.similarity_repo.get_mutuality(current_user.id, user_id)
            except Missing:
                # If no common answers, both will be None
                pass

        if view_level == UserViewLevel.full:
            user = UserResponse.from_user(target_user)
        else:
            user = UserResponse.from_user_other(target_user)

        # Add similarity and mutuality to response
        user.similarity = similarity
        user.mutuality = mutuality
        return user

    async def get_users(
        self, limit: int, offset: int, token: str
    ) -> list[UserResponse]:
        try:
            current_user = await self.get_current_user(token)
        except Missing:
            raise Unauthorized("You are not allowed to access users.")

        users = await self.repo.get_all_users_paginated(
            limit, offset, current_user.id
        )

        return [
            UserResponse.from_user_other(user)
            if user.id != current_user.id
            else UserResponse.from_user(user)
            for user in users
        ]

    async def get_users_by_ids(
        self,
        user_ids: list[int],
        current_user: "User"
    ) -> list[UserResponse]:
        """Get multiple users by their IDs with privacy settings applied."""
        users = await self.repo.get_users_by_ids(user_ids, current_user.id)

        # Apply privacy settings and convert to response objects
        responses = []
        for user in users:
            if user.id == current_user.id:
                responses.append(UserResponse.from_user(user))
            else:
                responses.append(UserResponse.from_user_other(user))

        return responses

    # async def create_user(self, user_data: UserCreate) -> UserResponse:
    #     # Ensure username or email doesn't already exist
    #     if await self.repo.user_exists_by_username_or_email(user_data.username, user_data.email):
    #         raise Missing("Username or email already exists.")
    #
    #     new_user = await self.repo.create_user(user_data)
    #     return UserResponse.from_orm(new_user)

    async def update_user(
        self, user_id: int, user_data: UserUpdate, current_user: "User"
    ) -> UserResponse:
        self.permissions.setup(current_user)
        if not self.permissions.can_edit_user(user_id):
            raise PermissionDenied("You are not allowed to update this user.")

        new_password_hash = None
        if user_data.old_password:
            if not verify_password(user_data.old_password, current_user.password_hash):
                raise WrongPassword("Provided password is incorrect.")
            if user_data.new_password is None:
                # TODO: move this to validation
                raise ConfigurationError("New password was not provided.")
            new_password_hash = get_password_hash(user_data.new_password)

        internal_update = UserUpdateInternal(
            name=user_data.name,
            surname=user_data.surname,
            birthday=user_data.birthday,
            country_id=user_data.country_id,
            gender=user_data.gender,
            description=user_data.description,
            profile_picture=user_data.profile_picture,
            settings=user_data.settings,
            password_hash=new_password_hash,
        )

        updated_user = await self.repo.update_user(user_id, internal_update)
        return UserResponse.from_user(updated_user)

    async def delete_user(self, user_id: int, current_user: "User") -> None:
        self.permissions.setup(current_user)
        if not self.permissions.can_edit_user(user_id):
            raise Unauthorized("You are not allowed to delete this user.")
        await self.repo.delete_user(user_id)

    async def get_settings(self, user_id: int, current_user: "User") -> UserSettings:
        self.permissions.setup(current_user)
        view_level = self.permissions.get_user_view_level(user_id)
        if view_level != UserViewLevel.full:
            raise PermissionDenied("You are not allowed to access this user's settings.")

        settings = await self.settings_repo.get_settings_by_user_id(user_id)
        return settings

    async def create_settings(
        self, user_id: int, settings_data: UserSettings, current_user: "User"
    ) -> UserSettings:
        self.permissions.setup(current_user)
        if not self.permissions.can_edit_user(user_id):
            raise PermissionDenied("You are not allowed to create settings for this user.")
        return await self.settings_repo.create_settings(user_id, settings_data)

    async def update_settings(
        self, user_id: int, settings_data: UserSettingsUpdate, current_user: "User"
    ) -> UserSettings:
        self.permissions.setup(current_user)
        if not self.permissions.can_edit_user(user_id):
            raise PermissionDenied("You are not allowed to update this user's settings.")

        return await self.settings_repo.update_settings(user_id, settings_data)

    async def delete_settings(self, user_id: int, current_user: "User") -> None:
        self.permissions.setup(current_user)
        if not self.permissions.can_edit_user(user_id):
            raise PermissionDenied("You are not allowed to delete this user's settings.")
        await self.settings_repo.delete_settings(user_id)

    async def get_similar_users(
        self,
        current_user: "User",
        sort_by: SimilaritySortEnum,
        connection_filter: ConnectionFilterEnum,
        time_range: TimeRangeEnum = TimeRangeEnum.last_year,
        limit: int = 10,
        offset: int = 0,
    ) -> list[UserResponse]:
        """Get a list of users similar to the current user based on various criteria."""
        # Calculate date range for filtering answers
        now = datetime.now()
        if time_range == TimeRangeEnum.last_day:
            start_date = now - timedelta(days=1)
        elif time_range == TimeRangeEnum.last_week:
            start_date = now - timedelta(weeks=1)
        elif time_range == TimeRangeEnum.last_month:
            start_date = now - timedelta(days=30)
        else:  # last_year
            start_date = now - timedelta(days=365)

        # Get users based on connection filter
        if connection_filter == ConnectionFilterEnum.followings:
            user_ids = await self.subscription_repo.get_following_ids(current_user.id)
        elif connection_filter == ConnectionFilterEnum.followers:
            user_ids = await self.subscription_repo.get_follower_ids(current_user.id)
        else:  # non_connected
            # FIXME: check if all users
            user_ids = await self.subscription_repo.get_non_connected_user_ids(current_user.id)

        logger.info(f'{connection_filter}: {user_ids}')

        # Get users with similarity/mutuality scores first
        user_ids_with_scores = await self.similarity_repo.get_top_scores(
            current_user_id=current_user.id,
            target_users=user_ids,
            sort_by=sort_by,
            start_date=start_date,
            limit=limit,
            offset=offset,
        )
        logger.info(f'user_ids_with_scores: {user_ids_with_scores}')

        if not user_ids_with_scores:
            return []

        # Get user details for users with scores
        scored_user_ids = [user_id for user_id, _ in user_ids_with_scores]
        users = await self.get_users_by_ids(scored_user_ids, current_user)
        users_dict = {user.id: user for user in users}

        # Add similarity and mutuality scores to user responses
        similar_users = []
        for user_id, scores in user_ids_with_scores:
            if user_id in users_dict:
                user = users_dict[user_id]
                user.similarity = schema.Similarity(
                    avg_similarity=scores.similarity,
                    common_total=0  # This field is not used in the frontend
                )
                user.mutuality = schema.Mutuality(
                    mutuality=scores.mutuality,
                    my_total=0,  # These fields are not used in the frontend
                    other_total=0,
                    common_total=0
                )
                similar_users.append(user)

        return similar_users


def build_user_service(
    repo: "UserRepository",
    settings_repo: "UserSettingsRepository",
    verification_service: "VerificationService",
    similarity_repo: "SimilarityRepository",
    subscription_repo: "SubscriptionRepository",
    pending_repo: "PendingRegistrationRepository",
) -> UserService:
    return UserService(
        repo, settings_repo, verification_service, similarity_repo, subscription_repo, pending_repo
    )
