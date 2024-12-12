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

    @allure.step("Перейти к третьему этапу")
    def transfer_to_advertisement(self):
        self.transfer_to_group_advertise()
        self.click(self.locators.FAST_CHOICE_REGIONS)
        self.click(self.locators.CONTINUE_BUTTON)
        self.find(self.locators.ADVERTISEMENT_SETTINGS)

    @allure.step("create company")
    def create_company(self):
        self.transfer_to_advertisement()
        self.move_to_element(self.locators.TITLE)
        self.enter_field(self.locators.TITLE, 'Тест')
        self.move_to_element(self.locators.SHORT_DESCRIPTION)
        self.enter_field(self.locators.SHORT_DESCRIPTION, 'Тест')
        self.move_to_element(self.locators.MEDIAFILES_BUTTON)
        self.click(self.locators.MEDIAFILES_BUTTON)
        self.find(self.locators.MEDIA_PICTURE)
        self.click(self.locators.MEDIA_PICTURE)
        self.click(self.locators.ADD_PICTURES)
        self.move_to_element(self.locators.ABOUT)
        text = self.get_text(self.locators.ABOUT)
        if text == '':
            self.enter_field(self.locators.ABOUT, 'Жидков Антон Алексеевич, ИНН 501818145478')

        self.find(self.locators.AI_IMAGE)
        self.click(self.locators.CONTINUE_BUTTON)

        self.find(self.locators.COMPANY_NAME, timeout=20)

    @allure.step("delete all companies")
    def delete_all_companies(self):
        self.click(self.locators.BASE_PAGE)
        self.find(self.locators.COMPANIES, timeout=20)
        self.click(self.locators.COMPANIES)

        self.click(self.locators.SELECT_ALL, timeout=10)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.DELETE_ACTION)