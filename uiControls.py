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

#driver.find_element(By.ID, "checkBoxOption2").click()
#driver.find_element((By.XPATH, "(//input[@type='checkbox'])[2]")) ##By mapping XPATHS
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") ## In case of dynamic options positions
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(1)

buttons = driver.find_elements(By.NAME,"radioButton")
buttons[2].click()
assert buttons[2].is_selected()

#for button in buttons:
 #   if button.get_attribute("value") == "radio3":
  #      button.click()
   #     assert button.is_selected()
    #    break

time.sleep(1)

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

## Methods is_displayed and is_selected are very useful to make assertions

time.sleep(3)

