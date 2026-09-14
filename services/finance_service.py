from models.income import Income
from models.expense import Expense
from utils.storage import JSONStorage


class FinanceService:

    @staticmethod
    def add_income(user_id, amount, category, description, date):
        transactions = JSONStorage.load_data(
            "data/transactions.json"
        )

        income = Income(
            amount,
            category,
            description,
            date,
            user_id
        )

        transaction_data = {
            "id": len(transactions) + 1,
            "user_id": income.user_id,
            "type": "income",
            "amount": income.amount,
            "category": income.category,
            "description": income.description,
            "date": income.date
        }

        transactions.append(transaction_data)

        JSONStorage.save_data(
            "data/transactions.json",
            transactions
        )

        return True

    @staticmethod
    def add_expense(user_id, amount, category, description, date):
        transactions = JSONStorage.load_data(
            "data/transactions.json"
        )

        expense = Expense(
            amount,
            category,
            description,
            date,
            user_id
        )

        transaction_data = {
            "id": len(transactions) + 1,
            "user_id": expense.user_id,
            "type": "expense",
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date
        }

        transactions.append(transaction_data)

        JSONStorage.save_data(
            "data/transactions.json",
            transactions
        )

        return True

    @staticmethod
    def view_transactions(user_id):
        transactions = JSONStorage.load_data(
            "data/transactions.json"
        )

        user_transactions = []

        for transaction in transactions:
            if transaction["user_id"] == user_id:
                user_transactions.append(transaction)

        return user_transactions

    @staticmethod
    def calculate_balance(user_id):
        transactions = FinanceService.view_transactions(user_id)

        balance = 0

        for transaction in transactions:
            if transaction["type"] == "income":
                balance += transaction["amount"]

            elif transaction["type"] == "expense":
                balance -= transaction["amount"]

        return balance

    @staticmethod
    def financial_summary(user_id):
        transactions = FinanceService.view_transactions(user_id)

        total_income = 0
        total_expenses = 0

        for transaction in transactions:
            if transaction["type"] == "income":
                total_income += transaction["amount"]

            elif transaction["type"] == "expense":
                total_expenses += transaction["amount"]

        balance = total_income - total_expenses

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": balance
        }