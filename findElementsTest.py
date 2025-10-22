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

driver.get("https://rahulshettyacademy.com/dropdownsPractise/") ## Goes to this specific webpage
driver.maximize_window() ## Will maximize the window

driver.find_element(By.ID, "autosuggest").send_keys("uni")
time.sleep(2) #Waiting options to be displayed

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") ##Identifing all elements and creating a list

for country in countries:
    if country.text == "United Kingdom (UK)": ## text method gets texts already loaded on the screen
        #print(country.text)
        country.click()
        break

country_selected = driver.find_element(By.ID, "autosuggest").get_attribute("value") ## get-attribute method gets dinamic texts
print("Country selected: ", country_selected)

#assert "United Kingdom (UK)" in country_selected
assert country_selected == "United Kingdom (UK)"



