from selenium.webdriver.common.by import By

from helpers.element import find_element


class AddressPage:
    CHECKOUT_BUTTON = (By.XPATH, '//button[@name="processAddress"]')
    ADDRESS_DELIVERY = [By.XPATH, '//ul[@id="address_delivery"]//li[contains(@class, "address_city")]']

    def __init__(self, browser):
        self.browser = browser

    def get_address(self):
        address_city = find_element(self.browser, self.ADDRESS_DELIVERY).text
        return address_city
