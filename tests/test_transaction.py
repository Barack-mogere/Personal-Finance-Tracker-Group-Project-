from models.transaction import Transaction
from models.income import Income
from models.expense import Expense


def test_transaction_creation():
    transaction = Transaction(
        1000,
        "Food",
        "Lunch",
        "2026-09-14",
        1
    )

    assert transaction.amount == 1000
    assert transaction.category == "Food"
    assert transaction.description == "Lunch"
    assert transaction.date == "2026-09-14"
    assert transaction.user_id == 1


def test_income_inheritance():
    income = Income(
        50000,
        "Salary",
        "Monthly salary",
        "2026-09-14",
        1
    )

    assert isinstance(income, Transaction)
    assert income.amount == 50000
    assert income.category == "Salary"


def test_expense_inheritance():
    expense = Expense(
        500,
        "Food",
        "Lunch",
        "2026-09-14",
        1
    )

    assert isinstance(expense, Transaction)
    assert expense.amount == 500
    assert expense.category == "Food"


def test_income_string():
    income = Income(
        50000,
        "Salary",
        "Monthly salary",
        "2026-09-14",
        1
    )

    assert str(income) == "Income: Salary - Ksh 50000 - Monthly salary"


def test_expense_string():
    expense = Expense(
        500,
        "Food",
        "Lunch",
        "2026-09-14",
        1
    )

    assert str(expense) == "Expense: Food - Ksh 500 - Lunch"