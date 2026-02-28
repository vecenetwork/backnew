import os

# Gmail: use EMAIL_ADDRESS=your@gmail.com + App Password. info@vece.ai works with Google Workspace
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "info@vece.ai")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
