from models.user import User


def test_user_creation():
    user = User(
        "Barack",
        "barack@example.com",
        "password123",
        "user",
        1
    )

    assert user.name == "Barack"
    assert user.email == "barack@example.com"
    assert user.password == "password123"
    assert user.role == "user"
    assert user.user_id == 1


def test_user_inheritance():
    user = User(
        "Barack",
        "barack@example.com",
        "password123"
    )

    assert user.name == "Barack"


def test_user_string():
    user = User(
        "Barack",
        "barack@example.com",
        "password123",
        "user",
        1
    )

    assert str(user) == "Barack - barack@example.com - user"