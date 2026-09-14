# Personal Finance Tracker

A simple Python Command-Line Interface (CLI) application that helps users manage their personal finances by recording income and expenses, viewing transactions, checking their balance, and viewing a financial summary.

## Project Overview

The Personal Finance Tracker is designed for students and young adults who want a simple way to keep track of their money.

Users can create an account, log in securely, record their income and expenses, and view their financial information. The application stores data using JSON files so that information is available even after the program is closed.

The project demonstrates Object-Oriented Programming (OOP), authentication, file persistence, input validation, automated testing, and CLI development in Python.

## Features

* User registration
* User login
* Password hashing
* User and Admin roles
* Add income
* Add expenses
* View personal transactions
* Calculate current balance
* View financial summary
* Input validation
* JSON data persistence
* Rich tables for displaying financial information
* Command-line help and version information
* Automated tests using pytest

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* argparse
* Rich
* pytest
* Git and GitHub

## Project Structure

```text
personal-finance-tracker/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── transaction.py
│   ├── income.py
│   └── expense.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   └── finance_service.py
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   ├── storage.py
│   └── validation.py
│
├── data/
│   ├── users.json
│   └── transactions.json
│
└── tests/
    ├── __init__.py
    ├── test_user.py
    ├── test_transaction.py
    ├── test_auth.py
    ├── test_finance_service.py
    ├── test_validation.py
    ├── test_decorators.py
    └── test_main.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Barack-mogere/Personal-Finance-Tracker-Group-Project-.git
```

### 2. Navigate into the project

```bash
cd Personal-Finance-Tracker-Group-Project-
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application with:

```bash
python main.py
```

The application will display an interactive menu where users can register, log in, manage their finances, and exit the program.

### Command-Line Options

Display the available command-line options:

```bash
python main.py --help
```

Display the application version:

```bash
python main.py --version
```

## How Authentication Works

When a user registers:

1. The user provides their name, email, and password.
2. The password is hashed before being stored.
3. The user information is saved in `data/users.json`.

When a user logs in:

1. The user enters their email and password.
2. The application finds the account using the email.
3. The entered password is verified against the stored hashed password.
4. If the credentials are correct, the user is logged in.

The application also supports `user` and `admin` roles.

## Data Storage

The application uses JSON files for persistent storage.

### users.json

Stores user information such as:

* User ID
* Name
* Email
* Hashed password
* Role

### transactions.json

Stores financial transactions such as:

* Transaction ID
* User ID
* Transaction type
* Amount
* Category
* Description
* Date

## Object-Oriented Design

The project uses several classes to demonstrate OOP principles.

### Person

Base class containing common person information.

### User

Inherits from `Person` and represents an application user.

### Transaction

Base class for financial transactions.

### Income

Inherits from `Transaction` and represents money received by a user.

### Expense

Inherits from `Transaction` and represents money spent by a user.

The project demonstrates:

* Encapsulation through properties
* Inheritance through parent and child classes
* Polymorphism through customized `__str__()` methods

## Testing

The project uses `pytest` for automated testing.

Run all tests with:

```bash
pytest
```

The test suite covers:

* User creation
* User inheritance
* Transaction creation
* Income and expense classes
* Password hashing
* Registration
* Login
* Finance calculations
* Input validation
* Authentication decorators
* CLI functions

## Git Workflow

The project uses Git and GitHub for collaboration.

Team members work on separate branches instead of directly modifying the `main` branch.

The workflow is:

```text
Create branch
     ↓
Write code
     ↓
Run tests
     ↓
Commit changes
     ↓
Push branch
     ↓
Create Pull Request
     ↓
Code review
     ↓
Merge into main
```

## Team Roles

### Barack

**Scrum Master / CLI & Integration Lead**

Responsible for:

* CLI development
* Integrating team members' work
* Pull request reviews and merges
* Project coordination

### Emmanuel

**OOP Developer**

Responsible for:

* Classes
* Inheritance
* Encapsulation
* Transaction and user models

### Beatrice

**Authentication Developer**

Responsible for:

* Registration
* Login
* Password hashing
* User roles
* Authentication decorators

### JB

**Persistence & Testing Developer**

Responsible for:

* JSON storage
* Data persistence
* Automated testing
* Test coverage

## Future Improvements

Possible future improvements include:

* Expense categories and spending limits
* Monthly financial reports
* Exporting transactions to CSV
* A graphical user interface
* More advanced password security
* Database storage such as SQLite

## License

This project was created as a group academic project.
