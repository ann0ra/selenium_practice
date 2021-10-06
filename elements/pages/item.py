from selenium.webdriver.common.by import By

from elements.modals.item import ItemModal
from helpers.element import find_element


class ItemPage:
    QUANTITY = (By.XPATH, '//input[@id="quantity_wanted"]')
    MINUS_BUTTON = (By.XPATH, '//a[contains(@class, "button-minus")]')
    PLUS_BUTTON = (By.XPATH, '//a[contains(@class, "button-plus")]')
    PRICE = (By.XPATH, '//span[@id="our_price_display"]')
    SIZE = (By.XPATH, '//select[@id="group_1"]')
    M_SIZE = (By.XPATH, '//option[@title="M"]')
    COLOR = (By.XPATH, '//a[@id="color_14"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@name="Submit"]')
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, '//a[@id="wishlist_button"]')

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self):
        cart = find_element(self.browser, self.ADD_TO_CART_BUTTON)
        cart.click()

        return ItemModal(self.browser)

    def add_quantity(self):
        plus_button = find_element(self.browser, self.PLUS_BUTTON)
        plus_button.click()

        return self

    def less_quantity(self):
        plus_button = find_element(self.browser, self.MINUS_BUTTON)
        plus_button.click()

        return self

    def get_quantity(self):
        quantity = find_element(self.browser, self.QUANTITY)

        return quantity.get_attribute('value')

    def choose_color(self):
        find_element(self.browser, self.COLOR).click()

        return self

    def choose_size(self):
        find_element(self.browser, self.M_SIZE).click()

        return self
