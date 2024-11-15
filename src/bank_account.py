from datetime import datetime
from src.exceptions import (
    InsufficientFoudsError,
    WithdrawTimeRestrictionError,
    WithdrawWeekendError,
)


class BankAccount:
    def __init__(self, balance=0, log_file=None, file_log_withdraw=None) -> None:
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")
        self.log_file_withdraw = file_log_withdraw

    def grabar_log(self, fileName, message):
        if fileName:
            with open(fileName, "a") as f:
                f.write(f"{message}\n")

    def _log_transaction(self, message):
        self.grabar_log(self.log_file, message)

    def _log_transaction_fail(self, message):
        self.grabar_log(self.log_file_withdraw, message)

    def deposit(self, amount):
        """Deposit method

        Args:
            amount (number): Amount that we will deposit

        Returns:
            number: New balance after deposit
        >>> account = BankAccount(100)
        >>> account.deposit(50)
        150
        """

        if amount < 0:
            raise ValueError("Can't deposit negative amounts")

        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}- New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawTimeRestrictionError(
                "Withdrawals are only allowed between 8:00 and 17:00"
            )

        if now.weekday() in [5, 6]:
            raise WithdrawWeekendError("Withdrawals not allowed in weekends")

        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self._log_transaction(f"Withdraw {amount}- New balance: {self.balance}")
            else:
                self._log_transaction_fail(
                    f"Saldo Insuficiente {amount} : {self.balance}"
                )

        return self.balance

    def get_balance(self):
        self._log_transaction(f"Balance cheched {self.balance}")
        return self.balance
