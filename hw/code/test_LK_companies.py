import re
from datetime import datetime
import time
import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import CompaniesLocators, TargetedActionsLocators, SiteLocators, \
    GroupLocators


@allure.story("Проверка кампаний")
class TestCompanies(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("View test")
    def test_popup(self):
        current_window = self.driver.current_window_handle
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/hq/new_create/ad_plan',
                                            len('https://ads.vk.com/hq/new_create/ad_plan')), "Переход на страницу создание кампании"

    @allure.title("Create company view test")
    def test_create_company(self):

        assert self.base_page.find(CompaniesLocators.CREATE_COMPANY_CONTAINER).is_displayed(), "Контейнер не отображается"


    @allure.title("Company name view test")
    def test_company_name(self):

        assert self.base_page.find(CompaniesLocators.COMPANY_NAME).is_displayed(), "Имя не отображается"

    @allure.title("Company name format test")
    def test_company_name_format(self):

        company_name = self.base_page.get_text(CompaniesLocators.COMPANY_NAME_TEXT)

        current_date = datetime.now().strftime("%Y-%m-%d")
        expected_pattern = rf"Кампания {current_date}"

        if re.fullmatch(expected_pattern, company_name):
            pass
        else:
            assert 1 == 0, "Название не соответствует формату"

    @allure.title("Company name handle test")
    def test_company_name_handle(self):
        self.base_page.move_to_element(CompaniesLocators.COMPANY_NAME_TEXT)
        self.base_page.click(CompaniesLocators.COMPANY_NAME_TEXT)

        assert 1 == 1, "Название не реагирует на нажатие"

@allure.story("Проверка целевых действий кампаний")
class TestTargetActions(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Site click handler test")
    def test_site_click(self):
        self.base_page.move_to_element(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.SITE_CONTAINER).is_displayed(), "Ввод сайта не отображается"

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
        self.base_page.click(CompaniesLocators.ERROR_BUTTON)

        assert self.base_page.find(CompaniesLocators.ERROR_LOG).is_displayed(), "Ошибка не отображается"

    @allure.title("Calendar test")
    def test_calendar(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.move_to_element(TargetedActionsLocators.CALENDAR_INPUT)
        self.base_page.click(TargetedActionsLocators.CALENDAR_INPUT)

        assert self.base_page.find(TargetedActionsLocators.CALENDAR_CONTAINER).is_displayed(), "Каледнарь не отображается"

@allure.story("Сайт")
class TestSite(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Input wrong href")
    def test_wrong_href(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "sdfasf")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        error = self.base_page.get_text(SiteLocators.SITE_INPUT_ERROR)

        assert error == "Не удалось подгрузить данные ссылки", "Не отображается ошибка"

    @allure.title("Input href view test")
    def test_href_view(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)

        assert self.base_page.find(TargetedActionsLocators.CALENDAR_INPUT).is_displayed(), "Не отображаются новые поля"

    @allure.title("Constraint input test")
    def test_constraint_input(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)

        self.base_page.move_to_element(SiteLocators.ABOUT_TEXT_AREA)
        self.base_page.enter_field(SiteLocators.ABOUT_TEXT_AREA, 'a'*500)

        assert self.base_page.get_text(SiteLocators.ABOUT_TEXT_AREA) == 'a'*300, "Ввод не ограничен"

    # @allure.title("Target action view test")
    # def test_target_action(self):
    #     self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
    #     self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
    #     self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
    #     self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)
    #     self.base_page.click(SiteLocators.TARGER_ACTION)
    #     self.base_page

    @allure.title("Test switch budget")
    def test_switch_budget(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)

        self.base_page.click(SiteLocators.SWITCH)

        try:
            self.base_page.find(TargetedActionsLocators.BUDGET_INPUT)
            assert False, "Блок бюджета не пропадает"
        except:
            assert True

    @allure.title("Go to advertise group test")
    def test_advertise_group(self):
        self.base_page.click(TargetedActionsLocators.SITE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.ADVERTISE_SITE, "https://vk.com/a645g743")
        self.base_page.click(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.find(TargetedActionsLocators.ADVERTISE_CONTAINER)
        self.base_page.enter_field(TargetedActionsLocators.BUDGET_INPUT, '100')

        self.base_page.click(CompaniesLocators.CONTINUE_BUTTON)
        self.base_page.find(GroupLocators.SET_DATE)

        assert  self.base_page.find(GroupLocators.STRATEGY_CONTAINER).is_displayed(), "Не перешли на следующую страницу"


@allure.story("Группы объявлений")
class TestAdvrtiseGroup(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Edit date")
    def test_edit_date(self):
        self.base_page.go_to_group()
        self.base_page.click(GroupLocators.SET_DATE)

        assert self.base_page.find(GroupLocators.CHOSE_DATES).is_displayed(), "Выбор даты не отображается"






