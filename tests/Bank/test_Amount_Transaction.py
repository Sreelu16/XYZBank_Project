
from base.basepage import BasePage
from base.Reporter import Reporter
from utilities.pages.HomePage import HomePage
from utilities.teststatus import TestStatus
from utilities.pages.CustomerPage import CustomerPage
import unittest
import pytest
import time



@pytest.mark.usefixtures("oneTimeSetUpLauncher", "setUp")
class AmountTransactions(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.reports = Reporter(self.driver, self.__class__.__name__)
        self.home = HomePage(self.driver, self.reports)
        self.cust= CustomerPage(self.driver, self.reports)

    def test_amount_transaction(self):
        try:
            self.home.loginIntoCustomer()
            self.cust.customer_deposit_amount()
            bal_amnt_before_withdrawl=self.cust.customer_withdrawl()
            self.cust.customer_withdraw_amount_validaton_after_withdrawl(bal_amnt_before_withdrawl)
            self.cust.customer_logout()
        finally:
            self.reports.writeResult()

