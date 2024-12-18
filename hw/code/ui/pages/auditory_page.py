import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from hw.code.ui.locators.AuditoryLocators import AuditoryLocators
from hw.code.ui.pages.base_page import BasePage


class AuditoryPage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AuditoryLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    # 1 тест
    def find_create_aud_btn(self):
        self.create_aud_btn = self.find_clickable(self.locators.CREATE_AUDITORY_BUTTON)

    def click_create_auditory(self):
        self.click(self.create_aud_btn)

    def find_add_ist_btn(self):
        self.add_ist_btn = self.find_clickable(self.locators.ADD_IST_BTN)

    def click_add_ist_btn(self):
        self.click(self.add_ist_btn)

    def find_phrases_btn(self):
        self.phrases_btn = self.find_clickable(self.locators.PHRASES_OPTION)

    def click_phrases_btn(self):
        self.click(self.phrases_btn)

    def find_create_phrase_window_elements(self):
        self.input_title = self.find_visibility(self.locators.PHRASES_TITLE_INPUT)
        self.input_phrases = self.find_visibility(self.locators.PHRASES_PLUS_INPUT)
        self.save_phrase_btn = self.find_visibility(self.locators.SAVE_BTN)



    def enter_auditory_name(self, auditory_name):
        self.enter_field_element(self.input_title, auditory_name)

    def enter_phrase(self, phrase):
        self.enter_field_element(self.input_phrases, phrase)

    def click_save_phrase_btn(self):
        self.click(self.save_phrase_btn)

    # общая для разных созданий
    def find_save_aud_button(self):
        self.save_aud_btn = self.find_clickable(self.locators.SAVE_2_BTN)

    def click_save_aud_btn(self):
        self.wait().until(EC.invisibility_of_element_located(self.save_phrase_btn))
        self.click(self.save_aud_btn)

    def go_to_edit_page(self):
        h5_title = self.find_clickable(self.locators.AUD_TITLE_H5)
        h5_title.click()

    def find_edit_page_labels(self):
        self.phrases_label = self.find_visibility(self.locators.PHRASE_IN_EDIT)
        self.title_edit = self.find_visibility(self.locators.TITLE_IN_EDIT)

    def assert_edit_titles(self, phrase_in_edit, title_in_edit):
        assert self.get_element_text(self.phrases_label) == phrase_in_edit
        assert self.get_element_text(self.title_edit) == title_in_edit
        self.find_and_click(self.locators.CANCEL_EDIT_BTN)

    # удаление аудитории

    def delete_auditory(self):
        self.aud_in_list = self.find_located(self.locators.AUD_IN_LIST)
        self.point_3 = self.find_located(self.locators.POINT_3)

        self.move_to_element(self.aud_in_list)
        self.move_to_element(self.point_3)
        self.click(self.point_3)

        self.delete_dropped_btn = self.find_located(self.locators.DELETE_DROPPED_BTN)
        self.click(self.delete_dropped_btn)

        self.find_and_click(self.locators.DELETE_SUBMIT_BTN)
    # 2 тест


    def click_add_ist(self):
        self.click(self.locators.ADD_IST_BTN)



    #
    def click_add_soobs_subsc(self):
        self.click(self.locators.SOOBS_SUBSC_BTN)

    def click_add_as_list(self):
        self.click(self.locators.ADD_AS_LIST_BTN)

    def click_soobs(self):
        self.click(self.locators.VK_SOOBS_BTN)

    def enter_soobs_href(self, soobs_href):
        self.enter_field(self.locators.TEXT_AREA, soobs_href, 15)

    def click_confr_add(self):
        self.click(self.locators.ADD_BTN)

    def click_close_krest(self):
        self.click(self.locators.CLOSE_BTN)

    def click_save(self):
        self.click(self.locators.SAVE_BTN)

    def click_submit_create(self):
        self.click(self.locators.SUBMIT_CREATE_BTN)

    def assert_lmao_span(self, expected_title):
        assert expected_title == self.get_text(self.locators.LMAO_SPAN)