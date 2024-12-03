import allure

from hw.code.materials_case_vk import MaterialsCaseVkAd
from hw.code.ui.locators.vk_ad_materials_locators import MaterialsLocators


@allure.story("Materials page")
class TestMaterialsCaseVkAd(MaterialsCaseVkAd):
    @allure.title("Materials view page Test")
    def test_materials_page(self):

        assert self.materials_page.find(MaterialsLocators.MATERIALS_HEADER).is_displayed(), "Заголовок не отображается"
