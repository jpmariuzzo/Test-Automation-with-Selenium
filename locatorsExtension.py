import selectors
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service(r"/pythonSelenium/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("mZzBGrCj1e")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("mZzBGrCj1e")

## driver.find_element(By.XPATH, "//button[@type='submit']").click()                ## Find by XPATH
## driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()    ## Find by text
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()         ## Find by css Selector



time.sleep(30)