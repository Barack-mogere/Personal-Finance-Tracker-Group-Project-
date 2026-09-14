# Barack

import argparse

from services.auth_service import AuthService
from services.finance_service import FinanceService
from utils.decorators import admin_required
from utils.validation import (
    get_positive_amount,
    get_non_empty_input,
    get_valid_date
)

from rich.console import Console
from rich.table import Table


console = Console()

def register():
    print("\n========== REGISTER ==========")

    name = get_non_empty_input("Enter your name: ")
    email = get_non_empty_input("Enter your email: ")
    password = get_non_empty_input("Enter your password: ")

    success = AuthService.register(
        name,
        email,
        password
    )

    if success:
        print("\nRegistration successful!")

    else:
        print("\nEmail already exists.")


def login():
    print("\n========== LOGIN ==========")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = AuthService.login(
        email,
        password
    )

    if user:
        print(f"\nWelcome, {user.name}!")
        print(f"Role: {user.role}")
        print(f"User ID: {user.user_id}")

        return user

    else:
        print("\nInvalid email or password.")
        return None


def add_income(user):
    print("\n========== ADD INCOME ==========")

    amount = get_positive_amount("Enter amount: ")
    category = get_non_empty_input("Enter category: ")
    description = get_non_empty_input("Enter description: ")
    date = get_valid_date("Enter date (YYYY-MM-DD): ")

    success = FinanceService.add_income(
        user.user_id,
        amount,
        category,
        description,
        date
    )

    if success:
        print("\nIncome added successfully!")


def add_expense(user):
    print("\n========== ADD EXPENSE ==========")

    amount = get_positive_amount("Enter amount: ")
    category = get_non_empty_input("Enter category: ")
    description = get_non_empty_input("Enter description: ")
    date = get_valid_date("Enter date (YYYY-MM-DD): ")

    success = FinanceService.add_expense(
        user.user_id,
        amount,
        category,
        description,
        date
    )

    if success:
        print("\nExpense added successfully!")


def view_transactions(user):
    transactions = FinanceService.view_transactions(
        user.user_id
    )

    if not transactions:
        console.print(
            "\n[yellow]You have no transactions yet.[/yellow]"
        )
        return

    table = Table(
        title="Your Transactions"
    )

    table.add_column("Type")
    table.add_column("Amount")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("Date")

    for transaction in transactions:
        table.add_row(
            transaction["type"].title(),
            f"Ksh {transaction['amount']}",
            transaction["category"],
            transaction["description"],
            transaction["date"]
        )

    console.print(table)

def view_balance(user):
    balance = FinanceService.calculate_balance(
        user.user_id
    )

    table = Table(
        title="Your Current Balance"
    )

    table.add_column("Account")
    table.add_column("Balance")

    table.add_row(
        user.name,
        f"Ksh {balance}"
    )

    console.print(table)

def financial_summary(user):
    summary = FinanceService.financial_summary(
        user.user_id
    )

    table = Table(
        title="Financial Summary"
    )

    table.add_column("Category")
    table.add_column("Amount")

    table.add_row(
        "Total Income",
        f"Ksh {summary['total_income']}"
    )

    table.add_row(
        "Total Expenses",
        f"Ksh {summary['total_expenses']}"
    )

    table.add_row(
        "Balance",
        f"Ksh {summary['balance']}"
    )

    console.print(table)

def user_menu(user):
    while True:
        print("\n========================================")
        print(f"        WELCOME, {user.name.upper()}")
        print("========================================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Financial Summary")
        print("6. Logout")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_income(user)

        elif choice == "2":
            add_expense(user)

        elif choice == "3":
            view_transactions(user)

        elif choice == "4":
            view_balance(user)

        elif choice == "5":
            financial_summary(user)

        elif choice == "6":
            print("\nLogging out...")
            break

        else:
            print("Invalid option. Please try again.")


def admin_menu(user):
    while True:
        print("\n========================================")
        print(f"        ADMIN PANEL - {user.name.upper()}")
        print("========================================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Financial Summary")
        print("6. View All Users")
        print("7. Logout")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_income(user)

        elif choice == "2":
            add_expense(user)

        elif choice == "3":
            view_transactions(user)

        elif choice == "4":
            view_balance(user)

        elif choice == "5":
            financial_summary(user)

        elif choice == "6":
            view_all_users(user)

        elif choice == "7":
            print("\nLogging out...")
            break

        else:
            print("Invalid option. Please try again.")


def main_menu():
    while True:
        print("\n========================================")
        print("       PERSONAL FINANCE TRACKER")
        print("========================================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()

            if user:
                if user.role == "admin":
                    admin_menu(user)
                else:
                    user_menu(user)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()