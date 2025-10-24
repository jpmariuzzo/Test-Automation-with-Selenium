import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpened = driver.window_handles # Creates a list of opened windows
driver.switch_to.window(windowsOpened[1]) ## Switches to the new window, [0] to [1]
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text
driver.close()
driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

time.sleep(3)