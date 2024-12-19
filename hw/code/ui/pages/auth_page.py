from hw.code.ui.locators.companiesLocator import CompaniesLocator
from hw.code.ui.locators.vk_ad_main_locators import AuthLocators
from hw.code.ui.pages.auditory_page import AuditoryPage
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.companies_page import CompaniesPage
from hw.code.ui.pages.main_page import MainPage
from hw.code.ui.pages.pixel_page import PixelPage


class AuthPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = AuthLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def login(self, email, password):
        go_to_lk_btn = self.find_visibility(AuthLocators.GO_TO_LK_BTN)
        self.click(go_to_lk_btn, 15)

        go_mail_btn = self.find_visibility(AuthLocators.GO_WITH_EMAIL_BTN)

        self.click(go_mail_btn, 15)

        email_field = self.find_visibility(AuthLocators.EMAIL_ENTER_FIELD)

        self.enter_field(email_field, email)

        enter_btn = self.find_visibility(AuthLocators.ENTER_BTN)
        self.click(enter_btn)

        other_way_btn = self.find_visibility(AuthLocators.ENTER_OTHER_WAY_BTN)
        self.click(other_way_btn)

        password_field = self.find_visibility(AuthLocators.PASSWORD_ENTER_FIELD)
        self.enter_field(password_field, password)

        enter_password_btn = self.find_visibility(AuthLocators.ENTER_PASSWORD_BTN)
        self.click(enter_password_btn)

    def login_mail(self, email, password):
        self.login(email, password)
        return MainPage(self.driver)

    def login_pixels(self, email, password):
        self.login(email, password)
        go_to_pixel_btn = self.find_visibility(AuthLocators.GO_TO_PIXEL_BTN)
        self.click(go_to_pixel_btn)
        return PixelPage(self.driver)

    def login_auditory(self, email, password):
        self.login(email, password)
        go_to_aud_btn = self.find_visibility(AuthLocators.GO_TO_AUDITORY_BTN)
        self.click(go_to_aud_btn)
        return AuditoryPage(self.driver)

    def go_to_companies(self, email, password):
        self.login(email, password)
        self.click(AuthLocators.COMPANIES_PAGE, timeout=60)
        self.click(AuthLocators.COMPANIES_PAGE)
        self.find(CompaniesLocator.CREATE_NEW_COMPANY)

        return CompaniesPage(self.driver)

