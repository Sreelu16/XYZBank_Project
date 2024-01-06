
from base.basepage import BasePage
from base.Reporter import Reporter
from utilities.pages.HomePage import HomePage
from utilities.pages.BankManagerPage import BankManagerPage
from utilities.teststatus import TestStatus
import unittest
import pytest




@pytest.mark.usefixtures("oneTimeSetUpLauncher", "setUp")
class DeleteAccount(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.reports = Reporter(self.driver, self.__class__.__name__)
        self.home = HomePage(self.driver, self.reports)
        self.manager= BankManagerPage(self.driver,self.reports)

    def test_Delete_Customer(self):
        try:
            self.home.loginIntoBankManager()
            self.manager.delete_Customer()
            self.driver.quit()
        finally:
            self.reports.writeResult()

