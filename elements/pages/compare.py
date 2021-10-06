from selenium.webdriver.common.by import By

from helpers.element import find_elements


class ComparePage:
    COMPARISON_TABLE = (By.XPATH, '//table[@id="product_comparison"]')
    PRODUCT_INFO = (By.XPATH, '//td[contains(@class, "product-block")]')

    def __init__(self, browser):
        self.browser = browser

    def get_product_info(self):
        product_info = find_elements(self.browser, self.PRODUCT_INFO)
        return len(product_info)
