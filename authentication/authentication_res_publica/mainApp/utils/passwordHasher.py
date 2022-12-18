import string
from Crypto.Hash import SHA256
import random


def generate_password(size: int) -> str:
    """Функция для создания пароля"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


def generate_hash(password: str) -> str:
    """Функция для создания хэша пароля"""
    hash_obj = SHA256.new(password.encode())
    return SHA256.new(hash_obj.digest()).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    """Функция для проверки хэша пароля"""
    new_hash = generate_hash(password)
    return new_hash == password_hash
