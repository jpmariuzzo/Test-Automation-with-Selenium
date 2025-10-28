import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chosing the way your going to run your Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") ##Headless mode doesn't show the webpage
chrome_options.add_argument("--ignore-certificate-errors") ##The Chrome will ignore all certifications errors, like those from SSL


service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options) ##Some arguments can be added here.
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Scrolling page on JavaScript
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")

time.sleep(5)