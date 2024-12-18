from hw.code.ui.locators.PixelLocators import PixelLocators
from hw.code.ui.pages.base_page import BasePage


class PixelPage(BasePage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = PixelLocators()
    create_pix_btn = None
    url_field = None
    pixel_add_btn = None
    pixel_new_option_btn = None
    close_crest_btn = None
    created_url_in_list = None
    point_3_btn = None
    edit_name_btn = None
    name_input = None
    submit_btn = None
    pix_title = None
    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def find_create_pix_btn(self):
        self.create_pix_btn = self.find(self.locators.CREATE_PIX_NOPIX_BTN)

    def click_create_pix(self):
        self.click(self.create_pix_btn)

    def find_url_field(self):
        self.url_field = self.find(self.locators.DOMEN_INPUT)

    def enter_pixel_name(self, pixel_name: str):
        self.enter_field(self.url_field, pixel_name)

    def find_pixel_add_btn(self):
        self.pixel_add_btn = self.find(self.locators.ADD_PIXEL_BTN)

    def click_create_window_pix(self):
        self.click(self.pixel_add_btn)

    def find_create_option_new_pix(self):
        self.pixel_new_option_btn = self.find(self.locators.CHOICE_CREATE_NEW_PIX_BTN)

    def click_create_option_new_pix(self):
        self.click(self.pixel_new_option_btn)

    def find_close_crest(self):
        self.close_crest_btn = self.find(self.locators.CLOSE_CREATED_BTN)

    def click_close_created(self):
        self.click(self.close_crest_btn)

    def find_created_url_inlist(self):
        self.created_url_in_list = self.find_visibility(self.locators.CREATED_PIX_URL)

    def assert_created_url(self, pixel_url: str):
        assert self.get_element_text(self.created_url_in_list) == pixel_url

    # меню три точки

    def find_3_point_and_move(self):
        body = self.find_visibility(self.locators.SPIS_BODY_DIV)
        self.move_to_element(body)
        self.point_3_btn = self.find_located(self.locators.POINT_3_BTN)

    def click_3_point(self):
        self.click(self.point_3_btn)

    # 3 тест

    def find_edit_name_dropped(self):
        self.edit_name_btn = self.find_clickable(self.locators.EDIT_NAME_DROPPED_BTN)

    def click_edit_name_dropped(self):
        self.click(self.edit_name_btn)

    def find_new_name_input(self):
        self.name_input = self.find_visibility(self.locators.EDIT_NAME_INPUT)

    def find_submit_edit_btn(self):
        self.submit_btn = self.find_clickable(self.locators.EDIT_SUBMIT_BTN)

    def enter_new_title(self, new_title: str):
        self.enter_field(self.name_input, new_title)

    def click_submit_edit_name(self):
        self.click(self.submit_btn)

    def find_pix_title(self):
        self.pix_title = self.find_visibility(self.locators.PIXEL_TITLE)

    def assert_new_title(self, expected_title: str):
        assert self.get_text(self.locators.PIXEL_TITLE) == expected_title





    def click_delete_dropped(self):
        self.click(self.locators.DELETE_DROPPED_BTN)

    def click_submit_delete(self):
        self.click(self.locators.SUBMIT_DELETE_BTN)

    def assert_deleted_pixel(self):
        assert self.get_text(self.locators.TITLE_NO_PIX) == "Нет привязанных пикселей трекинга"

    # 5 тест
    def click_settings(self):
        self.click(self.locators.SETTINGS_BTN)

    def click_aud_tags(self):
        self.click(self.locators.AUDITORY_TAGS_BTN)

    def click_create_tag(self):
        self.click(self.locators.CREATE_AUDITORY_TAG_BTN)

    def enter_tag_name(self, tag_name: str):
        self.move_to_element(self.locators.DOMEN_INPUT)
        self.enter_field(self.locators.DOMEN_INPUT, tag_name)

    def click_submit_create_tag(self):
        self.click(self.locators.SUBMIT_CREATE_BTN)

    def assert_created_auditory(self, expected_title):
        assert self.get_text(self.locators.TAG_NAME_CREATED_AUDITORY) == expected_title

