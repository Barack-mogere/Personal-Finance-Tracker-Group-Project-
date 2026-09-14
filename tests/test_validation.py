from utils.validation import (
    get_positive_amount,
    get_non_empty_input,
    get_valid_date
)
from unittest.mock import patch


def test_get_positive_amount():
    with patch(
        "builtins.input",
        return_value="500"
    ):
        result = get_positive_amount("Enter amount: ")

    assert result == 500


def test_get_positive_amount_rejects_invalid_input():
    with patch(
        "builtins.input",
        side_effect=["abc", "500"]
    ):
        result = get_positive_amount("Enter amount: ")

    assert result == 500


def test_get_positive_amount_rejects_negative_number():
    with patch(
        "builtins.input",
        side_effect=["-100", "500"]
    ):
        result = get_positive_amount("Enter amount: ")

    assert result == 500


def test_get_non_empty_input():
    with patch(
        "builtins.input",
        return_value="Food"
    ):
        result = get_non_empty_input("Enter category: ")

    assert result == "Food"


def test_get_non_empty_input_rejects_empty_input():
    with patch(
        "builtins.input",
        side_effect=["", "Food"]
    ):
        result = get_non_empty_input("Enter category: ")

    assert result == "Food"


def test_get_valid_date():
    with patch(
        "builtins.input",
        return_value="2026-09-14"
    ):
        result = get_valid_date("Enter date: ")

    assert result == "2026-09-14"


def test_get_valid_date_rejects_invalid_date():
    with patch(
        "builtins.input",
        side_effect=["14/09/2026", "2026-09-14"]
    ):
        result = get_valid_date("Enter date: ")

    assert result == "2026-09-14"