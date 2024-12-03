import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.pages.materials_page import MaterialsPage
from hw.code.ui.pages.news_page import NewsPage


class MaterialsCaseVkAd(BaseCaseVkAd):
    authorize = False
    use_cookie = False
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.materials_page: MaterialsPage = (request.getfixturevalue('materials_vk_ad_page'))
