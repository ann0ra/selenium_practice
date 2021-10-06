from data.product import PRODUCT_FOR_SEARCH
from data.user import USERNAME, PASSWORD


def test_flow_logined_user(home_page):
    """
    Preconditions:
    1. Open browser and open the start page

    Steps:
    1. Click on "Sign in" button on the top menu
    2. Enter "email address" and "password" in the Auth form
    3. Click "Sign in" button
    4. Find a product
    5. Choose the first item, choose color and size
    6. Add the product to a cart
    7. Proceed checkout

    Expected result:
    1. Address is 'M, Alaska 12312''
    """
    auth_page = home_page.top_menu.sign_in()
    auth_page.auth_form.fill_in_form(USERNAME, PASSWORD)
    searching = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    modal_item = searching.choose_item().choose_color().choose_size().add_to_cart()
    checkout = modal_item.get_checkout()
    addresses = checkout.proceed_checkout()
    actual_address = addresses.get_address()
    expected_address = 'M, Alaska 12312'
    assert expected_address == actual_address, f'expected {expected_address}, but got {actual_address}'


def test_flow_new_user(home_page):
    search_item = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    modal_item = search_item.choose_item().choose_color().choose_size().add_to_cart()
    checkout = modal_item.get_checkout()
    login_page = checkout.proceed_checkout_new_user()
    actual_message = login_page.get_account_message()
    expected_message = 'Please enter your email address to create an account.'
    assert expected_message == actual_message
