from datetime import time
import time
import allure
from selenium.webdriver.common.by import By

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginCarouselLoc


@allure.story("Carousel TestCase")
class TestCarousel(BaseCaseVkAd):
    authorize = False

    @allure.title("View carousel Test")
    def test_display_carousel(self):
        carousel = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_CONTAINER)
        assert carousel.is_displayed(), "Карусель не отображается на странице"

    @allure.title("Carousel autoscroll Test")
    def test_carousel_autoscroll(self):
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        container = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_BULLETS_CONTAINER)
        firstBullet = container.find_element(By.TAG_NAME, 'DIV')
        initial_class = firstBullet.get_attribute('class')
        time.sleep(8)
        new_class = firstBullet.get_attribute('class')

        assert initial_class != new_class, "Не произошло автопереключение"

    @allure.title("Carousel switch Test")
    def test_carousel_switch(self):
        container = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_BULLETS_CONTAINER)
        firstBullet = container.find_element(By.TAG_NAME, 'DIV')
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_2)
        initial_class = firstBullet.get_attribute('class')

        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        new_class = firstBullet.get_attribute('class')

        assert initial_class != new_class, "Не сработало переключение"

    @allure.title("Carousel button handler Test")
    def test_carousel_button(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        self.base_page.click(MainPageNoLoginCarouselLoc.CAROUSEL_HANDLE_BTN)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/promo/firstbonus',len('https://ads.vk.com/promo/firstbonus')), "Переход не произошел"
