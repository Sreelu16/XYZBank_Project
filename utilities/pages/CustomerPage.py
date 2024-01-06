#@author sreelakshmi
#Class Description: functions to be used for verify the customer created
import time
from base.basepage import BasePage
import test_data.testData as tD
import utilities.Constants as constant


class CustomerPage(BasePage):
    def __init__(self, driver, report):
        super().__init__(driver)
        self.customerManagerLocator = self.pageLocators('customerpage', 'CustomerPageLocators.json')
        self.homePageLocator = self.pageLocators('homepage', 'HomePageLocator.json')
        self.driver = driver
        self.reports = report

    def customer_login(self):
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click on Home button")
        self.elementClick(*self.locator(self.homePageLocator, 'homeButton'))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on customer login")
        self.elementClick(*self.locator(self.customerManagerLocator, 'customerLogin'))
        # select the username from the drop down
        self.reports.report(constant.TYPE_STEP, "Select your name ")
        #getting the username from test data
        username=tD.testData('firstName')+" "+tD.testData('lastName')
        self.dropdownSelectElement(*self.locator(self.customerManagerLocator,username))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "Click on login button")
        self.elementClick(*self.locator(self.customerManagerLocator, 'loginButton'))

    def customername_accountnumber_validation(self,account_number):
        #verify the username
        username_logged_in =self.getText(*self.locator(self.customerManagerLocator,'userNameLoggedIn'))
        self.verifyTextMatch("verify the same username displayed after logging in",tD.testData('firstName')+" "+tD.testData('lastName'),username_logged_in)
        #verify the account number
        actual_account_number=self.getText(*self.locator(self.customerManagerLocator,'accountNumberValue'))
        self.verifyTextMatch("verify the same account number is displayed after logging in", account_number,
                             actual_account_number)

    def customer_deposit_amount(self):
        #performing deposit amount
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on deposit tab")
        self.elementClick(*self.locator(self.customerManagerLocator, 'depositTab'))
        self.reports.report(constant.TYPE_STEP, "Enter amount to be deposited after customer login")
        self.enterInTextBox(tD.testData('depositAmount'), *self.locator(self.customerManagerLocator,'depositAmountField'))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on deposit button")
        self.elementClick(*self.locator(self.customerManagerLocator,'depositButton'))
        #verify the successful message
        success_msg=self.getText(*self.locator(self.customerManagerLocator,'depositSuccessMessage'))
        self.verifyTextMatch("checking the successful message after deposit","Deposit Successful",success_msg)

    def customer_balance_validaton_after_deposit(self):
        # verify balance amount after depost
        bal_amnt = self.getText(*self.locator(self.customerManagerLocator, 'balanceValue'))
        self.verifyTextMatch("checking the balance amount after deposit", tD.testData('depositAmount'), bal_amnt)
        # verify currency
        currency_val = self.getText(*self.locator(self.customerManagerLocator, 'currencyValue'))
        self.verifyTextMatch("checking the successful message after deposit", tD.testData('currency'), currency_val)

    def customer_logout(self):
        #perform logout action
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on logout button")
        self.elementClick(*self.locator(self.customerManagerLocator, 'logoutButton'))

    def customer_withdrawl(self):
        #click on withdrawl tab
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on withdrawl tab")
        self.elementClick(*self.locator(self.customerManagerLocator, 'withdrawlTab'))
        #customer balance amount before withdrawl
        bal_amnt_before_withdrawl = self.getText(*self.locator(self.customerManagerLocator, 'balanceValue'))
        #enter amount to be withdrawn
        self.reports.report(constant.TYPE_STEP, "Enter amount to be withdrawn after customer login")
        self.enterInTextBox(tD.testData('withdrawlAmount'),*self.locator(self.customerManagerLocator, 'withdrawlAmountField'))
        self.reports.report(constant.TYPE_CLICK_ELEMENT, "click on withdrawl button")
        self.elementClick(*self.locator(self.customerManagerLocator, 'withdrawButton'))
        # verify the successful message
        success_msg = self.getText(*self.locator(self.customerManagerLocator, 'withdrawSuccessMessage'))
        self.verifyTextMatch("checking the successful message after deposit", "Transaction successful", success_msg)
        return bal_amnt_before_withdrawl
    def customer_withdraw_amount_validaton_after_withdrawl(self,bal_amnt_before_withdrawl):
        # verify balance amount after depost
        bal_amnt = self.getText(*self.locator(self.customerManagerLocator, 'balanceValue'))
        self.verifyTextMatch("checking the balance amount after deposit", str(int(bal_amnt_before_withdrawl)-int(tD.testData('withdrawlAmount'))), bal_amnt)




