import logging
import re

import httpx

from settings import email as email_settings

logger = logging.getLogger(__name__)

RESEND_API_URL = "https://api.resend.com/emails"


class EmailSendError(Exception):
    pass


class EmailService:
    def __init__(self):
        self.api_key = (email_settings.RESEND_API_KEY or "").strip()
        self.sender_email = email_settings.EMAIL_FROM
        self._use_console = not self.api_key
        if self._use_console:
            logger.warning(
                "RESEND_API_KEY is empty — emails will NOT be sent, links printed to logs only"
            )
        else:
            logger.info("Email configured: sending via Resend (from %s)", self.sender_email)

    async def send_email(self, to_email: str, subject: str, body: str, is_html: bool = False):
        """Sends an email via Resend API. If RESEND_API_KEY is empty, prints link to console (local dev)."""
        if self._use_console:
            link_match = re.search(r'href="([^"]+)"', body)
            if link_match:
                link = link_match.group(1)
                logger.warning(
                    "RESEND_API_KEY not set — printing activation link to console (no email sent):\n"
                    f"  To: {to_email}\n"
                    f"  Subject: {subject}\n"
                    f"  Link: {link}"
                )
                print(f"\n>>> [LOCAL DEV] Activation link for {to_email}: {link}\n")
            else:
                logger.warning(
                    f"RESEND_API_KEY not set — no link found in body. To: {to_email}, Subject: {subject}"
                )
            return

        payload = {
            "from": self.sender_email,
            "to": [to_email],
            "subject": subject,
        }
        if is_html:
            payload["html"] = body
        else:
            payload["text"] = body

        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(
                    RESEND_API_URL,
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    timeout=30.0,
                )
                resp.raise_for_status()
                logger.info("Email sent successfully to %s", to_email)
            except httpx.HTTPStatusError as e:
                logger.exception("Resend API error sending email to %s: %s", to_email, e)
                raise EmailSendError(f"Failed to send email: {e.response.text}")
            except Exception as e:
                logger.exception("Error sending email to %s: %s", to_email, e)
                raise EmailSendError(f"Failed to send email: {e}")


def build_email_service() -> EmailService:
    return EmailService()
