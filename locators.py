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

driver.get("https://rahulshettyacademy.com/angularpractice/") ## Goes to this specific webpage
driver.maximize_window() ## Will maximize the window

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("rafael.caue.dacruz@mosman.com.br")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("mZzBGrCj1e")
driver.find_element(By.ID, "exampleCheck1").click()

#Static drop down
gender_select = driver.find_element(By.ID, "exampleFormControlSelect1")
selected = Select(gender_select)
selected.select_by_visible_text("Male")
#select_gender.select_by_index(1)

#XPath - //tagname[@attribute='value']
#CSS - tagname[attribute='value'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rafael Caue Gael da Cruz")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("10/05/2000")

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("(11) 99883-7472")
#driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message



#print(driver.title) ## Print the Page's title
#print(driver.current_url) ## Print the current URL





time.sleep(30)