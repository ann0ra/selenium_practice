from selenium.webdriver.common.by import By

from elements.forms.auth_form import AuthForm
from helpers.element import find_element


class AuthPage:
    CREATE_ACCOUNT_FORM = (By.XPATH, '//form[@id="create-account_form"]')
    FORM_MESSAGE = (By.XPATH, '//form[@id="create-account_form"]//p')

    def __init__(self, browser):
        self.browser = browser

        # Add auth form element
        self.auth_form = AuthForm(browser)

    def get_account_message(self):
        message = find_element(self.browser, self.FORM_MESSAGE).text
        return message
