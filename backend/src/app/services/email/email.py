import logging
import re
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from settings import email as email_settings

logger = logging.getLogger(__name__)


class EmailSendError(Exception):
    pass


class EmailService:
    SMTP_HOST = email_settings.SMTP_HOST
    SMTP_PORT = email_settings.SMTP_PORT

    def __init__(self):
        self.sender_email, self.sender_password = self.get_credentials()
        self._use_console = not (self.sender_password and self.sender_password.strip())

    @staticmethod
    def get_credentials():
        return email_settings.EMAIL_ADDRESS, email_settings.EMAIL_PASSWORD

    async def send_email(self, to_email: str, subject: str, body: str, is_html: bool = False):
        """Sends an email with the given subject and body. If EMAIL_PASSWORD is empty, prints link to console (local dev)."""
        if self._use_console:
            # Local dev: extract activation/verification link and print to console
            link_match = re.search(r'href="([^"]+)"', body)
            if link_match:
                link = link_match.group(1)
                logger.warning(
                    "EMAIL_PASSWORD not set — printing activation link to console (no email sent):\n"
                    f"  To: {to_email}\n"
                    f"  Subject: {subject}\n"
                    f"  Link: {link}"
                )
                print(f"\n>>> [LOCAL DEV] Activation link for {to_email}: {link}\n")
            else:
                logger.warning(f"EMAIL_PASSWORD not set — no link found in body. To: {to_email}, Subject: {subject}")
            return

        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html" if is_html else "plain"))

        try:
            await aiosmtplib.send(
                msg,
                hostname=self.SMTP_HOST,
                port=self.SMTP_PORT,
                start_tls=True,
                username=self.sender_email,
                password=self.sender_password,
            )
            logger.info("Email sent successfully!")
        except Exception as e:
            logger.exception(f"Error sending email: {e}")
            raise EmailSendError("Failed to send email.")


def build_email_service() -> EmailService:
    return EmailService()
