import unittest, os
from unittest.mock import patch
from src.bank_account import BankAccount
from src.exceptions import WithdrawTimeRestrictionError, WithdrawWeekendError


class BankAccoutTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(
            balance=1000,
            log_file="transaction_log.txt",
            file_log_withdraw="withdraw_log.txt",
        )

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

        if os.path.exists(self.account.log_file_withdraw):
            os.remove(self.account.log_file_withdraw)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)

        self.assertEqual(new_balance, 1500)

    def test_deposit_with_negative_amount_not_increase(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.account.deposit(-50))

    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    @patch("src.bank_account.datetime")
    def test_withdraw_with_negative_amount_not_decrease(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.assertEqual(self.account.withdraw(-10), 1000)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    @patch("src.bank_account.datetime")
    def test_withdraw_without_saldo(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.account.withdraw(1500)
        self.assertTrue(os.path.exists("withdraw_log.txt"))
        self.assertEqual(self._count_lines(self.account.log_file_withdraw), 1)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 3
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        mock_datetime.now.return_value.weekday.return_value = 3
        with self.assertRaises(WithdrawTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_weekends(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 6
        with self.assertRaises(WithdrawWeekendError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_allow_in_week(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 3
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 900)

    # Subtest
    def test_deposit_multiple_amounts(self):
        tests_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]

        for case in tests_cases:
            with self.subTest(case=case):
                self.account = BankAccount(
                    balance=1000,
                    log_file="transaction_log.txt",
                    file_log_withdraw="withdraw_log.txt",
                )
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
