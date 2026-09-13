# Barack
from services.auth_service import AuthService


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
            print("Login selected.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()