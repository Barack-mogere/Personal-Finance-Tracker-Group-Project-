# Beatrice
import hashlib
import json

from models.user import User


class AuthService:

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hashed_password):
        return AuthService.hash_password(password) == hashed_password

    @staticmethod
    def register(name, email, password, role="user"):
        with open("data/users.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["email"] == email:
                return False

        hashed_password = AuthService.hash_password(password)

        new_user = User(
            name,
            email,
            hashed_password,
            role
        )

        user_data = {
            "id": len(users) + 1,
            "name": new_user.name,
            "email": new_user.email,
            "password": new_user.password,
            "role": new_user.role
        }

        users.append(user_data)

        with open("data/users.json", "w") as file:
            json.dump(users, file, indent=4)

        return True

    @staticmethod
    def login(email, password):
        with open("data/users.json", "r") as file:
            users = json.load(file)

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
                        user["role"]
                    )

                return None

        return None