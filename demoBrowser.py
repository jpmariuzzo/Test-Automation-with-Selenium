import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

## Indicating the proper Chrome Wed Driver, according to installed Chrome version
## Each navigator has its own driver
##  The WebDriver acts as a bridge, allowing your Selenium script to communicate with the browser
service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

##driver = webdriver.Chrome()

driver.get("https://www.coursera.org/") ## Goes to this specific webpage

driver.maximize_window() ## Will maximize the window

print(driver.title) ## Print the Page's title
print(driver.current_url) ## Print the current URL





time.sleep(30)