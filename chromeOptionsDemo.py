import selectors
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\chromedriver-win64\chromedriver.exe")

##Configuring Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") ##Initializing the navigator maximized
chrome_options.add_argument("headless") ##Headless mode doesn't show the webpage
##chrome_options.add_argument("--disable-gpu") ##Disables GPU and improves testing performance
chrome_options.add_argument("--ignoring-certificate-errors")


driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
