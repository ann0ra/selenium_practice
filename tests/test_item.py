def test_item(product):
    item = product.add_to_cart()
    modal_window = item.get_checkout()

    actual_cart_result = modal_window.get_full_cart()
    actual_total_result = modal_window.get_total_product_price()
    expected_cart_result = '1 Product'
    expected_product_result = '$28.98'
    assert expected_cart_result == actual_cart_result, \
        f'expected: {expected_cart_result}, but got {actual_cart_result}'
    assert expected_product_result == actual_total_result, \
        f'expected: {expected_product_result}, but got{actual_total_result}'


def test_item_quantity(product):
    item = product.add_quantity()
    actual_result = item.get_quantity()
    expected_result = '2'
    assert expected_result == actual_result


def test_reduce_quantity(product):
    item = product.add_quantity()
    multi_item = item.add_quantity()
    actual_quantity = multi_item.get_quantity()
    expected_quantity = '3'
    assert expected_quantity == actual_quantity
    reduced_quantity = multi_item.less_quantity()
    reduced_quantity = reduced_quantity.get_quantity()
    expected_quantity = '2'
    assert reduced_quantity == expected_quantity


def test_item_color(product):
    item = product.choose_color()
    modal = item.add_to_cart()

    actual_color = modal.get_product_color()
    expected_color = 'Blue'
    assert expected_color == actual_color, f'expected: {expected_color}, but got {actual_color}'


def test_item_size(product):
    item = product.choose_size()
    modal = item.add_to_cart()
    actual_size = modal.get_product_size()
    expected_size = 'M'
    assert expected_size == actual_size, f'expected: {expected_size}, but got {actual_size}'
