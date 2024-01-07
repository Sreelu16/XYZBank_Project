
# # @author SreeLakshmi
# # Class Description: WebDriver Factory class implementation, It creates a web-driver instance based on browser configurations.
from selenium import webdriver
import os
import test_data.testData as td
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


class WebDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        self.browser = td.testData("browser")
        self.baseUrl = td.testData("environment")
        # self.baseUrl1 = td.testData("environment1")

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return 'WebDriver Instance':
        """

        if self.browser == "Firefox":
            driver = webdriver.Firefox()

        elif self.browser == "Chrome":

            driver = webdriver.Chrome(ChromeDriverManager().install())  # WebDriverManager handles download and setup
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument("ignore-certificate-errors")

        elif self.browser == "Edge":
            # Set Edge driver
            driverLocation = "../../drivers/Edge/MicrosoftWebDriver.exe"
            driver = webdriver.Edge(driverLocation)

        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver
    def gotoUrl(self, driver):
        driver.get(self.baseUrl)
