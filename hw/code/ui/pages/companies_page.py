import logging

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

    def switch_strategy(self, index):
        strategy = self.find(self.locators.STRATEGY)
        self.move_to_element(strategy)
        select = self.find_presence(self.locators.STRATEGY_SELECT)
        select = self.select_element(select)
        select.select_by_index(index)


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

    def choose_male_sex(self):
        demography = self.find(self.locators.DEMOGRAPHY_CONTAINER)
        self.click(demography)
        self.male_sex = self.find(self.locators.MALE_SEX)
        self.click(self.male_sex)

    def open_interest_and_behaviour(self):
        self.find_and_click(self.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        self.interest_container = self.find(self.locators.INTEREST_CONTAINER)
        self.key_phrases_container = self.find(self.locators.KEY_PHRASES_CONTAINER)
        self.communities_container = self.find(self.locators.COMMUNITIES_CONTAINER)
        self.musician_container = self.find(self.locators.MUSICIANS_CONTAINER)

    def open_interest(self):
        self.click(self.interest_container)

    def choose_first_interest(self):
        self.find_and_click(self.locators.INTEREST_INPUT)
        self.find_and_click(self.locators.FIRST_SEARCH_INTEREST)
        self.choosen_interest = self.find(self.locators.CHOSEN_INTEREST)

    def delete_interest(self):
        self.find_and_click(self.locators.DELETE_CHOSEN_INTEREST)

    def exclude_first_interest(self):
        self.find_and_click(self.locators.ADD_EXCLUDES)
        self.find_and_click(self.locators.EXCLUDES_INPUT)
        self.find_and_click(self.locators.FIRST_SEARCH_INTEREST)
        self.choosen_interest = self.find(self.locators.CHOSEN_INTEREST)

    def delete_all_interest(self):
        trash_bean = self.find(self.locators.DELETE_INTEREST)
        self.click(trash_bean)
        self.is_element_not_present(trash_bean)

    def open_interest_with_plus(self):
        open_button = self.find(self.locators.ADD_INTEREST)
        self.is_element_visible(open_button)
        self.click(open_button)

    def open_key_phrases(self):
        self.move_to_element(self.key_phrases_container)
        self.click(self.key_phrases_container)

    def insert_key_phases(self, phrases):
        self.input_key_phrases = self.find(self.locators.INPUT_KEY_PHRASES)
        self.move_to_element(self.input_key_phrases)
        self.enter_field_element(self.input_key_phrases, phrases)

    def insert_minus_phrases(self, phrases):
        self.input_minus_phrases = self.find(self.locators.INPUT_MINUS_PHRASES)
        self.move_to_element(self.input_minus_phrases)
        self.enter_field_element(self.input_minus_phrases, phrases)

    def insert_search_period(self, period):
        self.search_period = self.find(self.locators.SEARCH_PERIOD)
        self.move_to_element(self.search_period)
        self.enter_field_element(self.search_period, period)

    def confirm_search_period(self):
        self.click(self.key_phrases_container)

    def delete_key_phrases(self):
        trash_bean = self.find(self.locators.DELETE_KEY_PHRASES)
        self.click(trash_bean)
        self.is_element_not_present(trash_bean)

    def open_hey_phrases_with_animation(self):
        open_button = self.find(self.locators.ADD_KEY_PHRASES)
        self.is_element_visible(open_button)
        self.click(open_button)

    def open_communities(self):
        self.move_to_element(self.communities_container)
        self.click(self.communities_container)

    def insert_community_search(self, search):
        self.community_search = self.find(self.locators.COMMUNITIES_INPUT)
        self.move_to_element(self.community_search)
        self.enter_field_element(self.community_search, search)
        self.vk_communitites = self.find(self.locators.VK_COMMUNITIES, timeout=20)
        self.ok_communitites = self.find(self.locators.OK_COMMUNITIES, timeout=20)

    def choose_first_vk_community(self):
        self.click(self.vk_communitites)
        self.find_and_click(self.locators.FIRST_SEARCHED)
        self.click(self.vk_communitites)

    def choose_first_ok_community(self):
        self.click(self.ok_communitites)
        self.find_and_click(self.locators.FIRST_SEARCHED_OK)
        self.click(self.ok_communitites)

    def delete_chosen_community(self):
        self.find_and_click(self.locators.DELETE_GROUP)

    def cancel_communities(self):
        self.cancel_communities_btn = self.find(self.locators.CANCEL_BTN)
        self.click(self.cancel_communities_btn)

    def delete_communities(self):
        trash_bean = self.find(self.locators.COMMUNITIES_DELETE_ALL)
        self.click(trash_bean)
        self.is_element_not_present(trash_bean)

    def open_communities_with_plus(self):
        open_btn = self.find(self.locators.OPEN_COMMUNITIES)
        self.is_element_visible(open_btn)
        self.click(open_btn)

    def open_musicians(self):
        self.move_to_element(self.musician_container)
        self.click(self.musician_container)

    def insert_musicians_search(self, search):
        musician_input = self.find(self.locators.MUSICIANS_INPUT)
        self.move_to_element(musician_input)
        self.enter_field_element(musician_input, search)

    def choose_first_musician(self):
        self.find_and_click(self.locators.FIRST_MUSICIAN)
        self.find_and_click(self.locators.DONE_MUSICIANS_SEARCH)

    def delete_chosen_musician(self):
        self.find_and_click(self.locators.DELETE_SEARCHED_MUSICIAN)

    def delete_all_musicians(self):
        self.find_and_click(self.locators.MUSICIANS_DELETE_ALL)

    def delete_trash_bean_musician(self):
        trash_bean = self.find(self.locators.MUSICIANS_TRASH_BEAN)
        self.click(trash_bean)
        self.is_element_not_present(trash_bean)

    def open_musicians_with_plus(self):
        open_btn = self.find(self.locators.OPEN_MUSICIANS)
        self.click(open_btn)

    def insert_title(self,title):
        self.title = self.find(self.locators.TITLE)
        self.move_to_element(self.title)
        self.enter_field_element(self.title, title)

    def insert_short_description(self, description):
        self.description = self.find(self.locators.SHORT_DESCRIPTION)
        self.move_to_element(self.description)
        self.enter_field_element(self.description, description)

    def insert_about(self, about):
        self.about = self.find(self.locators.ABOUT)
        self.move_to_element(self.about)
        self.enter_field_element(self.about, about)

    def insert_media(self):
        mediafiles = self.find(self.locators.MEDIAFILES_BUTTON)
        self.move_to_element(mediafiles)
        self.click(mediafiles)
        picture = self.find(self.locators.MEDIA_PICTURE)
        self.click(picture)
        self.find_and_click(self.locators.ADD_PICTURES)

    def save_company_name(self):
        self.company_name = self.get_text(self.locators.COMPANY_NAME_)

    def wait_video_loaded(self):
        self.find(self.locators.AI_IMAGE)

    def save_company_name_companies(self):
        self.company_name = self.get_text(self.locators.COMPANY_NAME)

    def dont_save_draft(self):
        draft = self.find(self.locators.DONT_SAVE_DRAFT)
        self.click(draft)

    def duplicate_company(self):
        self.find_and_click(self.locators.CLOSE_SUGGEST)
        company = self.find(self.locators.COMPANY_STRING)
        self.move_to_element(company)
        options = self.find(self.locators.COMPANY_OPTIONS)
        self.move_to_element(options)
        self.click(options)
        duplicate = self.find(self.locators.COMPANY_DUPLICATE)
        self.wait_elemnt_enabled(duplicate)
        self.click(duplicate)
        self.find(self.locators.REDACT_OBJECT)
        self.duplicated_name = self.find(self.locators.COMPANY_NAME_)


    def full_duplicate(self):
        self.continue_button = self.find(self.locators.CONTINUE_BUTTON)
        self.transfer_to_next_step()
        self.open_interest_and_behaviour()
        self.transfer_to_next_step()
        self.find(self.locators.TITLE)
        self.transfer_to_next_step()


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

    def assert_strategy(self):
        assert self.get_text(self.locators.STRATEGY_SELECTED) == 'Предельная цена', 'Переключение Select не работает'

    def assert_invalid_end_input_date(self):
        assert self.get_attribute(self.locators.END_INPUT_DATE, 'value') == "", "Произошёл выбор прошедшей даты"

    def assert_choice_moscow(self):
        assert self.get_text(self.locators.CHOSEN_REGION) == "Москва", "Быстрый выбор не сработал"

    def assert_search_choice(self):
        assert self.get_text(self.locators.CHOSEN_REGION) == "Королев", "Поиск не сработал"

    def assert_few_regions(self):
        assert self.get_text(
            self.locators.NUMBER_CHOSEN) == '2 выбрано', 'Не сработал выбор нескольких регионов'

    def assert_male_sex_selected(self):
        input = self.find(self.locators.MALE_SEX_INPUT)
        assert input.is_selected() == True, "Выбор пола не работает"

    def assert_interest_input(self):
        assert self.get_element_text(self.choosen_interest) == 'Авто', 'Поиск не работает'

    def assert_interest_delete(self):
        assert self.is_element_not_present(self.locators.CHOSEN_INTEREST), "Удаление категории не произошло"

    def assert_interest_error(self):
        assert self.get_text(
            self.locators.INTEREST_ERROR) == 'Нельзя исключать добавленное — просто удалите это из интересов', 'Конфликт интересов не проверяется'

    def assert_all_interest_deleted(self):

        assert self.is_element_not_present(
            self.choosen_interest), 'Удаление интересов не произошло'

    def assert_key_phrases_suggest(self):
        assert self.get_text(
            self.locators.PHRASES_SUGGEST) == 'Показать 10 похожих', "Подсказки не работают"

    def assert_minus_phrases_input(self):
        assert self.get_element_text(
            self.input_minus_phrases) == 'Авто', "Поле минус фразы заблокировано"

    def assert_phrases_conflict(self):
        assert self.get_text(
            self.locators.PHRASES_WARNINGS) == 'У вас дублируется\n1 фраза', 'Не обработано дублирование фраз'

    def assert_search_period_input(self):
        assert self.get_element_attribute(self.search_period,
                                            "value") == "30", "Ввод не ограничен 2 символами"

    def assert_big_search_period(self):
        assert self.get_element_attribute(self.search_period,
                                            "value") == "30", "Ввод не исправляет значение на 30"

    def assert_zero_search_period(self):
        assert self.get_element_attribute(self.search_period,
                                          "value") == "1", "Ввод не исправляет значение на 1"

    def assert_key_phrases_deleted(self):
        assert self.get_element_attribute(self.search_period,
                                          "value") == "15", "Значение периода не сохраняется"

    def assert_choose_communities(self):
        assert self.get_text(
            self.locators.COMMUNITY_COUNTER) == 'Выбрано 2 сообщества', 'Выбор сообщества не работает'

    def assert_delete_community(self):
        assert self.is_not_present(
            self.locators.SELECTED_GROUP), 'Удаление выбранной группы не работает'

    def assert_cancel_communities(self):
        assert self.is_element_not_present(
            self.cancel_communities_btn), 'Кнопка отмены не работает'

    def assert_delete_communities(self):
        assert self.is_element_not_present(
            self.locators.SELECTED_GROUP), 'Кнопка корзины не работает'

    def assert_choose_musician(self):
        assert self.get_text(
            self.locators.SELECTED_MUSICIAN_COUNTER) == 'Выбран 1 музыкант', 'Выбор музыканта не работает'

    def assert_delete_musician(self):
        assert self.is_not_present(self.locators.SELECTED_MUSICIAN), 'Удаление музыканта не работает'

    def assert_delete_all_musician(self):
        assert self.is_not_present(self.locators.SELECTED_MUSICIAN), 'Удаление всех музыкантов не работает'

    def assert_delete_trash_bean(self):
        assert self.is_not_present(
            self.locators.SELECTED_MUSICIAN), 'Корзина не работает'

    def assert_transfer_to_advertisement(self):
        assert self.find(
            self.locators.ADVERTISEMENT_SETTINGS), 'Переход на этап объявления не произошёл'

    def assert_title_input(self):
        assert self.get_element_text(self.title) == 'Тест', 'Ввод заголовка заблокирован'

    def assert_description_input(self):
        assert self.get_element_text(self.description) == 'Тест', 'Ввод короткого описания заблокирован'

    def assert_about_input(self):
        assert self.get_element_text(self.about) == 'Иванов Иван Иванович, ИНН 501818145478', 'Ввод о рекламодателе заблокирован'

    def assert_add_media(self):
        assert self.wait_for_clickable(self.locators.IMAGES,
                                                 timeout=20), 'Загрузка фотографии не работает.'

    def assert_complete_advertisement(self):
        name = self.find(self.locators.COMPANY_NAME, timeout=20)
        assert self.get_element_text(name) == self.company_name, 'Кампания не создаётся'

    def assert_duplicated_company_name(self):
        assert self.get_element_text(
            self.duplicated_name) == 'копия ' + self.company_name, 'Имя копии задаётся неверно'

    def assert_duplicated_company(self):
        name = self.find(self.locators.DUPLICATED_NAME, timeout=20)
        assert self.get_element_text(name) != self.duplicated_name, 'Копия не создалась'

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
        self.insert_site_href("https://www.statista.com")
        self.set_budget("100")
        self.wait_budget_error_not_present()
        self.transfer_to_next_step()

    @allure.step("Перейти к третьему этапу")
    def transfer_to_advertisement(self):
        self.transfer_to_group_advertise()
        self.fast_choice_moscow()
        self.transfer_to_next_step()

    @allure.step("create company")
    def create_company(self):
        self.transfer_to_advertisement()
        self.insert_title('Тест')
        self.insert_short_description('Тест')
        self.insert_media()
        self.insert_about('Иванов Иван Иванович, ИНН 501818145478')

        self.save_company_name()
        self.wait_video_loaded()
        self.transfer_to_next_step()
        self.find(self.locators.COMPANY_NAME, timeout=60)

    @allure.step("delete all companies")
    def delete_all_companies(self):
        self.find_and_click(self.locators.BASE_PAGE)
        companies = self.find(self.locators.COMPANIES, timeout=20)
        self.click(companies)

        self.find_and_click(self.locators.SELECT_ALL, timeout=10)
        self.find_and_click(self.locators.ACTIONS)
        self.find_and_click(self.locators.DELETE_ACTION)

    def delete_companies(self):
        self.find_and_click(self.locators.SELECT_ALL, timeout=10)
        self.find_and_click(self.locators.ACTIONS)
        self.find_and_click(self.locators.DELETE_ACTION)

    def go_to_base_page(self):
        self.find_and_click(self.locators.BASE_PAGE)
        self.dont_save_draft()

    def go_to_companies(self):
        companies = self.find(self.locators.COMPANIES, timeout=20)
        self.click(companies)