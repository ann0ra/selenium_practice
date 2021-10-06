from selenium.webdriver.common.by import By

from elements.pages.addres import AddressPage
from elements.pages.auth import AuthPage
from helpers.element import find_element


class CartPage:
    EMPTY_CART_TEXT = (By.XPATH, '//p[contains(@class, "alert")]')
    PRODUCT = (By.XPATH, '//tr[contains(@class, "cart_item")]')
    DELETE_ICON = (By.XPATH, '//a[@class="cart_quantity_delete"]')
    PROCEED_BUTTON = (By.XPATH, '//p//a[@title="Proceed to checkout"]')
    TOTAL_PRODUCT = (By.XPATH, '//td[@id="total_product"]')
    SUMMARY_PRODUCTS_QUANTITY = (By.XPATH, '//span[@id="summary_products_quantity"]')

    def __init__(self, browser):
        self.browser = browser

    def get_empty_cart_alert(self):
        cart_text_element = find_element(self.browser, self.EMPTY_CART_TEXT)
        return cart_text_element.text

    def delete_item(self):
        delete_item = self.browser.find_element(*self.DELETE_ICON)
        delete_item.click()

    def get_full_cart(self):
        summary = self.browser.find_element(*self.SUMMARY_PRODUCTS_QUANTITY).text
        return summary

    def get_total_product_price(self):
        total_product = find_element(self.browser, self.TOTAL_PRODUCT).text
        return total_product

    def remove_product(self):
        find_element(self.browser, self.DELETE_ICON).click()
        return self

    def proceed_checkout(self):
        find_element(self.browser, self.PROCEED_BUTTON).click()
        return AddressPage(self.browser)

    def proceed_checkout_new_user(self):
        find_element(self.browser, self.PROCEED_BUTTON).click()
        return AuthPage(self.browser)
