def test_banner(home_page):
    """ Click to a banner on the main page and check that it was redirected to external website """
    home_page.click_banner()
    assert 'prestashop.com' in home_page.browser.current_url, \
           f'Expected "prestashop.com", but got {home_page.browser.current_url}'


def test_certain_banner(home_page):
    home_page.click_certain_banner()
    assert 'prestashop.com' in home_page.browser.current_url, \
           f'Expected "prestashop.com", but got {home_page.browser.current_url}'
