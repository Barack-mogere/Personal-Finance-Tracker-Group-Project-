from utils.decorators import login_required, admin_required
from models.user import User


def test_login_required_allows_logged_in_user(capsys):

    @login_required
    def protected_function(user):
        return "Access granted"

    user = User(
        "Barack",
        "barack@example.com",
        "password",
        "user",
        1
    )

    result = protected_function(user)

    assert result == "Access granted"


def test_login_required_blocks_logged_out_user(capsys):

    @login_required
    def protected_function(user):
        return "Access granted"

    result = protected_function(None)

    captured = capsys.readouterr()

    assert result is None
    assert "Please log in first." in captured.out


def test_admin_required_allows_admin():

    @admin_required
    def admin_function(user):
        return "Admin access granted"

    admin = User(
        "Barack",
        "barack@example.com",
        "password",
        "admin",
        1
    )

    result = admin_function(admin)

    assert result == "Admin access granted"


def test_admin_required_blocks_regular_user(capsys):

    @admin_required
    def admin_function(user):
        return "Admin access granted"

    user = User(
        "Barack",
        "barack@example.com",
        "password",
        "user",
        1
    )

    result = admin_function(user)

    captured = capsys.readouterr()

    assert result is None
    assert "Admin access required." in captured.out


def test_admin_required_blocks_logged_out_user(capsys):

    @admin_required
    def admin_function(user):
        return "Admin access granted"

    result = admin_function(None)

    captured = capsys.readouterr()

    assert result is None
    assert "Please log in first." in captured.out