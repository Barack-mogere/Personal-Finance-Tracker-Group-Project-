# Beatrice
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user is None:
            print("Please log in first.")
            return None

        return func(user, *args, **kwargs)

    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user is None:
            print("Please log in first.")
            return None

        if user.role != "admin":
            print("Admin access required.")
            return None

        return func(user, *args, **kwargs)

    return wrapper