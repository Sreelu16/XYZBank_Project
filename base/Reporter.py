#@author Sreelakshmi
#Class Description: Reporter class to generate reports in all the test cases
import os
from shutil import copyfile
import datetime
import time
import test_data.testData as td


class Reporter:
    def __init__(self, driver, name):
        self.driver = driver
        self.screenShotStatus = td.testData('screenshot')
        self.passedLogs = []
        self.failedLogs = []
        self.name = name
        self.starttime = datetime.datetime.now().replace(microsecond=0)
        self.passtablerow = ''
        self.failresultrow = ''
        if os.getenv('local'):
            srchtmlTemplate = os.path.abspath("./../../report.html")
            self.desthtmlTemplate = os.path.abspath("./../../reports/" + name + ".html")
        else:
            srchtmlTemplate = os.getcwd() + os.path.abspath("./../../report.html")
            self.desthtmlTemplate = os.getcwd() + os.path.abspath("./../../reports/" + name + ".html")
        copyfile(srchtmlTemplate, self.desthtmlTemplate)
        with open(self.desthtmlTemplate, 'rt') as f:
            self.f = f.readlines()

    def screenShot(self):
        """
        Take a screenshot of the current open web page
        """
        fileName = self.name + "." + str(round(time.time() *1000)) + ".png"
        if len(fileName) >= 200:
            fileName = str(round(time.time() *1000)) + ".png"

        screenshotDirectory = "../screenshots/"
        screenshotDirectory = screenshotDirectory.lstrip("../")

        relativeFileName = os.path.join(screenshotDirectory, fileName)
        currentDirectory = os.path.dirname(__file__).replace("base","")
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        # relativeFileName = screenshotDirectory + fileName
        # currentDirectory = os.path.dirname(__file__)
        # destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            return str(destinationDirectory) + str(fileName)
        except:
            print("### Exception Occurred when taking screenshot")

    def report(self, typeoflog, message='', result='', Result='PASS'):
        snapshot = self.screenShot() if Result == 'FAIL' else ''
        result = {
            'typeoflog': typeoflog,
            'message': message,
            'result': result,
            'snapshot': snapshot
        }
        if Result == 'PASS':
            self.passedLogs.append(result)
        else:
            self.failedLogs.append(result)

    def writeResult(self):
        for index, passresult in enumerate(self.passedLogs):
            self.passtablerow = self.passtablerow + '<tr><td width="5%" style="padding: 5px;">' + str(
                index + 1) + '</td>'
            self.passtablerow = self.passtablerow + '<td style="padding: 5px;" width="7%">' + passresult[
                "typeoflog"] + '</td>'
            self.passtablerow = self.passtablerow + '<td width="40%" style="word-wrap: break-all;padding: 5px;">' + \
                                passresult["message"] + '</td>'
            self.passtablerow = self.passtablerow + '<td style="padding: 5px;" width = "40%">' + passresult[
                "result"] + '</td>'
            self.passtablerow = self.passtablerow + '<td style="padding: 5px;" width = "8%">' + passresult[
                "snapshot"] + '</td></tr>'

        for index, failedResult in enumerate(self.failedLogs):
            self.failresultrow = self.failresultrow + '<tr style="background: #efef9d;"><td width="5%" style="padding: 5px;">' + str(
                index + 1) + '</td>'
            self.failresultrow = self.failresultrow + '<td width="7%" style="padding: 5px;">' + failedResult[
                "typeoflog"] + '</td>'
            self.failresultrow = self.failresultrow + '<td width="40%" style="word-wrap: break-all;padding: 5px;">' + \
                                 failedResult["message"] + '</td>'
            self.failresultrow = self.failresultrow + '<td width = "40%" style="padding: 5px;">' + failedResult[
                "result"] + '</td>'
            if self.screenShotStatus:
                self.failresultrow = self.failresultrow + '<td width = "8%" style="padding: 5px;">' + '<a target="_blank" href="' + \
                                     failedResult["snapshot"] + ' ">Click Here<a/></td></tr>'
            else:
                self.failresultrow = self.failresultrow + '<td style="padding: 5px;" width = "8%">' + '</td></tr>'
        timeTaken = str(datetime.datetime.now().replace(microsecond=0) - self.starttime)
        f1 = open(self.desthtmlTemplate, "w")
        for line in self.f:
            # read replace the string and write to output file
            if '<!-- INSERT_RESULTS -->' in line:
                f1.write(line.replace('<!-- INSERT_RESULTS -->', self.passtablerow))
            elif '<!-- INSERT_FAILED_RESULTS -->' in line:
                f1.write(line.replace('<!-- INSERT_FAILED_RESULTS -->', self.failresultrow))

            elif '#timetaken' in line:
                f1.write(line.replace('#timetaken', timeTaken))
            elif '#testcasename' in line:
                f1.write(line.replace('#testcasename', self.name))
            elif '#browser' in line:
                f1.write(line.replace('#browser', str(td.testData("browser"))))
            else:
                f1.write(line)
        f1.close()
