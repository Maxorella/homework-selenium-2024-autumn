import allure
from selenium.webdriver.common.by import By

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginCookie


@allure.story("Cookie Test")
class TestCookie(BaseCaseVkAd):

    authorize = False
    @allure.title("Cookie view Test")
    def test_cookie(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

    @allure.title("Cookie view reload Test")
    def test_cookie_reload(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

        self.driver.refresh()

        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

    @allure.title("Cookie close Test")
    def test_cookie_close(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
        cookie.find_element(By.TAG_NAME, 'button').click()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True

    @allure.title('Cookie close reload Test')
    def test_cookie_close_reload(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
        cookie.find_element(By.TAG_NAME, 'button').click()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True

        self.driver.refresh()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True