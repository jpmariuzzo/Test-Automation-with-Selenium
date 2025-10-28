import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj) ##Some arguments can be added here.
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "option[value='20']").click()
driver.find_element(By.XPATH, "//span[@class='sort-icon sort-descending']").click()

browserListCollected = driver.find_elements(By.XPATH, "//tr/td[1]")
sortedList = []
browserList = []
for element in browserListCollected:
    sortedList.append(element.text)

browserList = sortedList.copy() ## Creates a copy of a list
sortedList.sort()
print(sortedList)
assert sortedList == browserList

time.sleep(3)