# We associate all methods to the mentioned web page

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pythonSelenium.utilities.BrowserUtilities import BrowserUtilities


class Checkout_Confirmation(BrowserUtilities):
    def __init__(self, driver, deliverylocation):
        super().__init__(driver)
        self.driver = driver
        self.success_btn = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.delivery_location = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, deliverylocation)
        self.checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.purchase_btn = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")


    def checkout(self):
        self.driver.find_element(*self.success_btn).click()



    def delivery_address(self, country_name_initials):
        self.driver.find_element(*self.delivery_location).send_keys(country_name_initials)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option)).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_btn).click()

    def validate_order(self, success_message):
        assert success_message in self.driver.find_element(*self.success_message).text

