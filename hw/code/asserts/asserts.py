import re


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

def assert_click_try(page_obj, locator, message=None):

    try:
        page_obj.click(locator)
        assert False, message
    except:
        assert True

def assert_is_page_opened(page_obj, url, trunc=0, timeout=10, message=None):
    assert page_obj.is_opened(url, trunc, timeout), message


def assert_regexp(page_obj, locator, expected_pattern, timeout=5, message=None):
    text = page_obj.get_text(locator, timeout)

    if re.fullmatch(expected_pattern, text):
        pass
    else:
        assert 1 == 0, message


def assert_constraint_input(page_obj, locator, expected_input, trunc_size, timeout=10, message=None):
    page_obj.enter_field(locator, expected_input)
    text = page_obj.get_text(locator, timeout)
    assert text == expected_input[:trunc_size], message