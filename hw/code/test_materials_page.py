import allure

from hw.code.asserts.asserts import find_assert
from hw.code.materials_case_vk import MaterialsCaseVkAd
from hw.code.ui.locators.vk_ad_materials_locators import MaterialsLocators


@allure.story("Materials page")
class TestMaterialsCaseVkAd(MaterialsCaseVkAd):
    @allure.title("Materials view page Test")
    def test_materials_page(self):

        find_assert(self.materials_page, MaterialsLocators.MATERIALS_HEADER, message="Заголовок не отображается")
