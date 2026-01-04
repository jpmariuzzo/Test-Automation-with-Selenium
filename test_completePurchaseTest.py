import json
import time
import pytest


from pythonSelenium.pageObjects.ShopPage import ShopPage
from pythonSelenium.pageObjects.login import LoginPage
with open(r"C:\Users\jpmar\PyCharmProjects\pythonTesting\pythonSelenium\testCaseData\test_completePurchaseTest.json") as f:
    test_data = json.load(f)
    test_list = test_data["data"]
# with gerencia recursos. Abre e fecha files automaticamente

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list) #parametrize expects a list
#The fixture allows us to run test many times
def test_EndToEnd(browser_instance, test_list_item): #Only fixtures are allowed in test function argument
    print("test_completePurchaseTest execution.")

    #driver object will appear after fixture execution
    driver = browser_instance #Activating driver inside test code, browser_instance object is the driver here

    login_page = LoginPage(driver)
    print(login_page.get_title())

    shop_page = login_page.login(username=test_list_item["useremail"], password=test_list_item["userpassword"])
    shop_page.add_to_cart(selected_phone=test_list_item["productname"], selected_country=test_list_item["deliverylocation"])
    print(shop_page.get_title())

    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.delivery_address(country_name_initials=test_list_item["countryinitials"])
    checkout_confirmation.validate_order(success_message="Success! Thank you! Your order will be delivered in next few weeks :-).")

    #success_message = "Success! Thank you! Your order will be delivered in next few weeks :-)."
    #time.sleep(3)
    #driver.close()