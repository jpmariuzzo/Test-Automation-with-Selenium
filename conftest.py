import re

import pytest
import os
from datetime import datetime
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browser_instance(request): #request is a default fixture
    global driver
    browser_name = request.config.getoption("browser_name") ##--browser_name is a configuration option from the request
    print("Configuring browser instance...")
    print("Defining service object...")

        #r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")

    if browser_name =="chrome":
        service_obj = ChromeService()
        print("Defining chrome options...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  ##Initializing the navigator maximized
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)



    elif browser_name == "firefox":
        service_obj = FirefoxService()
        print("Defining Firefox options...")
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()

    print("Defining implicitly wait time...")
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver #Executed after fixture execution
    driver.close() ##Line will be executed after main test code executed


#def capture_screenshot(file_name):
#    safe_name = make_safe_filename(report.nodeid)
#    file_path = os.path.join(reports_dir, safe_name)
#    driver.get_screenshot_as_file(file_name)

def capture_screenshot(driver, file_path):
    print("Saving screenshot to:", file_path)
    success = driver.get_screenshot_as_file(file_path)
    print("Screenshot success:", success)

def make_safe_filename(nodeid):
    return re.sub(r'[\\/*?:"<>|[\]]', "_", nodeid) + ".png"


#@pytest.hookimpl(hookwrapper=True)
#def pytest_runtest_makereport(item):
    #Extends the Pytest plugin to take and embed screenshot in html report, whenever


#    pytest_html = item.config.pluginmanager.getplugin("html")
#    outcome = yield
#    report = outcome.get_result()
#    extra = getattr(report, "extra", [])


#    if report.when == "call" or report.when == "setup":
#        xfail = hasattr(report, "wasxfail")

#        if (report.skipped and xfail) or (report.failed and not xfail):
#            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
#            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")

#            safe_name = make_safe_filename(report.nodeid)
#            file_path = os.path.join(reports_dir, safe_name)

#            print("file name is "+file_name)
#            capture_screenshot(file_name)

#            if file_name:
#                html =(
#                    '<div>'
#                    '<img src="%s" '
#                    'alt="screenshot" '
#                    'style="width:304px;height:228px;" '
#                    'onclick="window.open(this.src)" '
#                    'align="right"/>'
#                    '</div>') % file_name

#                extra.append(pytest_html.extras.html(html))
#        report.extra = extra


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("setup", "call") and (report.failed or report.skipped):
        driver = item.funcargs.get("browser_instance")
        if driver:
            # Criar pasta reports se não existir
            reports_dir = os.path.join(os.getcwd(), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            # Nome seguro
            safe_name = make_safe_filename(report.nodeid)
            file_path = os.path.join(reports_dir, safe_name)

            # Captura screenshot
            capture_screenshot(driver, file_path)

            # Embed no HTML
            html = f"""
            <div>
                <img src="{safe_name}"
                     alt="screenshot"
                     style="width:300px;height:200px;"
                     onclick="window.open('{safe_name}')"/>
            </div>
            """
            extra.append(pytest_html.extras.html(html))

    report.extra = extra
