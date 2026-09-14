from services.auth_service import AuthService


def test_password_hashing():
    password = "mypassword123"

    hashed_password = AuthService.hash_password(password)

    assert hashed_password != password
    assert AuthService.verify_password(
        password,
        hashed_password
    )


def test_register_user(tmp_path, monkeypatch):
    test_file = tmp_path / "users.json"

    test_file.write_text("[]")

    monkeypatch.setattr(
        "services.auth_service.JSONStorage.load_data",
        lambda filename: []
    )

    saved_users = []

    monkeypatch.setattr(
        "services.auth_service.JSONStorage.save_data",
        lambda filename, data: saved_users.extend(data)
    )

    result = AuthService.register(
        "Test User",
        "test@example.com",
        "password123"
    )

    assert result is True
    assert len(saved_users) == 1
    assert saved_users[0]["name"] == "Test User"
    assert saved_users[0]["email"] == "test@example.com"


def test_duplicate_email():
    existing_users = [
        {
            "id": 1,
            "name": "Existing User",
            "email": "test@example.com",
            "password": "hashedpassword",
            "role": "user"
        }
    ]

    original_load = AuthService.register

    from unittest.mock import patch

    with patch(
        "services.auth_service.JSONStorage.load_data",
        return_value=existing_users
    ):
        result = AuthService.register(
            "Another User",
            "test@example.com",
            "password123"
        )

    assert result is False


def test_login_success():
    password = "password123"
    hashed_password = AuthService.hash_password(password)

    users = [
        {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
            "password": hashed_password,
            "role": "user"
        }
    ]

    from unittest.mock import patch

    with patch(
        "services.auth_service.JSONStorage.load_data",
        return_value=users
    ):
        user = AuthService.login(
            "test@example.com",
            password
        )

    assert user is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"
    assert user.role == "user"


def test_login_failure():
    users = [
        {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
            "password": AuthService.hash_password("correctpassword"),
            "role": "user"
        }
    ]

    from unittest.mock import patch

    with patch(
        "services.auth_service.JSONStorage.load_data",
        return_value=users
    ):
        user = AuthService.login(
            "test@example.com",
            "wrongpassword"
        )

    assert user is None