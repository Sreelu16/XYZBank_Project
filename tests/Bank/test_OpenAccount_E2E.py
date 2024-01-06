
from base.basepage import BasePage
from base.Reporter import Reporter
from utilities.pages.HomePage import HomePage
from utilities.pages.BankManagerPage import BankManagerPage
from utilities.pages.CustomerPage import CustomerPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time



@pytest.mark.usefixtures("oneTimeSetUpLauncher", "setUp")
class OpenCustomerAccount(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.reports = Reporter(self.driver, self.__class__.__name__)
        self.home = HomePage(self.driver, self.reports)
        self.manager= BankManagerPage(self.driver,self.reports)
        self.customer= CustomerPage(self.driver,self.reports)
    def test_open_account(self):
        try:
            self.home.loginIntoBankManager()
            self.manager.add_customer()
            account_number=self.manager.open_account()
            self.customer.customer_login()
            self.customer.customername_accountnumber_validation(account_number)
            self.customer.customer_deposit_amount()
            self.customer.customer_balance_validaton_after_deposit()
            self.customer.customer_logout()
            self.driver.quit()
        finally:
            self.reports.writeResult()

