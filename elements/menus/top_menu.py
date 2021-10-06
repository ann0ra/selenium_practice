from selenium.webdriver.common.by import By
from elements.pages.auth import AuthPage
from selenium.common.exceptions import NoSuchElementException

from elements.pages.cart import CartPage
from elements.pages.search import SearchPage


class TopMenu:
    SING_IN_BUTTON = (By.XPATH, '//a[@class="login"]')
    SING_OUT_BUTTON = (By.XPATH, '//a[@class="logout"]')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@class="account"]')
    SEARCH_FIELD = (By.XPATH, '//input[@id="search_query_top"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@name="submit_search"]')
    CART_BUTTON = (By.XPATH, '//div[@class="shopping_cart"]/a')

    def __init__(self, browser):
        self.browser = browser

    def is_sign_in_present(self):
        try:
            self.browser.find_element(*self.SING_IN_BUTTON)
            return True
        except NoSuchElementException:
            return False

    def sign_in(self):
        """ Click on Sign In button and go to AUTH page"""
        sign_in_button = self.browser.find_element(*self.SING_IN_BUTTON)
        sign_in_button.click()

        auth = AuthPage(self.browser)
        return auth

    def get_account_name(self):
        account_button = self.browser.find_element(*self.ACCOUNT_BUTTON)
        return account_button.text

    def sign_out(self):
        sign_out = self.browser.find_element(*self.SING_OUT_BUTTON)
        sign_out.click()

        return self

    def search_item(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(item)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

        return SearchPage(self.browser)

    def click_cart(self):
        cart_button = self.browser.find_element(*self.CART_BUTTON)
        cart_button.click()

        return CartPage(self.browser)
