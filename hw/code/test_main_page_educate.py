import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginEducate


@allure.story("Educate Test")
class TestEducate(BaseCaseVkAd):
    authorize = False

    @allure.title("Educate view Test")
    def test_educate(self):
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate = self.base_page.find(MainPageNoLoginEducate.EDUCATE_CONTAINER)

        assert educate.is_displayed(), "Блок не отображается"


    @allure.title("Educate more Test")
    def test_educate_more(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_ABOUT)
        self.base_page.click(MainPageNoLoginEducate.EDUCATE_ABOUT)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/events',
                                            len('https://ads.vk.com/events')), "Переход не произошел"



    @allure.title("Educate click Test")
    def test_educate_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate = self.base_page.find(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate.click()
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/events',
                                            len('https://ads.vk.com/events')), "Переход не произошел"
