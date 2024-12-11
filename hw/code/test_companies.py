import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка кампаний")
class TestCompanies(BaseCase):

    @allure.title("Тест валидной ссылки")
    def test_advertise_site_positive(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        assert companies_page.element_presented(companies_page.locators.BUDGET_FIELD, 5), "Не раскрылись поля"

    @allure.title("Тест невалидной ссылки")
    def test_advertise_site_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "rewq")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        error = companies_page.get_text(companies_page.locators.HREF_ERROR)

        assert error == "Не удалось подгрузить данные ссылки", 'Ошибка не отображается'

    @allure.title("Тест отображения ошибок")
    def test_error_view(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "rewq")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.ERROR_BTN)

        assert companies_page.get_text(companies_page.locators.ADVERTISE_SITE_ERROR) == "Рекламируемый сайт"

    @allure.title("Тест валидации бюджета")
    def test_budget_positive(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.enter_field(companies_page.locators.BUDGET_FIELD, "100")
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)

        assert companies_page.find(companies_page.locators.EXPAND_REGION), "Переход на следующий этап не сработал"

    @allure.title("Тест валидации бюджета 2")
    def test_budget_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.enter_field(companies_page.locators.BUDGET_FIELD, "50")
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.ERROR_BTN)

        assert companies_page.get_text(companies_page.locators.ADVERTISE_SITE_ERROR) == "Бюджет"

    # @allure.title("Тест валидации бюджета 3")
    # def test_budget_consumption(self, companies_page):
    #     companies_page.create_new_company()
    #     companies_page.create_site_advertise()
    #     companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
    #     companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
    #     companies_page.enter_field(companies_page.locators.BUDGET_FIELD, "999999999999999")
    #     companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
    #
    #     assert  companies_page.get_text(companies_page.locators.BUDGET_FIELD) == "9 999 999 999 999"

    @allure.title("Тест сохранения бюджета")
    def test_budget_save(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.enter_field(companies_page.locators.BUDGET_FIELD, "100")
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)

        assert companies_page.get_text(companies_page.locators.BUDGET_DUPLICATE) == "100 ₽"

    # @allure.title("Тест опции за всё время")
    # def test_all_time_budget(self, companies_page):
    #     companies_page.create_new_company()
    #     companies_page.create_site_advertise()
    #     companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
    #     companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)

    @allure.title("Тест календаря (выбора даты до)")
    def test_calendar_choice(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.click(companies_page.locators.END_DATE)
        companies_page.click(companies_page.locators.DECEMBER_31)

        assert companies_page.get_attribute(companies_page.locators.END_INPUT_DATE, 'value') == "31.12.2024"

    @allure.title("Негативный тест календаря")
    def test_calendar_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        companies_page.click(companies_page.locators.END_DATE)
        companies_page.click(companies_page.locators.DECEMBER_2)

        assert companies_page.get_attribute(companies_page.locators.END_INPUT_DATE, 'value') == '', "Произошёл выбор прошедшей даты"

    @allure.title("Проверка быстрого выбора региона")
    def test_region_fast_choice(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.FAST_CHOICE_REGIONS)

        assert companies_page.get_text(companies_page.locators.CHOSEN_REGION) == "Москва", "Быстрый выбор не сработал"

    @allure.title("Проверка поиска городов в регионах показа")
    def test_region_search(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.enter_field(companies_page.locators.REGION_SEARCH, "Королев")
        companies_page.click(companies_page.locators.SEARCH_RESULT)

        assert companies_page.get_text(companies_page.locators.CHOSEN_REGION) == "Королев", "Поиск не сработал"

    @allure.title("Проверка добавления нескольких регионов")
    def test_few_regions(self, companies_page):
        companies_page.transfer_to_group_advertise()

        companies_page.click(companies_page.locators.FAST_CHOICE_REGIONS)
        companies_page.enter_field(companies_page.locators.REGION_SEARCH, "Королев")
        companies_page.click(companies_page.locators.SEARCH_RESULT)

        assert companies_page.get_text(companies_page.locators.NUMBER_CHOSEN) == '2 выбрано', 'Не сработал выбор нескольких регионов'

    @allure.title("Демография. Тест на выбор пола")
    def test_demography_sex_choice(self, companies_page):
        companies_page.transfer_to_group_advertise()
