from hw.code.ui.locators.AuditoryLocators import AuditoryLocators
from hw.code.ui.pages.base_page import BasePage


class AuditoryPage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AuditoryLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def click_create_auditory(self):
        self.click(self.locators.CREATE_AUDITORY_BUTTON)

    def enter_auditory_name(self, auditory_name):
        self.enter_field(self.locators.AUDITORY_NAME_INPUT, auditory_name)

    def click_add_ist(self):
        self.click(self.locators.ADD_IST_BTN)

    def click_add_soobs_subsc(self):
        self.click(self.locators.SOOBS_SUBSC_BTN)

    def click_add_as_list(self):
        self.click(self.locators.ADD_AS_LIST_BTN)

    def click_soobs(self):
        self.click(self.locators.VK_SOOBS_BTN)

    def enter_soobs_href(self, soobs_href):
        self.enter_field(self.locators.TEXT_AREA, soobs_href)

    def click_confr_add(self):
        self.click(self.locators.ADD_BTN)

    def click_close_krest(self):
        self.click(self.locators.CLOSE_BTN)

    def click_save(self):
        self.click(self.locators.SAVE_BTN)

    def click_submit_create(self):
        self.click(self.locators.SUBMIT_CREATE_BTN)

    def assert_lmao_span(self):
        pass
        #self.click(self.locators.SUBMIT_CREATE_BTN)