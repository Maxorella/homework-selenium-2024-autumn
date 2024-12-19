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
        companies_page.set_budget("100")
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

    # @allure.title("Тест стратегии ставок")
    # def test_strategy(self, companies_page):
    #     companies_page.create_new_company()
    #     companies_page.create_site_advertise()
    #     companies_page.insert_site_href("https://www.statista.com")
    #     companies_page.switch_strategy(1)
    #     time.sleep(30)
    #     companies_page.assert_strategy()

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
        companies_page.open_interest_and_behaviour()
        companies_page.open_interest()
        companies_page.choose_first_interest()

        companies_page.assert_interest_input()

    @allure.title("Удаление выбранной категории")
    def test_interest_delete(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.delete_interest()

        companies_page.assert_interest_delete()

    # На английском для саджестов
    @allure.title("Exclude interest test")
    def test_interest_exclude(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_interest()
        companies_page.exclude_first_interest()

        companies_page.assert_interest_input()

    @allure.title("interest and exclude interest conflict test")
    def test_interest_conflict(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.exclude_first_interest()
        companies_page.transfer_to_next_step()

        companies_page.assert_interest_error()

    @allure.title("delete interest test")
    def test_interest_delete_exclude(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_interest()
        companies_page.choose_first_interest()
        companies_page.exclude_first_interest()

        companies_page.delete_all_interest()
        companies_page.open_interest_with_plus()
        companies_page.assert_all_interest_deleted()

    @allure.title("key phrases suggest test")
    def test_keyphrases_suggest(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()
        companies_page.insert_key_phases('Авто')

        companies_page.assert_key_phrases_suggest()

    @allure.title("minus phrases test")
    def test_minus_phrases(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()

        companies_page.insert_minus_phrases('Авто')

        companies_page.assert_minus_phrases_input()

    @allure.title("phrases conflict test")
    def test_phrases_conflict(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()
        companies_page.insert_key_phases('Авто')
        companies_page.insert_minus_phrases('Авто')

        companies_page.assert_phrases_conflict()

    @allure.title("search period input test")
    def test_search_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()

        companies_page.insert_search_period("300")

        companies_page.assert_search_period_input()

    @allure.title("enter big period test")
    def test_enter_big_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()

        companies_page.insert_search_period("50")
        companies_page.confirm_search_period()

        companies_page.assert_big_search_period()

    @allure.title("enter zero period test")
    def test_enter_zero_period(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()

        companies_page.insert_search_period("0")
        companies_page.confirm_search_period()

        companies_page.assert_zero_search_period()

    @allure.title("delete key phrases test")
    def test_delete_key_phrases(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_key_phrases()

        companies_page.insert_search_period("15")
        companies_page.confirm_search_period()
        companies_page.delete_key_phrases()

        companies_page.open_hey_phrases_with_animation()

        companies_page.assert_key_phrases_deleted()

    @allure.title("communities choose test")
    def test_communities_choose(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_communities()

        companies_page.insert_community_search('Профсоюз')
        companies_page.choose_first_vk_community()
        companies_page.choose_first_ok_community()
        companies_page.open_communities()

        companies_page.assert_choose_communities()

    @allure.title("communities delete chosen group test")
    def test_communities_delete(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_communities()

        companies_page.insert_community_search('Профсоюз')
        companies_page.choose_first_vk_community()
        companies_page.open_communities()

        companies_page.delete_chosen_community()

        companies_page.assert_delete_community()

    @allure.title("communities cancel test")
    def test_communities_cancel(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_communities()

        companies_page.insert_community_search('Профсоюз')
        companies_page.choose_first_vk_community()
        companies_page.open_communities()

        companies_page.cancel_communities()

        companies_page.assert_cancel_communities()

    @allure.title("communities delete all test")
    def test_communities_all(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_communities()

        companies_page.insert_community_search('Профсоюз')
        companies_page.choose_first_vk_community()
        companies_page.open_communities()

        companies_page.delete_communities()
        companies_page.open_communities_with_plus()

        companies_page.assert_delete_communities()

    @allure.title("musicians choose test")
    def test_musicians_choose(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_musicians()

        companies_page.insert_musicians_search('Баста')

        companies_page.choose_first_musician()

        companies_page.assert_choose_musician()

    @allure.title("musicians delete chosen test")
    def test_musicians_delete_chosen(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_musicians()

        companies_page.insert_musicians_search('Баста')

        companies_page.choose_first_musician()
        companies_page.delete_chosen_musician()

        companies_page.assert_delete_musician()

    @allure.title("musicians delete all test")
    def test_delete_all(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_musicians()

        companies_page.insert_musicians_search('Баста')

        companies_page.choose_first_musician()
        companies_page.delete_all_musicians()

        companies_page.assert_delete_all_musician()

    @allure.title("musicians trash bean all test")
    def test_trash_bean(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.open_interest_and_behaviour()
        companies_page.open_musicians()

        companies_page.insert_musicians_search('Баста')

        companies_page.choose_first_musician()
        companies_page.delete_trash_bean_musician()
        companies_page.open_musicians_with_plus()

        companies_page.assert_delete_trash_bean()

    @allure.title("transfer to advertisement test")
    def test_transfer_to_advertisement(self, companies_page):
        companies_page.transfer_to_group_advertise()
        companies_page.fast_choice_moscow()
        companies_page.transfer_to_next_step()

        companies_page.assert_transfer_to_advertisement()

    @allure.title("title input positive test")
    def test_title_in_positive(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.insert_title('Тест')

        companies_page.assert_title_input()

    @allure.title("short description input negative test")
    def test_short_description_in_positive(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.insert_short_description('Тест')

        companies_page.assert_description_input()

    @allure.title("About test")
    def test_about_autocomplete(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.insert_about('Иванов Иван Иванович, ИНН 501818145478')

        companies_page.assert_about_input()


    @allure.title("add media test")
    def test_add_media(self, companies_page):
        companies_page.transfer_to_advertisement()

        companies_page.insert_media()

        companies_page.assert_add_media()

    @allure.title("complete advertisement test")
    def test_complete_advertisement(self, companies_page):
        companies_page.transfer_to_advertisement()
        companies_page.insert_title('Тест')
        companies_page.insert_short_description('Тест')
        companies_page.insert_media()
        companies_page.insert_about('Иванов Иван Иванович, ИНН 501818145478')

        companies_page.save_company_name()
        companies_page.wait_video_loaded()
        companies_page.transfer_to_next_step()

        companies_page.assert_complete_advertisement()

        companies_page.delete_companies()

    @allure.title("duplicate company name test")
    def test_duplicate_company_name(self, companies_page):
        companies_page.create_company()

        companies_page.duplicate_company()

        companies_page.assert_duplicated_company_name()

        companies_page.go_to_base_page()
        companies_page.go_to_companies()

        companies_page.delete_companies()

    @allure.title("duplicate company test")
    def test_duplicate_company(self, companies_page):
        companies_page.create_company()
        companies_page.duplicate_company()

        companies_page.full_duplicate()

        companies_page.go_to_companies()

        companies_page.assert_duplicated_company()

        companies_page.delete_companies()




















