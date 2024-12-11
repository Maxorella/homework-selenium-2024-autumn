import allure

from hw.code.ui.locators.companiesLocator import CompaniesLocator
from hw.code.ui.pages.base_page import BasePage


class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CompaniesLocator

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step("Переход к созданию кампании")
    def create_new_company(self):
        self.click(self.locators.CREATE_NEW_COMPANY)

    @allure.step("Перейти к созданию рекламы сайта")
    def create_site_advertise(self):
        self.click(self.locators.CREATE_SITE_ADVERTISE)

    @allure.step("Перейти ко второму этапу")
    def transfer_to_group_advertise(self):
        self.create_new_company()
        self.create_site_advertise()
        self.enter_field(self.locators.SITE_HREF, "https://www.statista.com")
        self.click(self.locators.CREATE_SITE_ADVERTISE)
        self.enter_field(self.locators.BUDGET_FIELD, "100")
        self.click(self.locators.CONTINUE_BUTTON)
        self.click(self.locators.CONTINUE_BUTTON)