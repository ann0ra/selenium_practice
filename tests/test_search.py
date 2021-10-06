import pytest

from data.product import PRODUCT_FOR_SEARCH


def test_search(home_page):
    search_page = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    actual_search_result = []
    items_info = search_page.get_list_items()
    for item in items_info:
        name = item['name']
        actual_search_result.append(name)
    expected_search_result = ['Printed Summer Dress', 'Printed Dress', 'Printed Summer Dress',
                              'Printed Chiffon Dress', 'Printed Dress', 'Faded Short Sleeve T-shirts', 'Blouse']
    assert expected_search_result == actual_search_result, \
        f'expected: {expected_search_result}, but got {actual_search_result}'


def test_search_and_choose(home_page):
    search_page = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    item = search_page.choose_item()
    item = item.add_to_cart()
    actual_result = item.is_item_modal_present()

    assert actual_result, f'expected: modal window is visible, but got {actual_result}'


@pytest.mark.parametrize('option, expected_sorting', [
    ('name:asc', {
        'name': ['Blouse', 'Faded Short Sleeve T-shirts', 'Printed Chiffon Dress', 'Printed Dress', 'Printed Dress',
                 'Printed Summer Dress', 'Printed Summer Dress'],
        'price': ['$27.00', '$16.51', '$16.40', '$26.00', '$50.99', '$28.98', '$30.50']}),
    ('price:asc', {
        'name': ['Faded Short Sleeve T-shirts', 'Printed Chiffon Dress', 'Printed Dress', 'Blouse',
                 'Printed Summer Dress', 'Printed Summer Dress', 'Printed Dress'],
        'price': ['$16.51', '$16.40', '$26.00', '$27.00', '$30.50', '$28.98', '$50.99']})
])
def test_product_name_sort(home_page, option, expected_sorting):
    search_page = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    sorted_product_info = search_page.sort_product(option)

    actual_sorted_product_name = []
    actual_sorted_product_price = []
    for product in sorted_product_info:
        actual_sorted_product_name.append(product['name'])
        actual_sorted_product_price.append(product['price'])

    assert expected_sorting['name'] == actual_sorted_product_name, \
        f'expected {expected_sorting["name"]}, but got {actual_sorted_product_name}'
    assert expected_sorting['price'] == actual_sorted_product_price, \
        f'expected {expected_sorting["price"]}, but got {actual_sorted_product_price}'
