from typing import TYPE_CHECKING

from app.exceptions import Unauthorized, Missing, Duplicate
from app.schema.user import User, Role
from app.schema.waitlist import WaitlistData

if TYPE_CHECKING:
    from app.services.email.email import EmailService
    from infrastructure.repository.waitlist import WaitlistRepository


WAITLIST_EMAIL = """Hi!

Thanks for signing up — you've been successfully added to the VECE waitlist!

We're excited to have you on board. You'll be the first to know when we launch or have important updates to share.

Talk soon,
The VECE Team
"""


class EmailAlreadyExistsError(Duplicate):
    pass


class WaitlistService:
    def __init__(self, waitlist_repo: "WaitlistRepository", email_service: "EmailService"):
        self.waitlist_repo = waitlist_repo
        self.email_service = email_service

    async def join_waitlist(self, data: WaitlistData) -> WaitlistData:
        """Create a new waitlist entry, or raise if email already used."""
        try:
            await self.waitlist_repo.get_by_email(data.email)
            raise EmailAlreadyExistsError("Email already in waitlist")
        except Missing:
            return await self.waitlist_repo.create(data)

    async def get_by_email(self, email: str, user: User) -> WaitlistData:
        """Allow only admin to access arbitrary email entries"""
        if user.role != Role.admin:
            raise Unauthorized("Only admins can view waitlist data by email")
        return await self.waitlist_repo.get_by_email(email)

    async def list_all(self, user: User, limit: int = 100, offset: int = 0) -> list[WaitlistData]:
        """Admin-only paginated listing of all waitlist entries"""
        if user.role != Role.admin:
            raise Unauthorized("Only admins can list the waitlist")
        return await self.waitlist_repo.list_all(limit=limit, offset=offset)

    async def delete_by_email(self, email: str, user: User):
        """Allow only admin to delete waitlist entries"""
        if user.role != Role.admin:
            raise Unauthorized("Only admins can delete waitlist entries")
        await self.waitlist_repo.delete_by_email(email)

    async def send_verification_email(self, user_email: str):
        subject = "VECE waitlist"
        body = WAITLIST_EMAIL

        await self.email_service.send_email(user_email, subject, body)


def build_waitlist_service(repo: "WaitlistRepository", email_service: "EmailService") -> WaitlistService:
    return WaitlistService(repo, email_service)
