from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.ShopPage import ShopPage
from pythonSelenium.utilities.BrowserUtilities import BrowserUtilities


#username: rahulshettyacademy
#password: learning

class LoginPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)

        # Defining locators
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.login_btn = (By.ID, "signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click() ## Adding * tuple is broken in parameters

        shop_page = ShopPage(self.driver)
        return shop_page

