import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(browser, locator, timeout=10):
    for _ in range(0, 100):
        if browser.execute_script('return jQuery.active') == 0:
            break
        time.sleep(0.5)
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.element_to_be_clickable(locator))
    return element


def find_elements(browser, locator, timeout=10):
    for _ in range(0, 100):
        if browser.execute_script('return jQuery.active') == 0:
            break
        time.sleep(0.5)
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.presence_of_all_elements_located(locator))
    return element


def find_element_in_se(element, locator):
    return element.find_element(*locator)


def find_elements_in_se(element, locator):
    return element.find_elements(*locator)
