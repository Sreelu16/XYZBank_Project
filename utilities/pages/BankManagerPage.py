#@author sreelakshmi
#Class Description: functions to be used for all the manager activities like open account ,delete account
import time
from base.basepage import BasePage
import test_data.testData as tD
import utilities.Constants as constant


class BankManagerPage(BasePage):
    def __init__(self, driver, report):
        super().__init__(driver)
        self.bankManagerLocator = self.pageLocators('managerpage', 'ManagerPageLocators.json')
        self.driver = driver
        self.reports = report

    def add_customer(self):
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click Add Customer menu")
        self.elementClick(*self.locator(self.bankManagerLocator, 'addCutomerTab'))
        self.reports.report(constant.TYPE_STEP, "Enter First name on Add customer page")
        self.enterInTextBox(tD.testData('firstName'), *self.locator(self.bankManagerLocator, 'firstName'))
        self.reports.report(constant.TYPE_STEP, "Enter Last name on Add customer page")
        self.enterInTextBox(tD.testData('lastName'), *self.locator(self.bankManagerLocator, 'lastName'))
        self.reports.report(constant.TYPE_STEP, "Enter Post code on Add customer page")
        self.enterInTextBox(tD.testData('postCode'), *self.locator(self.bankManagerLocator, 'postCode'))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Submit Customer details")
        self.elementClick(*self.locator(self.bankManagerLocator, 'submit'))
        message=self.acceptAlertAndRetunText()
        self.verifyParticialTextMatch("Assert customer added successfully","Customer added successfully with customer id",message)

    def open_account(self):
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click open account menu")
        self.elementClick(*self.locator(self.bankManagerLocator, 'openAccountTab'))
        self.reports.report(constant.TYPE_STEP, "Select customer : Demo user ")
        self.dropdownSelectElement(*self.locator(self.bankManagerLocator, 'Demo user'))
        self.reports.report(constant.TYPE_STEP, "Select currency : Doller")
        self.dropdownSelectElement(*self.locator(self.bankManagerLocator, tD.testData('currency')))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Submit open account details")
        self.elementClick(*self.locator(self.bankManagerLocator, 'submit'))
        message = self.acceptAlertAndRetunText()
        self.verifyParticialTextMatch("Assert Open Account successfully","Account created successfully with account Number", message)
        return message.split(":")[1]
    def delete_Customer(self):
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click Customer menu")
        self.elementClick(*self.locator(self.bankManagerLocator, 'customerTab'))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Delete Customer")
        self.elementClick(*self.locator(self.bankManagerLocator, 'deleteCustomer'))
        self.VerifyElementisNotPresent(*self.locator(self.bankManagerLocator, 'deleteCustomer'))
