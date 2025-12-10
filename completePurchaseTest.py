import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")

##Configuring Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") ##Initializing the navigator maximized
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

selectedPhone = "Blackberry"
selectedCountry = "France"
successMessage = "Success! Thank you! Your order will be delivered in next few weeks :-)."

for phone in phones:
    if phone.find_element(By.XPATH, "div/h4/a").text == selectedPhone:
        phone.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("Fra")
countryLocator = (By.LINK_TEXT, selectedCountry)

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(countryLocator)).click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

assert successMessage in driver.find_element(By.CLASS_NAME, "alert-success").text

time.sleep(3)
driver.close()