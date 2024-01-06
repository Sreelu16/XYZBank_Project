#@author Sreelakshmi
#Class Description: basepage class to define generic methods to be used across all classes


from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import utilities.read_json as RJ
import os
import time
from dotenv import load_dotenv
from base.Reporter import Reporter
import utilities.Constants as constant


load_dotenv()


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()


    def pageLocators(self, page,fileName):
        """
        read the locators of specific page
        :param page: page
        :return: list of all locators in specific page
        """
        if os.getenv('local'):
            locatorFile = "../../locators/" + fileName
            locatorsPath = os.path.abspath(locatorFile)
            locatorsJsonFile = RJ.readJson(locatorsPath)
        else:
            locatorFile = "/locators/" + fileName
            locatorsJsonFile = RJ.readJson(locatorFile)
        pageLocators = [locator for locator in locatorsJsonFile if locator['pageName'] in page]
        return pageLocators

    def locator(self, pageLocators, locatorName):
        """
        get specific locator in specific page
        :param pageLocators: specific page
        :param locatorName: locator name
        :return: locator and locator Type
        """
        result =None
        for locator in pageLocators:
            if locatorName == locator['name']:
                result= locator['locator'], locator['locateUsing'], locatorName
        if result==None:
            Reporter.report(self.reports, "Locator name", 'Search locator name in Json :' + str(locatorName),
                            'Failed to find the locator in Json file: ' + str(locatorName), constant.TYPE_FAIL)
        else:
            return result

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return  self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False


