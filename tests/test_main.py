from unittest.mock import patch

import main
from models.user import User


def test_register_success(capsys):
    with patch(
        "main.get_non_empty_input",
        side_effect=[
            "Test User",
            "test@example.com",
            "password123"
        ]
    ), patch(
        "main.AuthService.register",
        return_value=True
    ):

        main.register()

    captured = capsys.readouterr()

    assert "Registration successful!" in captured.out


def test_register_duplicate_email(capsys):
    with patch(
        "main.get_non_empty_input",
        side_effect=[
            "Test User",
            "test@example.com",
            "password123"
        ]
    ), patch(
        "main.AuthService.register",
        return_value=False
    ):

        main.register()

    captured = capsys.readouterr()

    assert "Email already exists." in captured.out


def test_login_success(capsys):
    user = User(
        "Test User",
        "test@example.com",
        "hashedpassword",
        "user",
        1
    )

    with patch(
        "main.input",
        side_effect=[
            "test@example.com",
            "password123"
        ]
    ), patch(
        "main.AuthService.login",
        return_value=user
    ):

        result = main.login()

    captured = capsys.readouterr()

    assert result == user
    assert "Welcome, Test User!" in captured.out


def test_login_failure(capsys):
    with patch(
        "main.input",
        side_effect=[
            "test@example.com",
            "wrongpassword"
        ]
    ), patch(
        "main.AuthService.login",
        return_value=None
    ):

        result = main.login()

    captured = capsys.readouterr()

    assert result is None
    assert "Invalid email or password." in captured.out


def test_add_income(capsys):
    user = User(
        "Test User",
        "test@example.com",
        "hashedpassword",
        "user",
        1
    )

    with patch(
        "main.get_positive_amount",
        return_value=50000
    ), patch(
        "main.get_non_empty_input",
        side_effect=[
            "Salary",
            "Monthly salary"
        ]
    ), patch(
        "main.get_valid_date",
        return_value="2026-09-14"
    ), patch(
        "main.FinanceService.add_income",
        return_value=True
    ):

        main.add_income(user)

    captured = capsys.readouterr()

    assert "Income added successfully!" in captured.out


def test_add_expense(capsys):
    user = User(
        "Test User",
        "test@example.com",
        "hashedpassword",
        "user",
        1
    )

    with patch(
        "main.get_positive_amount",
        return_value=500
    ), patch(
        "main.get_non_empty_input",
        side_effect=[
            "Food",
            "Lunch"
        ]
    ), patch(
        "main.get_valid_date",
        return_value="2026-09-14"
    ), patch(
        "main.FinanceService.add_expense",
        return_value=True
    ):

        main.add_expense(user)

    captured = capsys.readouterr()

    assert "Expense added successfully!" in captured.out