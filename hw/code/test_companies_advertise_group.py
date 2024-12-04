import allure

from hw.code.asserts.asserts import find_assert
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import GroupLocators


@allure.story("Группы объявлений")
class TestAdvertiseGroup(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Edit date")
    def test_edit_date(self):
        self.base_page.go_to_group()
        find_assert(self.base_page, GroupLocators.SET_DATE, 10, "Выбор даты не отображается")