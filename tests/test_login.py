from selenium.common.exceptions import NoSuchElementException

from data.user import USERNAME, PASSWORD, FIRST_NAME, LAST_NAME


def test_login(home_page):
    """
    Preconditions:
    1. Open browser and open the start page

    Steps:
    1. Click on "Sign in" button on the top menu
    2. Enter "email address" and "password" in the Auth form
    3. Click "Sign in" button

    Expected result:
    1. There is "Sign out" button presented on the top menu
    2. There is "<FIRST_NAME> <LAST_NAME>" presented on the top menu
    """
    auth_page = home_page.top_menu.sign_in()
    auth_page.auth_form.fill_in_form(USERNAME, PASSWORD)
    account_name = home_page.top_menu.get_account_name()

    assert f'{FIRST_NAME} {LAST_NAME}' == account_name, f'Expected: {FIRST_NAME} {LAST_NAME}, but got {account_name}'


def test_sign_out(sign_in):
    menu = sign_in.top_menu.sign_out()
    assert sign_in.top_menu.is_sign_in_present()
    try:
        menu.get_account_name()
        assert False
    except NoSuchElementException:
        assert True
