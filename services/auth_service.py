# Beatrice
import hashlib


class AuthService:

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        return AuthService.hash_password(password) == hashed_password