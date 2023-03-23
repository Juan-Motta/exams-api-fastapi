import hashlib
import binascii

from app.config.enviroments import CONFIG

def hash_password(password: str) -> str:
    salt = CONFIG["secret_key"]
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100_000)
    hashed_password = binascii.hexlify(dk)
    return f"pbkdf2_sha256$100000${hashed_password.decode()}"

def verify_password(stored_password: str, provided_password: str) -> bool:
    hashed_provided_password = hash_password(provided_password)
    return stored_password == hashed_provided_password