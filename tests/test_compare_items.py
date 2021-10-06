import pytest

from data.product import PRODUCT_FOR_SEARCH


@pytest.mark.parametrize('number_to_compare, expected_product_number', [(1, 1), (3, 3)])
def test_compare(home_page, number_to_compare, expected_product_number):
    search_page = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    search_page = search_page.add_to_compare_item(number_to_compare)
    compare_page = search_page.get_compare_list()
    actual_product_number = compare_page.get_product_info()
    assert expected_product_number == actual_product_number, \
        f'Expected {expected_product_number}, but got {actual_product_number}'


def test_over_add(home_page):
    search_page = home_page.top_menu.search_item(PRODUCT_FOR_SEARCH)
    search_page = search_page.add_to_compare_item(4)
    actual_warning_text = search_page.get_compare_warning()
    expected_warning_text = 'You cannot add more than 3 product(s) to the product comparison'
    assert expected_warning_text == actual_warning_text, \
        f'Expected {expected_warning_text}, but got {actual_warning_text}'
