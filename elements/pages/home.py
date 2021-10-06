from selenium.webdriver.common.by import By

from elements.menus.top_menu import TopMenu
from helpers.element import find_elements, find_element


class HomePage:

    SHOP_NOW_BUTTON = (By.XPATH, '//button[@class="btn btn-default"]')
    CERTAIN_BANNER = (By.XPATH, '//a[@title="sample-3"]/parent::li[@class="homeslider-container"]')
    BANNER = (By.XPATH, '//li[@class="homeslider-container"]')

    NEXT_BANNER_BUTTON = (By.XPATH, '//a[@class="bx-next"]')

    def __init__(self, browser):
        self.browser = browser

        # Add top menu element
        self.top_menu = TopMenu(browser)

    def click_banner(self):
        banners = find_elements(self.browser, self.BANNER)
        for banner in banners:
            if banner.is_displayed():
                banner.click()
                return
        raise UserWarning('No banner')

    def click_certain_banner(self):
        attempt = 10
        while attempt > 0:
            banner = self.browser.find_element(*self.CERTAIN_BANNER)
            if banner.is_displayed():
                banner.click()
                return
            else:
                find_element(self.browser, self.NEXT_BANNER_BUTTON).click()
            attempt -= 1
        raise UserWarning('No banner')
