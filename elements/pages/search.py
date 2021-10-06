from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.pages.compare import ComparePage
from elements.pages.item import ItemPage
from helpers.element import find_elements, find_element, find_element_in_se


class SearchPage:

    FOUND_ITEMS = (By.XPATH, '//div[@id="center_column"]//a[@class="product-name"]')
    NOT_FOUND_ALERT = (By.XPATH, '//p[contains(@class, "alert-warning")]')
    SORT_FIELD = (By.XPATH, '//select[@id="selectProductSort"]')
    SORT_BY = (By.XPATH, '//option[@value="{}"]')
    ADD_TO_COMPARE_ICON = (By.XPATH, '//a[@class="add_to_compare"]')
    COMPARE_BUTTON = (By.XPATH, '//div[contains(@class, "top-pagination-content")]//button')
    COMPARISON_WARNING = (By.XPATH, '//div[@class="fancybox-outer"]')

    PRODUCTS_INFO = (By.XPATH, '//div[@class="product-container"]//div[@class="right-block"]')
    PRODUCT_NAME = (By.XPATH, './/a[@class="product-name"]')
    PRODUCT_PRICE = (By.XPATH, './/span[@class="price product-price"]')

    def __init__(self, browser):
        self.browser = browser

    def get_list_items(self):
        """
        Returns a list of items presented on a search page
        """
        products = find_elements(self.browser, self.PRODUCTS_INFO)
        items_info = []
        for product in products:
            items_info.append({
                'name': find_element_in_se(product, self.PRODUCT_NAME).text,
                'price': find_element_in_se(product, self.PRODUCT_PRICE).text,
            })

        return items_info

    def choose_item(self):
        """
        Finds the first item on a search page and choose it
        :return: an item page тип??
        """
        item = find_elements(self.browser, self.FOUND_ITEMS)[0]
        item.click()

        return ItemPage(self.browser)

    def _add_to_compare_list(self, item):
        """
        Add items to a compare list

        :param item: item for compare
        :return:
        """
        a = ActionChains(self.browser)
        a.move_to_element(item).perform()
        compare_icon = find_element(self.browser, self.ADD_TO_COMPARE_ICON)
        a.move_to_element(compare_icon).perform()
        compare_icon.click()

    def add_to_compare_item(self, number):
        """number of items which will be added"""
        items = find_elements(self.browser, self.FOUND_ITEMS)
        for item in items[:number]:
            self._add_to_compare_list(item)

        return self

    def get_compare_list(self):
        find_elements(self.browser, self.COMPARE_BUTTON)[0].click()

        return ComparePage(self.browser)

    def get_compare_warning(self) -> str:
        compare_warning = find_element(self.browser, self.COMPARISON_WARNING).text
        return compare_warning

    def sort_product(self, option: str = 'name:asc') -> list:
        """ Sort items alphabetically """

        sort_locator = (self.SORT_BY[0], self.SORT_BY[1].format(option))
        find_element(self.browser, sort_locator).click()

        return self.get_list_items()
