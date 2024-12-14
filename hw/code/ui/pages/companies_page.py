import allure

from hw.code.ui.locators.companiesLocator import CompaniesLocator
from hw.code.ui.pages.base_page import BasePage


class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CompaniesLocator

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step("Поиск инпута ссылки на сайт")
    def find_href_input(self):
        self.advertise_href = self.find(self.locators.SITE_HREF)

    @allure.step("Поиск опции сайта в рекламе")
    def find_advertise_site_option(self):
        self.advertise_site_option = self.find(self.locators.CREATE_SITE_ADVERTISE)

    @allure.step("Ввод ссылки в поле рекламируемого сайта")
    def insert_site_href(self, href):
        self.enter_field_element(self.advertise_href,href)
        self.click(self.advertise_site_option)

    def set_budget(self, budget):
        self.budget_input = self.find(self.locators.BUDGET_FIELD)
        self.enter_field_element(self.budget_input,budget)
        self.click(self.continue_button)

    def wait_budget_error_not_present(self):
        err = self.find(self.locators.ERROR_BTN)
        self.is_element_not_present(err)

    def set_valid_end_date(self):
        self.find_and_click(self.locators.END_DATE)
        self.find_and_click(self.locators.DECEMBER_31)

    def set_invalid_end_date(self):
        self.find_and_click(self.locators.END_DATE)
        self.find_and_click(self.locators.DECEMBER_2)

    def fast_choice_moscow(self):
        self.find_and_click(self.locators.FAST_CHOICE_REGIONS)

    def choice_region_korolev(self):
        field = self.find(self.locators.REGION_SEARCH)
        self.enter_field_element(field, "Королев")
        self.find_and_click(self.locators.SEARCH_RESULT)

    @allure.step("Переход на следующий этап")
    def transfer_to_next_step(self):
        self.click(self.continue_button)

    def assert_valid_href(self):
        assert self.element_presented(self.locators.BUDGET_FIELD, 5), "Не раскрылись поля"

    def assert_invalid_href(self):
        err_el = self.find(self.locators.HREF_ERROR)
        err_text = self.get_element_text(err_el)
        assert err_text == "Не удалось подгрузить данные ссылки", 'Ошибка не отображается'

    def assert_error_view(self):
        self.find_and_click(self.locators.ERROR_BTN)
        site_error = self.find(self.locators.ADVERTISE_SITE_ERROR)
        err_text = self.get_element_text(site_error)
        assert err_text == "Рекламируемый сайт", "Не указывается возникшая ошибка"

    def assert_budget_error(self):
        self.find_and_click(self.locators.ERROR_BTN)
        site_error = self.find(self.locators.ADVERTISE_SITE_ERROR)
        err_text = self.get_element_text(site_error)
        assert err_text == "Бюджет", "Не обработана ошибка бюджета < 100"

    def assert_budget_save(self):
        budget = self.find(self.locators.BUDGET_DUPLICATE)
        assert self.get_element_text(budget) == "100 ₽", 'Не происходит сохранение бюджета'

    def assert_transfer_to_step_2(self):
        assert self.find(self.locators.EXPAND_REGION), "Переход на второй этап не сработал"

    def assert_end_input_date(self):
        assert self.get_attribute(self.locators.END_INPUT_DATE, 'value') == "31.12.2024", "Выбор даты не работает"

    def assert_invalid_end_input_date(self):
        assert self.get_attribute(self.locators.END_INPUT_DATE, 'value') == "", "Произошёл выбор прошедшей даты"

    def assert_choice_moscow(self):
        assert self.get_text(self.locators.CHOSEN_REGION) == "Москва", "Быстрый выбор не сработал"

    def assert_search_choice(self):
        assert self.get_text(self.locators.CHOSEN_REGION) == "Королев", "Поиск не сработал"

    def assert_few_regions(self):
        assert self.get_text(
            self.locators.NUMBER_CHOSEN) == '2 выбрано', 'Не сработал выбор нескольких регионов'

    def get_error_href_text(self):
        return self.get_text(self.locators.HREF_ERROR)

    @allure.step("Переход к созданию кампании")
    def create_new_company(self):
        self.find_and_click(self.locators.CREATE_NEW_COMPANY)

    @allure.step("Перейти к созданию рекламы сайта")
    def create_site_advertise(self):
        self.find_advertise_site_option()
        self.click(self.advertise_site_option)
        self.find_href_input()
        self.continue_button = self.find(self.locators.CONTINUE_BUTTON)

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

