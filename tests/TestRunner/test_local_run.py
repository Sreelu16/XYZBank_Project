import unittest
from tests.Bank.test_OpenAccount_E2E import OpenCustomerAccount
from tests.Bank.test_Amount_Transaction import AmountTransactions
from tests.Bank.test_DeleteAccount import DeleteAccount
tc001 = unittest.TestLoader().loadTestsFromTestCase(OpenCustomerAccount)
tc002 = unittest.TestLoader().loadTestsFromTestCase(AmountTransactions)
tc003 = unittest.TestLoader().loadTestsFromTestCase(DeleteAccount)

smokeTest = unittest.TestSuite([tc001,tc002,tc003])
unittest.TextTestRunner(verbosity=2).run(smokeTest)














































