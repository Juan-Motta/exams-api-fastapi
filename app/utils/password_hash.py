import hashlib
import binascii

from app.config.enviroments import CONFIG

def hash_password(password: str) -> str:
    salt = CONFIG["secret_key"]  
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    hashed_password = binascii.hexlify(dk)
    return f'{salt.hex()}:{hashed_password.decode()}'

def verify_password(stored_password: str, provided_password: str) -> bool:
    salt, hashed_password = stored_password.split(':')
    salt = bytes.fromhex(salt)
    hashed_provided_password = hash_password(provided_password, salt)
    return hashed_password == hashed_provided_password.split(':')[1]