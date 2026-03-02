from enum import Enum

from typing import Optional

from app.exceptions import PermissionDenied
from app.schema.user import Role, User


class BasePolicy:
    def __init__(self, current_user: Optional[User] = None):
        self.user = current_user

    def setup(self, current_user: User):
        self.user = current_user

    def is_admin(self) -> bool:
        user = self.user
        return (
                user is not None and
                user.is_verified and
                user.is_active and
                user.role == Role.admin
        )

    def is_self(self, target_user_id: int) -> bool:
        user = self.user
        return (
                user is not None and
                user.is_verified and
                user.is_active and
                user.id == target_user_id
        )

    def is_authenticated(self) -> bool:
        return self.user is not None and self.user.is_verified and self.user.is_active

    # def is_admin(self) -> bool:
    #     return self.is_authenticated() and self.user.role == Role.admin
    #
    # def is_self(self, target_user_id: int) -> bool:
    #     return self.is_authenticated() and self.user.id == target_user_id

    def allow_if_admin(self) -> bool:
        return self.is_admin()


class UserViewLevel(str, Enum):
    none = "none"
    other = "other"
    full = "full"


class UserPermissions(BasePolicy):

    def get_user_view_level(self, target_user_id: int) -> UserViewLevel:
        if not self.user:
            raise PermissionDenied("You cannot view this user.")

        if self.is_admin():
            return UserViewLevel.full

        if self.is_self(target_user_id):
            return UserViewLevel.full

        if self.can_view_user_limited():
            return UserViewLevel.other

        raise PermissionDenied("You cannot view this user.")

    def can_view_user_limited(self) -> bool:
        return self.is_authenticated()

    def can_edit_user(self, target_user_id: int) -> bool:
        return self.is_admin() or self.is_self(target_user_id)

    def can_manage_settings(self, target_user_id: int) -> bool:
        return self.can_edit_user(target_user_id)
