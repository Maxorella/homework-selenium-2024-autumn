def assert_compare_block_text(page_obj, locator, expected_text, timeout=10, message=None):

    text = page_obj.get_text(locator, timeout)
    assert text == expected_text, message

def assert_is_page_open(page_obj, locator, url, timeout=10, message=None):
    page_obj.click(locator, timeout)
    assert page_obj.is_opened(url), message

def find_assert(page_obj, locator, timeout=10, message=None):

    assert page_obj.find(locator, timeout).is_displayed(), message

def attribute_assert(page_obj, locator, attribute, expected, message=None):

    assert page_obj.get_attribute(locator, attribute) == expected, message

