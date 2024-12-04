import allure

from hw.code.asserts.asserts import find_assert
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import TargetedActionsLocators, CompaniesLocators


@allure.story("Проверка целевых действий кампаний")
class TestTargetActions(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Site click handler test")
    def test_site_click(self):
        self.base_page.move_to_element(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)

        find_assert(self.base_page, TargetedActionsLocators.SITE_CONTAINER, 10, "Ввод сайта не отображается")
    @allure.title("Target catalog handler test")
    def test_target_catalog(self):
        self.base_page.click(TargetedActionsLocators.CATALOG_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.CATALOG_PROPERTIES).is_displayed(), "Выбор объекта не отображается"

    @allure.title("Mobile handler test")
    def test_mobile(self):
        self.base_page.click(TargetedActionsLocators.MOBILE_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.MOBILE_INPUT).is_displayed(), "Ввод мобильного приложения не отображается"

    @allure.title("Community handler test")
    def test_community(self):
        self.base_page.click(TargetedActionsLocators.COMMUNITY_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.COMMUNITY_INPUT).is_displayed(), "Ввод сообщества не отображается"

    @allure.title("OK handler test")
    def test_ok(self):
        self.base_page.click(TargetedActionsLocators.OK_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.OK_INPUT).is_displayed(), "Ввод ОК не отображается"

    @allure.title("Dzen handler test")
    def test_dzen(self):
        self.base_page.click(TargetedActionsLocators.DZEN_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.DZEN_INPUT).is_displayed(), "Ввод Дзена не отображается"

    @allure.title("Lead handler test")
    def test_lead(self):
        self.base_page.click(TargetedActionsLocators.LEAD_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.LEAD_INPUT).is_displayed(), "Ввод лид форм не отображается"

    @allure.title("VK mini apps handler test")
    def test_vk_mini(self):
        self.base_page.click(TargetedActionsLocators.VK_MINI_APPS_CONTAINER)

        assert  self.base_page.find(TargetedActionsLocators.VK_MINI_APPS_INPUT).is_displayed(), "Ввод мини приложений не отображается"

    @allure.title("Music handler test")
    def test_music(self):
        self.base_page.click(TargetedActionsLocators.MUSIC_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.MUSIC_INPUT).is_displayed(), "Ввод музыки не отображается"

    @allure.title("Video handler test")
    def test_video(self):
        self.base_page.click(TargetedActionsLocators.VIDEO_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.VIDEO_INPUT).is_displayed(), "Ввод видео не отображается"

    @allure.title("Site continue error test")
    def test_site_continue_error(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)

        self.base_page.click(CompaniesLocators.CONTINUE_BUTTON)

        self.base_page.move_to_element(CompaniesLocators.ERROR_BUTTON)
        self.base_page.click(CompaniesLocators.ERROR_BUTTON)

        assert self.base_page.find(CompaniesLocators.ERROR_LOG).is_displayed(), "Ошибка не отображается"

    @allure.title("Calendar test")
    def test_calendar(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER, 20)
        self.base_page.move_to_element(TargetedActionsLocators.CALENDAR_INPUT)
        self.base_page.click(TargetedActionsLocators.CALENDAR_INPUT)

        assert self.base_page.find(TargetedActionsLocators.CALENDAR_CONTAINER, 10).is_displayed(), "Каледнарь не отображается"
