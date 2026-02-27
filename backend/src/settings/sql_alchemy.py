import os

SQLALCHEMY_ECHO = bool(int(os.getenv("SQLALCHEMY_ECHO", False)))  # 0 or 1
