import logging
from datetime import timedelta

from infrastructure.api.auth.jwt_utils import get_email_from_token, create_token
from settings.general import BASE_URL
from settings.security import EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES


from app.services.email.email import EmailService

logger = logging.getLogger(__name__)

ACTIVATION_CODE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Activate Your Account</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.5; color: #333;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f7f7f7; padding: 20px 12px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #ffffff; max-width: 100%;">
          <tr>
            <td style="padding: 24px 20px 16px 20px; text-align: center;">
              <img src="https://drive.google.com/uc?export=view&id=1AM84Ekjy5CuK3kafmL0uxgpBylc5njws" alt="Logo" style="height: 32px; margin-bottom: 16px;">
              <div style="font-size: 20px; font-weight: 600; color: #1a1a1a;">Welcome!</div>
            </td>
          </tr>
          <tr>
            <td style="padding: 0 20px 24px 20px;">
              <p style="margin: 0 0 16px 0; font-size: 15px;">Hi there,</p>
              <p style="margin: 0 0 16px 0; font-size: 15px;">Thanks for signing up! Here is your activation code:</p>
              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 20px 0;">
                <tr>
                  <td align="center">
                    <div style="display: inline-block; padding: 16px 32px; background-color: #f0f0f0; border-radius: 8px; font-size: 28px; font-weight: 600; letter-spacing: 6px; font-family: monospace;">{activation_code}</div>
                  </td>
                </tr>
              </table>
              <p style="margin: 20px 0 0 0; font-size: 15px;">Enter this code on the sign-in page to activate your account.</p>
              <p style="margin: 12px 0 0 0; color: #666; font-size: 13px;">This code expires in 24 hours.</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 16px 20px; background-color: #f9f9f9; border-top: 1px solid #e5e5e5;">
              <p style="margin: 0; color: #666; font-size: 12px;">If you didn't create an account, you can safely ignore this email.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""

VERIFY_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verify Your Email</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.5; color: #333;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f7f7f7; padding: 20px 12px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #ffffff; max-width: 100%;">
          <tr>
            <td style="padding: 24px 20px 16px 20px; text-align: center;">
              <img src="https://drive.google.com/uc?export=view&id=1AM84Ekjy5CuK3kafmL0uxgpBylc5njws" alt="Logo" style="height: 32px; margin-bottom: 16px;">
              <div style="font-size: 20px; font-weight: 600; color: #1a1a1a;">Welcome!</div>
            </td>
          </tr>
          <tr>
            <td style="padding: 0 20px 24px 20px;">
              <p style="margin: 0 0 16px 0; font-size: 15px;">Hi there,</p>
              <p style="margin: 0 0 16px 0; font-size: 15px;">Thanks for signing up! We're excited to have you on board.</p>
              <p style="margin: 0 0 16px 0; font-size: 15px;">To get started, please verify your email address:</p>
              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 20px 0;">
                <tr>
                  <td align="center">
                    <a href="{verification_link}" style="display: block; padding: 16px 24px; background-color: #000000; color: #ffffff; text-decoration: none; border-radius: 6px; font-weight: 500; font-size: 15px;">Verify Email Address</a>
                  </td>
                </tr>
              </table>
              <p style="margin: 20px 0 0 0; color: #666; font-size: 13px;">This link will expire in 24 hours.</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 16px 20px; background-color: #f9f9f9; border-top: 1px solid #e5e5e5;">
              <p style="margin: 0; color: #666; font-size: 12px;">If you didn't create an account, you can safely ignore this email.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""

RESET_EMAIL_TEMPLATE = """
Hi {user_name},

We received a request to reset your password for your VECE account. 
If you did not make this request, you can safely ignore this email.

To reset your password, please click the link below:
{reset_link}

Best regards,
VECE Team
"""


class VerificationService:
    """Handles email verification-related operations."""

    def __init__(self, email_service: "EmailService"):
        self.email_service = email_service

    @staticmethod
    def generate_verification_token(user_email: str) -> str:
        data = {"sub": user_email}
        expires = timedelta(minutes=EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES)
        token = create_token(data, expires)
        return token

    @staticmethod
    async def verify_token(token: str) -> str:
        email = get_email_from_token(token)
        return email

    async def send_verification_email(self, user_email: str, user_name: str):
        """Sends a verification email to the user."""
        verification_token = self.generate_verification_token(user_email)

        verification_link = f"{BASE_URL}/verify-email?token={verification_token}"

        subject = "Verify Your Email"
        body = VERIFY_EMAIL_TEMPLATE.format(
            user_name=user_name, verification_link=verification_link
        )

        await self.email_service.send_email(user_email, subject, body, is_html=True)

    async def send_activation_email_with_link(self, email: str, verification_link: str):
        """Sends activation email with a pre-built verification link (e.g. for pending registration)."""
        subject = "Activate your VECE account"
        body = VERIFY_EMAIL_TEMPLATE.format(
            user_name="there", verification_link=verification_link
        )
        await self.email_service.send_email(email, subject, body, is_html=True)

    async def send_activation_email_with_code(self, email: str, activation_code: str):
        """Sends activation email with a 6-digit code (for pending registration)."""
        subject = "Activate your VECE account"
        body = ACTIVATION_CODE_TEMPLATE.format(activation_code=activation_code)
        await self.email_service.send_email(email, subject, body, is_html=True)

    async def send_password_reset_email(self, user_email: str, user_name: str):
        """Sends a verification email to the user."""
        reset_token = self.generate_verification_token(user_email)

        reset_link = f"{BASE_URL}/reset-password?token={reset_token}"

        subject = "Reset Your Password"
        body = RESET_EMAIL_TEMPLATE.format(user_name=user_name, reset_link=reset_link)

        await self.email_service.send_email(user_email, subject, body)


def build_verification_service(email_service: "EmailService") -> VerificationService:
    return VerificationService(email_service)
