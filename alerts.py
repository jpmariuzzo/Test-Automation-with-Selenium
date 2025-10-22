import selectors
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

## Indicating the proper Chrome Wed Driver, according to installed Chrome version
## Each navigator has its own driver
##  The WebDriver acts as a bridge, allowing your Selenium script to communicate with the browser
service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

##driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/") ## Goes to this specific webpage
driver.maximize_window() ## Will maximize the window
name = "Minestrone"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert ## switch_to.alert changes from browser mode to alert mode, to get the alerts in Java or Javascript
alertText = alert.text



print(alertText)
assert name in alertText
time.sleep(1)
alert.accept() ## Methods .accept() and .dismiss() allow you to accept or refuse the pop-up/alert

time.sleep(3)

