# Beatrice
from models.user import User
from utils.storage import JSONStorage
import hashlib


class AuthService:

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        return AuthService.hash_password(password) == hashed_password

    @staticmethod
    def register(name, email, password, role="user"):
        users = JSONStorage.load_data("data/users.json")

        for user in users:
            if user["email"] == email:
                return False

        hashed_password = AuthService.hash_password(password)

        new_user = User(
            name,
            email,
            hashed_password,
            role,
            len(users) + 1
        )

        user_data = {
            "id": new_user.user_id,
            "name": new_user.name,
            "email": new_user.email,
            "password": new_user.password,
            "role": new_user.role
        }

        users.append(user_data)

        JSONStorage.save_data(
            "data/users.json",
            users
        )

        return True

    @staticmethod
    def login(email, password):
        users = JSONStorage.load_data("data/users.json")

        for user in users:
            if user["email"] == email:

                if AuthService.verify_password(
                    password,
                    user["password"]
                ):
                    return User(
                        user["name"],
                        user["email"],
                        user["password"],
                        user["role"],
                        user["id"]
                    )

                return None

        return None

    @staticmethod
    def get_all_users():
        users = JSONStorage.load_data("data/users.json")

        return users