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
driver.implicitly_wait(5) ## 5 seconds is the max timeout to wait an element to show up in the screen

##driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/") ## Goes to this specific webpage
driver.maximize_window() ## Will maximize the window

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)## Necessary sleep timer to build the list, to not return a empty list

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products))
assert len(products) > 0

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
## time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5)

promoInfo = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoInfo)
assert promoInfo == 'Code applied ..!'



time.sleep(3)