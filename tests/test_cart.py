def test_cart(home_page):
    expected_alert_message = 'Your shopping cart is empty.'
    cart_page = home_page.top_menu.click_cart()

    actual_alert_message = cart_page.get_empty_cart_alert()

    assert expected_alert_message == actual_alert_message, \
        f'Messages are not equal. Expected {expected_alert_message}, but got {actual_alert_message}'


def test_full_cart(product):
    cart = product.add_to_cart().get_checkout()
    empty_cart_alert = cart.remove_product().get_empty_cart_alert()
    expected_cart = 'Your shopping cart is empty.'
    assert expected_cart == empty_cart_alert, f'Expected {expected_cart}, but got {empty_cart_alert}'
