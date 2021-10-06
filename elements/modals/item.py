from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from elements.pages.cart import CartPage
from helpers.element import find_element


class ItemModal:
    CROSS_BUTTON = (By.XPATH, '//span[@class="cross"]')
    PROCEED_TO_CHECKOUT = (By.XPATH, '//a[@title="Proceed to checkout"]')
    CONTINUE_SHOPPING = (By.XPATH, '//span[@title="Continue shopping"]')
    POP_WINDOW = (By.XPATH, '//div[@id="layer_cart"]')

    PRODUCT_COLOR_SIZE = (By.XPATH, '//span[@id="layer_cart_product_attributes"]')

    def __init__(self, browser):
        self.browser = browser

    def get_checkout(self):
        checkout_button = find_element(self.browser, self.PROCEED_TO_CHECKOUT)
        checkout_button.click()

        return CartPage(self.browser)

    def is_item_modal_present(self):
        try:
            window = find_element(self.browser, self.POP_WINDOW)
            return window.is_displayed()
        except NoSuchElementException:
            return False

    def get_product_color(self):
        color = find_element(self.browser, self.PRODUCT_COLOR_SIZE).text.split(',')[0]

        return color

    def get_product_size(self):
        size = find_element(self.browser, self.PRODUCT_COLOR_SIZE).text.split(',')[1]
        size = size.replace(' ', '')
        return size
