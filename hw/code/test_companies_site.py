import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import TargetedActionsLocators, SiteLocators, CompaniesLocators, \
    GroupLocators


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

        self.base_page.move_to_element(CompaniesLocators.CONTINUE_BUTTON)
        self.base_page.click(CompaniesLocators.CONTINUE_BUTTON)

        self.base_page.find(GroupLocators.SET_DATE)

        assert  self.base_page.find(GroupLocators.STRATEGY_CONTAINER).is_displayed(), "Не перешли на следующую страницу"
