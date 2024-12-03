import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.pages.events_page import EventsPage


class EventsCaseVkAd(BaseCaseVkAd):
    authorize = False
    use_cookie = False
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.events_page: EventsPage = (request.getfixturevalue('events_vk_ad_page'))
