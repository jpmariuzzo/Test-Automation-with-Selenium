import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)

driver.switch_to.frame("courses-iframe") ## iFrame ID
driver.find_element(By.CSS_SELECTOR, "div[class='nav-outer clearfix'] a[class='dropdown-toggle']").click()
#action.move_to_element(driver.find_element(By.CSS_SELECTOR, "div[class='nav-outer clearfix'] a[class='dropdown-toggle']")).perform()
#time.sleep(1)
#action.move_to_element(driver.find_element(By.XPATH, "(//a[@href='contact-us'][normalize-space()='Contact'])[1]")).click().perform()

driver.find_element(By.XPATH, "(//a[@href='contact-us'][normalize-space()='Contact'])[1]").click()



##driver.switch_to.default_content()
##print(driver.find_element(By.CSS_SELECTOR, "h3").text)

time.sleep(10)
