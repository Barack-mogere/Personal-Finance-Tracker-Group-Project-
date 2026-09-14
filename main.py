# Barack
from services.auth_service import AuthService
from services.finance_service import FinanceService


def register():
    print("\n========== REGISTER ==========")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

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

        return user

    else:
        print("\nInvalid email or password.")
        return None


def add_income(user):
    print("\n========== ADD INCOME ==========")

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    success = FinanceService.add_income(
        user.user_id,
        amount,
        category,
        description,
        date
    )

    if success:
        print("\nIncome added successfully!")


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
            print("Add Expense selected.")

        elif choice == "3":
            print("View Transactions selected.")

        elif choice == "4":
            print("View Balance selected.")

        elif choice == "5":
            print("Financial Summary selected.")

        elif choice == "6":
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
                user_menu(user)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()