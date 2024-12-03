import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.pages.cases_page import CasesPage


class CasesCaseVkAd(BaseCaseVkAd):
    authorize = False
    use_cookie = False
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.cases_page: CasesPage = (request.getfixturevalue('cases_vk_ad_page'))
