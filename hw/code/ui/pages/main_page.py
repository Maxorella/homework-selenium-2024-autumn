import os
import time
from contextlib import contextmanager
import json

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.locators.vk_ad_main_locators import AuthLocators


from hw.code.ui.locators.vk_ad_main_locators import AuthLocators
from hw.code.ui.pages.base_page import BasePage


class MainPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    # locators = Locators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()
