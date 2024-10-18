import unittest
from test_bank_account import BankAccoutTest

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccoutTest("test_deposit"))
    suite.addTest(BankAccoutTest("test_withdraw"))
    
    return suite
    
if __name__ == '__main__':
    
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())