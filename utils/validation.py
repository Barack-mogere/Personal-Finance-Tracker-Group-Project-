from datetime import datetime


def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_valid_date(prompt):
    while True:
        date = input(prompt).strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Please enter the date in YYYY-MM-DD format.")