import pytest
from src.bank_account import BankAccount
from src.exceptions import WithdrawTimeRestrictionError, WithdrawWeekendError
from unittest.mock import patch
import os


@pytest.fixture
def account():
    yield BankAccount(
        balance=1000,
        log_file="transaction_log.txt",
        file_log_withdraw="withdraw_log.txt",
    )


def test_deposit(account):
    new_balance = account.deposit(500)

    assert new_balance == 1500


def test_deposit_with_negative_amount_not_increase(account):
    with pytest.raises(ValueError):
        account.deposit(-50)


@patch("src.bank_account.datetime")
def test_withdraw(mock_datetime, account):
    mock_datetime.now.return_value.hour = 10
    new_balance = account.withdraw(200)
    assert new_balance == 800


@patch("src.bank_account.datetime")
def test_withdraw_with_negative_amount_not_decrease(mock_datetime, account):
    mock_datetime.now.return_value.hour = 10
    assert account.withdraw(-10) == 1000


@patch("src.bank_account.datetime")
def test_withdraw_in_available_hours(mock_datetime, account):
    mock_datetime.now.return_value.hour = 10
    assert account.withdraw(10) == 990


@patch("src.bank_account.datetime")
def test_withdraw_not_in_available_days(mock_datetime, account):
    mock_datetime.now.return_value.hour = 10
    mock_datetime.now.return_value.weekday.return_value = 6
    with pytest.raises(WithdrawWeekendError):
        account.withdraw(10)


def teardown_module(module):
    if os.path.exists("transaction_log.txt"):
        os.remove("transaction_log.txt")

    if os.path.exists("withdraw_log.txt"):
        os.remove("withdraw_log.txt")
