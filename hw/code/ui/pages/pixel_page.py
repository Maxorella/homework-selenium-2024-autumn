from hw.code.ui.locators.PixelLocators import PixelLocators
from hw.code.ui.pages.base_page import BasePage




class PixelPage(BasePage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = PixelLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def click_create_pix(self):
        self.click(self.locators.CREATE_PIX_NOPIX_BTN)

    def enter_pixel_name(self, pixel_name: str):
        self.enter_field(self.locators.DOMEN_INPUT, pixel_name)

    def click_create_window_pix(self):
        self.click(self.locators.ADD_PIXEL_BTN)

    def click_create_new_pix(self):
        self.click(self.locators.CHOICE_CREATE_NEW_PIX_BTN)

    def click_close_created(self):
        self.click(self.locators.CLOSE_CREATED_BTN)

    def assert_created_url(self, pixel_url: str):
        assert self.get_text(self.locators.CREATED_PIX_URL) == pixel_url

    def click_3_point(self):
        self.click_move(self.locators.POINT_3_BTN)

    def click_delete_dropped(self):
        self.click(self.locators.DELETE_DROPPED_BTN)

    def click_submit_delete(self):
        self.click(self.locators.SUBMIT_DELETE_BTN)

    def assert_deleted_pixel(self):
        assert self.get_text(self.locators.TITLE_NO_PIX) == "Нет привязанных пикселей трекинга"

    # 5 тест
    def click_go_pixel_settings(self):
        self.click(self.locators.AUDITORY_TAGS_BTN)

    def click_create_tag(self):
        self.click(self.locators.CREATE_AUDITORY_TAG_BTN)

    def enter_tag_name(self, tag_name: str):
        self.enter_field(self.locators.DOMEN_INPUT, tag_name)

    def click_submit_create_tag(self):
        self.click(self.locators.SUBMIT_CREATE_BTN)

    def assert_created_auditory(self, expected_title):
        assert self.get_text(self.locators.TAG_NAME_CREATED_AUDITORY) == expected_title
