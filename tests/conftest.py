import stat

import pytest
import os
from shutil import copyfile
from base.webdriverfactory import WebDriverFactory

srchtmlTemplate = ''
desthtmlTemplate = ''

if os.getenv('local'):
    srchtmlTemplate = os.path.abspath("./../../emailreport.html")
    desthtmlTemplate = os.path.abspath("./../../reports/emailable.html")
else:
    srchtmlTemplate = os.getcwd() + os.path.abspath("./../../emailreport.html")
    desthtmlTemplate = os.getcwd() + os.path.abspath("./../../reports/emailable.html")
print("*****email test******")
copyfile(srchtmlTemplate, desthtmlTemplate)
with open(desthtmlTemplate, 'rt') as f:
    f = f.readlines()


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


def pytest_sessionstart(session):
    session.html = ''
    session.results = dict()


@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    print("Running class setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print("Test has been successfully executed")


@pytest.fixture(scope="class")
def oneTimeSetUpLauncher(request):
    print("Running class setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print("Test has been successfully executed")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    row = ''
    for result in session.results.values():
        res = ''
        if result.passed:
            res = "Passed"
        else:
            res = "Failed"

        headline = result.head_line.split(".")[0] if result.head_line else ""
        location = result.location[0].split("\\")[1] if result.location else ""
        location_data = result.location[0] if result.location else ""
        link = '<a href="' + headline + '.html">Link Text</a>'
        if res == "Passed":
            row = row + ('<tr> <td>' + str(headline) + '</td><td>' + str(location) + "</td><td>" + res + "</td><td>" + link + "</td></tr>")
        else:
            row = row + ('<tr style="background: red;color: #fff;"> <td>' + str(headline) + '</td><td>' + str(
                location) + "</td><td>" + res + "</td> <td>" + link + "</td></tr>")

    f1 = open(desthtmlTemplate, "w")
    for line in f:
        # read replace the string and write to output file
        if '[TEST_CASE_DATA]' in line:
            f1.write(line.replace('[TEST_CASE_DATA]', row))
        else:
            f1.write(line)

    f1.close()
