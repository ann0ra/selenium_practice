import pytest
from selenium import webdriver
from data.site import URL
from data.user import USERNAME, PASSWORD

from elements.pages.home import HomePage
from elements.pages.item import ItemPage


@pytest.fixture
def browser():
    """ Open browser and open the start page """
    driver = webdriver.Chrome(executable_path='driver/chromedriver')
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.delete_all_cookies()
    driver.close()
    driver.quit()


@pytest.fixture
def home_page(browser):
    """ Home page object """
    home = HomePage(browser)
    return home


@pytest.fixture
def sign_in(home_page):
    """ Sign in if not signed yet """
    if home_page.top_menu.is_sign_in_present():
        auth_page = home_page.top_menu.sign_in()
        auth_page.auth_form.fill_in_form(USERNAME, PASSWORD)

    return home_page


@pytest.fixture
def product(browser):
    """ Product page object """
    browser.get(f'{URL}/index.php?id_product=5&controller=product&search_query=dress&results=7')
    product = ItemPage(browser)
    return product
