#Page Objects should only have action methods and locators!!

from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.Checkout_Confirmation import Checkout_Confirmation
from pythonSelenium.utilities.BrowserUtilities import BrowserUtilities


class ShopPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_page = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_list = (By.XPATH, "//div[@class='card h-100']")

        self.checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_to_cart(self, selected_phone, selected_country):
        # driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
        self.driver.find_element(*self.shop_page).click()
        self.selected_country = selected_country
        self.selected_phone = selected_phone
        print("Selected phone: ", self.selected_phone)
        print("Selected country: ", self.selected_country)

        phones = self.driver.find_elements(*self.product_list)

        for phone in phones:
            if phone.find_element(By.XPATH, "div/h4/a").text == self.selected_phone:
                phone.find_element(By.XPATH, "div/button").click()


    def go_to_cart(self):
        self.driver.find_element(*self.checkout_btn).click()
        checkout_confirmation = Checkout_Confirmation(self.driver, deliverylocation=self.selected_country)
        return checkout_confirmation
