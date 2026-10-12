import os
import secrets
from dotenv import load_dotenv

load_dotenv(override=True)

def verify_user(username: str, password: str) -> bool:
    expected_username = os.getenv("AUTH_USERNAME") or os.getenv("USERNAME") or ""
    expected_password = os.getenv("PASSWORD") or ""
    return secrets.compare_digest(username, expected_username) and secrets.compare_digest(password, expected_password)

def verify_key(api_key: str) -> bool:
    expected_key = os.getenv("API_KEY") or ""
    return secrets.compare_digest(api_key, expected_key)
