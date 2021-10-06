from selenium.webdriver.common.by import By


class AuthForm:
    EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="passwd"]')
    SUNG_IN_BUTTON = (By.XPATH, '//button[@id="SubmitLogin"]')

    def __init__(self, browser):
        self.browser = browser

    def fill_in_form(self, email, password):
        email_field = self.browser.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

        sing_in_button = self.browser.find_element(*self.SUNG_IN_BUTTON)
        sing_in_button.click()
