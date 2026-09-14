from services.finance_service import FinanceService
from unittest.mock import patch


def test_add_income():
    transactions = []

    with patch(
        "services.finance_service.JSONStorage.load_data",
        return_value=transactions
    ), patch(
        "services.finance_service.JSONStorage.save_data"
    ) as mock_save:

        result = FinanceService.add_income(
            1,
            50000,
            "Salary",
            "Monthly salary",
            "2026-09-14"
        )

    assert result is True

    saved_transactions = mock_save.call_args[0][1]

    assert len(saved_transactions) == 1
    assert saved_transactions[0]["user_id"] == 1
    assert saved_transactions[0]["type"] == "income"
    assert saved_transactions[0]["amount"] == 50000
    assert saved_transactions[0]["category"] == "Salary"


def test_add_expense():
    transactions = []

    with patch(
        "services.finance_service.JSONStorage.load_data",
        return_value=transactions
    ), patch(
        "services.finance_service.JSONStorage.save_data"
    ) as mock_save:

        result = FinanceService.add_expense(
            1,
            500,
            "Food",
            "Lunch",
            "2026-09-14"
        )

    assert result is True

    saved_transactions = mock_save.call_args[0][1]

    assert len(saved_transactions) == 1
    assert saved_transactions[0]["user_id"] == 1
    assert saved_transactions[0]["type"] == "expense"
    assert saved_transactions[0]["amount"] == 500
    assert saved_transactions[0]["category"] == "Food"


def test_view_transactions():
    transactions = [
        {
            "id": 1,
            "user_id": 1,
            "type": "income",
            "amount": 50000,
            "category": "Salary",
            "description": "Monthly salary",
            "date": "2026-09-14"
        },
        {
            "id": 2,
            "user_id": 2,
            "type": "expense",
            "amount": 1000,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-09-14"
        }
    ]

    with patch(
        "services.finance_service.JSONStorage.load_data",
        return_value=transactions
    ):
        result = FinanceService.view_transactions(1)

    assert len(result) == 1
    assert result[0]["user_id"] == 1
    assert result[0]["type"] == "income"


def test_calculate_balance():
    transactions = [
        {
            "id": 1,
            "user_id": 1,
            "type": "income",
            "amount": 50000,
            "category": "Salary",
            "description": "Monthly salary",
            "date": "2026-09-14"
        },
        {
            "id": 2,
            "user_id": 1,
            "type": "expense",
            "amount": 500,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-09-14"
        },
        {
            "id": 3,
            "user_id": 1,
            "type": "expense",
            "amount": 1500,
            "category": "Transport",
            "description": "Bus fare",
            "date": "2026-09-14"
        }
    ]

    with patch(
        "services.finance_service.JSONStorage.load_data",
        return_value=transactions
    ):
        balance = FinanceService.calculate_balance(1)

    assert balance == 48000


def test_financial_summary():
    transactions = [
        {
            "id": 1,
            "user_id": 1,
            "type": "income",
            "amount": 50000,
            "category": "Salary",
            "description": "Monthly salary",
            "date": "2026-09-14"
        },
        {
            "id": 2,
            "user_id": 1,
            "type": "expense",
            "amount": 500,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-09-14"
        },
        {
            "id": 3,
            "user_id": 1,
            "type": "expense",
            "amount": 1500,
            "category": "Transport",
            "description": "Bus fare",
            "date": "2026-09-14"
        }
    ]

    with patch(
        "services.finance_service.JSONStorage.load_data",
        return_value=transactions
    ):
        summary = FinanceService.financial_summary(1)

    assert summary["total_income"] == 50000
    assert summary["total_expenses"] == 2000
    assert summary["balance"] == 48000