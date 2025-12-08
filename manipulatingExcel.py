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

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
file_path = r"C:\Users\jpmar\Downloads\download.xlsx"

#driver.find_element(By.ID, "downloadButton").click()



#Get and edit Excel

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']") #Type has to be FILE if you want to send a file
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 10)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)") # . to select a class
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text) #We use * to unpack the tuple

time.sleep(3)