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

    def create_site_advertise(self):
        self.click(self.locators.CREATE_SITE_ADVERTISE)
