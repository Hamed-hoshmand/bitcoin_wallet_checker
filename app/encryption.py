from cryptography.fernet import Fernet
from .config import Config

cipher_suite = Fernet(Config.ENCRYPTION_KEY.encode())

def encrypt_seed_phrase(seed_phrase):
    return cipher_suite.encrypt(seed_phrase.encode()).decode()

def decrypt_seed_phrase(encrypted_phrase):
    return cipher_suite.decrypt(encrypted_phrase.encode()).decode()
