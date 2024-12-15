import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка кампаний")
class TestCompanies(BaseCase):

    @allure.title("Тест валидной ссылки")
    def test_advertise_site_positive(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")

        companies_page.assert_valid_href()

    @allure.title("Тест невалидной ссылки")
    def test_advertise_site_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("rewq")

        companies_page.assert_invalid_href()

    @allure.title("Тест отображения ошибок")
    def test_error_view(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")
        companies_page.transfer_to_next_step()

        companies_page.assert_error_view()


    @allure.title("Тест валидации бюджета")
    def test_budget_valid(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")
        companies_page.set_budget("100")
        companies_page.wait_budget_error_not_present()

        companies_page.transfer_to_next_step()


    @allure.title("Тест валидации бюджета 2")
    def test_budget_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")
        companies_page.set_budget("50")

        companies_page.assert_budget_error()


    @allure.title("Тест сохранения бюджета")
    def test_budget_save(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")
        companies_page.enter_field(companies_page.locators.BUDGET_FIELD, "100")
        companies_page.transfer_to_next_step()

        companies_page.assert_budget_save()

    @allure.title("Тест календаря (выбора даты до)")
    def test_calendar_choice(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")

        companies_page.set_valid_end_date()

        companies_page.assert_end_input_date()

    @allure.title("Негативный тест календаря")
    def test_calendar_negative(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.insert_site_href("https://www.statista.com")

        companies_page.set_invalid_end_date()

        companies_page.assert_invalid_end_input_date()

    @allure.title("Проверка быстрого выбора региона")
    def test_region_fast_choice(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.fast_choice_moscow()

        companies_page.assert_choice_moscow()

    @allure.title("Проверка поиска городов в регионах показа")
    def test_region_search(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.choice_region_korolev()

        companies_page.assert_search_choice()

    @allure.title("Проверка добавления нескольких регионов")
    def test_few_regions(self, companies_page):
        companies_page.transfer_to_group_advertise()

        companies_page.fast_choice_moscow()
        companies_page.choice_region_korolev()

        companies_page.assert_few_regions()


    @allure.title("Демография. Тест на выбор пола")
    def test_demography_sex_choice(self, companies_page):
        companies_page.transfer_to_group_advertise()

        companies_page.choose_male_sex()

        companies_page.assert_male_sex_selected()


    @allure.title("Интересы и поведение. Тест строки интересов")
    def test_interest_input(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest()
        companies_page.choose_first_interest()

        companies_page.assert_interest_input()

    @allure.title("Удаление выбранной категории")
    def test_interest_delete(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.delete_interest()

        companies_page.assert_interest_delete()

    # На английском для саджестов
    @allure.title("Exclude interest test")
    def test_interest_exclude(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest()
        companies_page.exclude_first_interest()

        companies_page.assert_interest_input()

    @allure.title("interest and exclude interest conflict test")
    def test_interest_conflict(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.exclude_first_interest()
        companies_page.transfer_to_next_step()

        companies_page.assert_interest_error()

    @allure.title("delete interest test")
    def test_interest_delete_exclude(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.exclude_first_interest()

        companies_page.delete_all_interest()
        companies_page.open_interest_with_plus()
        companies_page.assert_all_interest_deleted()

    @allure.title("key phrases suggest test")
    def test_keyphrases_suggest(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest() # закончил тут
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.INPUT_KEY_PHRASES)
        companies_page.enter_field(companies_page.locators.INPUT_KEY_PHRASES, 'Авто')

        assert companies_page.get_text(companies_page.locators.PHRASES_SUGGEST) == 'Показать 10 похожих', "Подсказки не работают"

    @allure.title("minus phrases test")
    def test_minus_phrases(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.INPUT_MINUS_PHRASES)
        companies_page.enter_field(companies_page.locators.INPUT_MINUS_PHRASES, 'Авто')

        assert companies_page.get_text(companies_page.locators.INPUT_MINUS_PHRASES) == 'Авто', "Поле минус фразы заблокировано"

    @allure.title("phrases conflict test")
    def test_phrases_conflict(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.INPUT_KEY_PHRASES)
        companies_page.enter_field(companies_page.locators.INPUT_KEY_PHRASES, 'Авто')
        companies_page.move_to_element(companies_page.locators.INPUT_MINUS_PHRASES)
        companies_page.enter_field(companies_page.locators.INPUT_MINUS_PHRASES, 'Авто')

        assert companies_page.get_text(companies_page.locators.PHRASES_WARNINGS) == 'У вас дублируется\n1 фраза', 'Не обработано дублирование фраз'

    @allure.title("search period test")
    def test_search_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)

        companies_page.move_to_element(companies_page.locators.SEARCH_PERIOD)
        companies_page.enter_field(companies_page.locators.SEARCH_PERIOD, "300")

        assert companies_page.get_attribute(companies_page.locators.SEARCH_PERIOD, "value") == "30", "Ввод не ограничен 2 символами"

    @allure.title("enter big period test")
    def test_enter_big_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)

        companies_page.move_to_element(companies_page.locators.SEARCH_PERIOD)
        companies_page.enter_field(companies_page.locators.SEARCH_PERIOD, "50")
        companies_page.click(companies_page.locators.FIELDS_CONTAINER)

        assert companies_page.get_attribute(companies_page.locators.SEARCH_PERIOD, "value") == "30", "Ввод не исправляет значение на 30"

    @allure.title("enter zero period test")
    def test_enter_zero_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)

        companies_page.move_to_element(companies_page.locators.SEARCH_PERIOD)
        companies_page.enter_field(companies_page.locators.SEARCH_PERIOD, "0")
        companies_page.click(companies_page.locators.FIELDS_CONTAINER)

        assert companies_page.get_attribute(companies_page.locators.SEARCH_PERIOD,
                                            "value") == "1", "Ввод не исправляет значение на 1"

    @allure.title("delete key phrases test")
    def test_delete_key_phrases(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)

        companies_page.move_to_element(companies_page.locators.SEARCH_PERIOD)
        companies_page.enter_field(companies_page.locators.SEARCH_PERIOD, "15")

        companies_page.click(companies_page.locators.DELETE_KEY_PHRASES)
        companies_page.click(companies_page.locators.KEY_PHRASES_CONTAINER)

        assert companies_page.get_attribute(companies_page.locators.SEARCH_PERIOD,
                                            "value") == "15", "Значение периода не сохраняется"

    @allure.title("communities choose test")
    def test_communities_choose(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.COMMUNITIES_INPUT)
        companies_page.enter_field(companies_page.locators.COMMUNITIES_INPUT, 'Профсоюз')
        companies_page.click(companies_page.locators.VK_COMMUNITIES, timeout=20)
        companies_page.click(companies_page.locators.FIRST_SEARCHED)
        companies_page.click(companies_page.locators.VK_COMMUNITIES)
        companies_page.click(companies_page.locators.OK_COMMUNITIES)
        companies_page.click(companies_page.locators.FIRST_SEARCHED_OK)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)

        assert companies_page.get_text(companies_page.locators.COMMUNITY_COUNTER) == 'Выбрано 2 сообщества', 'Выбор сообщества не работает'

    @allure.title("communities delete chosen group test")
    def test_communities_delete(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.COMMUNITIES_INPUT)
        companies_page.enter_field(companies_page.locators.COMMUNITIES_INPUT, 'Профсоюз')
        companies_page.click(companies_page.locators.VK_COMMUNITIES, timeout=20)
        companies_page.click(companies_page.locators.FIRST_SEARCHED)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)

        companies_page.click(companies_page.locators.DELETE_GROUP)

        assert companies_page.is_element_not_present(companies_page.locators.SELECTED_GROUP), 'Удаление выбранной группы не работает'

    @allure.title("communities cancel test")
    def test_communities_cancel(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.move_to_element(companies_page.locators.COMMUNITIES_INPUT)
        companies_page.enter_field(companies_page.locators.COMMUNITIES_INPUT, 'Профсоюз')
        companies_page.click(companies_page.locators.VK_COMMUNITIES, timeout=20)
        companies_page.click(companies_page.locators.FIRST_SEARCHED)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)

        companies_page.click(companies_page.locators.CANCEL_BTN)

        assert companies_page.is_element_not_present(companies_page.locators.SELECTED_GROUP), 'Кнопка отмены не работает'

    @allure.title("communities delete all test")
    def test_communities_all(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)
        companies_page.enter_field(companies_page.locators.COMMUNITIES_INPUT, 'Профсоюз')
        companies_page.click(companies_page.locators.VK_COMMUNITIES, timeout=10)
        companies_page.click(companies_page.locators.FIRST_SEARCHED)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)

        companies_page.click(companies_page.locators.COMMUNITIES_DELETE_ALL)
        companies_page.click(companies_page.locators.COMMUNITIES_CONTAINER)

        assert companies_page.is_element_not_present(companies_page.locators.SELECTED_GROUP), 'Кнопка корзины не работает'

    @allure.title("musicians choose test")
    def test_musicians_choose(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.click(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_INPUT)
        companies_page.enter_field(companies_page.locators.MUSICIANS_INPUT,'Баста')
        companies_page.click(companies_page.locators.FIRST_MUSICIAN)
        companies_page.click(companies_page.locators.DONE_MUSICIANS_SEARCH)

        assert companies_page.get_text(companies_page.locators.SELECTED_MUSICIAN_COUNTER) == 'Выбран 1 музыкант', 'Выбор музыканта не работает'

    @allure.title("musicians delete chosen test")
    def test_musicians_delete_chosen(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.click(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_INPUT)
        companies_page.enter_field(companies_page.locators.MUSICIANS_INPUT, 'Баста')
        companies_page.click(companies_page.locators.FIRST_MUSICIAN)
        companies_page.click(companies_page.locators.DONE_MUSICIANS_SEARCH)

        companies_page.click(companies_page.locators.DELETE_SEARCHED_MUSICIAN)

        assert companies_page.is_element_not_present(companies_page.locators.SELECTED_MUSICIAN), 'Удаление музыканта не работает'

    @allure.title("musicians delete all test")
    def test_delete_all(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.click(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_INPUT)
        companies_page.enter_field(companies_page.locators.MUSICIANS_INPUT, 'Баста')
        companies_page.click(companies_page.locators.FIRST_MUSICIAN)
        companies_page.click(companies_page.locators.DONE_MUSICIANS_SEARCH)

        companies_page.click(companies_page.locators.MUSICIANS_DELETE_ALL)

        assert companies_page.is_element_not_present(
            companies_page.locators.SELECTED_MUSICIAN), 'Удаление всего не работает'

    @allure.title("musicians trash bean all test")
    def test_trash_bean(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.INTEREST_AND_BEHAVIOUR_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.click(companies_page.locators.MUSICIANS_CONTAINER)
        companies_page.move_to_element(companies_page.locators.MUSICIANS_INPUT)
        companies_page.enter_field(companies_page.locators.MUSICIANS_INPUT, 'Баста')
        companies_page.click(companies_page.locators.FIRST_MUSICIAN)
        companies_page.click(companies_page.locators.DONE_MUSICIANS_SEARCH)

        companies_page.click(companies_page.locators.MUSICIANS_TRASH_BEAN)

        companies_page.click(companies_page.locators.MUSICIANS_CONTAINER)

        assert companies_page.is_element_not_present(
            companies_page.locators.SELECTED_MUSICIAN), 'Корзина не работает'

    @allure.title("transfer to advertisement test")
    def test_transfer_to_advertisement(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.click(companies_page.locators.FAST_CHOICE_REGIONS)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)

        assert companies_page.find(companies_page.locators.ADVERTISEMENT_SETTINGS), 'Переход на этап объявления не произошёл'

    @allure.title("title input positive test")
    def test_title_in_positive(self, companies_page):
        companies_page.transfer_to_advertisement()
        companies_page.move_to_element(companies_page.locators.TITLE)
        companies_page.enter_field(companies_page.locators.TITLE, 'Тест')

        assert companies_page.get_text(companies_page.locators.TITLE) == 'Тест', 'Ввод заголовка заблокирован'

    @allure.title("short description input negative test")
    def test_short_description_in_positive(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.move_to_element(companies_page.locators.SHORT_DESCRIPTION)
        companies_page.enter_field(companies_page.locators.SHORT_DESCRIPTION, 'Тест')

        assert companies_page.get_text(companies_page.locators.SHORT_DESCRIPTION) == 'Тест', 'Ввод короткого описания заблокирован'

    @allure.title("About autocomplete test")
    def test_about_autocomplete(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.move_to_element(companies_page.locators.ABOUT)

        assert companies_page.get_text(companies_page.locators.ABOUT) != '', 'Автозаполнение не работает. Попробуйте сами создать и ввести ФИО и ИНН в форму'

    @allure.title("add media test")
    def test_add_media(self, companies_page):
        companies_page.transfer_to_advertisement()
        companies_page.move_to_element(companies_page.locators.MEDIAFILES_BUTTON)
        companies_page.click(companies_page.locators.MEDIAFILES_BUTTON)
        companies_page.find(companies_page.locators.MEDIA_PICTURE)
        companies_page.click(companies_page.locators.MEDIA_PICTURE)
        companies_page.click(companies_page.locators.ADD_PICTURES)

        assert companies_page.wait_for_clickable(companies_page.locators.IMAGES, timeout=20), 'Загрузка фотографии не работает. Возможно на аккаунте нет загруженных фотографий'

    @allure.title("complete advertisement test")
    def test_complete_advertisement(self, companies_page):
        companies_page.transfer_to_advertisement()
        companies_page.move_to_element(companies_page.locators.TITLE)
        companies_page.enter_field(companies_page.locators.TITLE, 'Тест')
        companies_page.move_to_element(companies_page.locators.SHORT_DESCRIPTION)
        companies_page.enter_field(companies_page.locators.SHORT_DESCRIPTION, 'Тест')
        companies_page.move_to_element(companies_page.locators.MEDIAFILES_BUTTON)
        companies_page.click(companies_page.locators.MEDIAFILES_BUTTON)
        companies_page.find(companies_page.locators.MEDIA_PICTURE)
        companies_page.click(companies_page.locators.MEDIA_PICTURE)
        companies_page.click(companies_page.locators.ADD_PICTURES)
        companies_page.move_to_element(companies_page.locators.ABOUT)
        text = companies_page.get_text(companies_page.locators.ABOUT)
        if text == '':
            companies_page.enter_field(companies_page.locators.ABOUT, 'Жидков Антон Алексеевич, ИНН 501818145478')

        company_name = companies_page.get_text(companies_page.locators.COMPANY_NAME_)
        companies_page.find(companies_page.locators.AI_IMAGE)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)

        companies_page.find(companies_page.locators.COMPANY_NAME, timeout=20)

        assert companies_page.get_text(companies_page.locators.COMPANY_NAME) == company_name, 'Кампания не создаётся'

        companies_page.click(companies_page.locators.SELECT_ALL, timeout=10)
        companies_page.click(companies_page.locators.ACTIONS)
        companies_page.click(companies_page.locators.DELETE_ACTION)

    @allure.title("duplicate company name test")
    def test_duplicate_company_name(self, companies_page):
        companies_page.create_company()
        current_company_name = companies_page.get_text(companies_page.locators.COMPANY_NAME)
        companies_page.move_to_element(companies_page.locators.COMPANY_OPTIONS)
        companies_page.click(companies_page.locators.COMPANY_DUPLICATE)
        companies_page.find(companies_page.locators.COMPANY_NAME_)

        assert companies_page.get_text(companies_page.locators.COMPANY_NAME_) != 'копия ' + current_company_name, 'Имя копии задаётся неверно'

        companies_page.delete_all_companies()

    @allure.title("duplicate company test")
    def test_duplicate_company(self, companies_page):
        companies_page.create_company()
        companies_page.move_to_element(companies_page.locators.COMPANY_OPTIONS)
        companies_page.move_to_element(companies_page.locators.COMPANY_DUPLICATE)
        companies_page.click(companies_page.locators.COMPANY_DUPLICATE)
        companies_page.find(companies_page.locators.COMPANY_NAME_)
        name = companies_page.get_text(companies_page.locators.COMPANY_NAME_)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.wait_for_clickable(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.wait_for_clickable(companies_page.locators.CONTINUE_BUTTON)
        companies_page.click(companies_page.locators.CONTINUE_BUTTON)
        companies_page.find(companies_page.locators.DUPLICATED_NAME,timeout=20)

        assert companies_page.get_text(companies_page.locators.DUPLICATED_NAME) != 'копия ' + name, 'Копия не создалась'

        companies_page.delete_all_companies()




















