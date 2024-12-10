from hw.code.ui.locators.vk_ad_main_locators import AuthLocators
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.main_page import MainPage


class AuthPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = AuthLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def login_mail(self, email, password):
        self.click(AuthLocators.GO_TO_LK_BTN, 15)
        self.click(AuthLocators.GO_WITH_EMAIL_BTN, 15)
        self.enter_field(AuthLocators.EMAIL_ENTER_FIELD, email, 15)
        self.click(AuthLocators.ENTER_BTN, 15)
        self.click(AuthLocators.ENTER_OTHER_WAY_BTN, 15)
        self.enter_field(AuthLocators.PASSWORD_ENTER_FIELD, password, 15)
        self.click(AuthLocators.ENTER_PASSWORD_BTN, 15)
        return MainPage(self.driver)
