#@author sreelakshmi
#Class Description:  Login functions to be used across all test cases
import time
from base.basepage import BasePage
import test_data.testData as tD
import utilities.Constants as constant


class HomePage(BasePage):
    def __init__(self, driver, report):
        super().__init__(driver)
        self.homePageLocator = self.pageLocators('homepage', 'HomePageLocator.json')
        self.customerManagerLocator = self.pageLocators('customerpage', 'CustomerPageLocators.json')
        self.driver = driver
        self.reports = report

    def loginIntoBankManager(self):
        self.reports.report(constant.TYPE_STEP, "Verify home page is loaded ")
        self.isElementPresent(*self.locator(self.homePageLocator, 'homeButton'))
        self.reports.report(constant.TYPE_STEP, "Login into bank manager")
        self.elementClick(*self.locator(self.homePageLocator, 'managerLogin'))
        currentUrl=self.getURL()
        self.verifyTextMatch("Assert that manager logged in successflly",currentUrl,tD.testData('manager_url'))

    def loginIntoCustomer(self):
        self.reports.report(constant.TYPE_STEP, "Verify home page is loaded ")
        self.isElementPresent(*self.locator(self.homePageLocator, 'homeButton'))
        self.reports.report(constant.TYPE_STEP, "Login into Cutomer Account")
        self.elementClick(*self.locator(self.homePageLocator, 'customerLogin'))
        currentUrl=self.getURL()
        self.verifyTextMatch("Assert that customer logged in successflly",currentUrl,tD.testData('customer_url'))
        self.reports.report(constant.TYPE_STEP, "Select your name ")
        self.dropdownSelectElement(*self.locator(self.customerManagerLocator,tD.testData('existing_user')))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click on login button")
        self.elementClick(*self.locator(self.customerManagerLocator, 'loginButton'))



