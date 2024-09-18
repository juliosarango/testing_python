import unittest
import os
from src.bank_account import BankAccount


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

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_withdraw_without_saldo(self):
        self.account.withdraw(1500)
        self.assertTrue(os.path.exists("withdraw_log.txt"))
        self.assertEqual(self._count_lines(self.account.log_file_withdraw), 1)
