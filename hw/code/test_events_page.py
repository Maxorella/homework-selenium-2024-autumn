import allure
from selenium.webdriver.common.by import By

from hw.code.events_case_vk import EventsCaseVkAd
from hw.code.ui.locators.vk_ad_events_locators import EventsLocators


@allure.story("Events page")
class TestEventsCaseVkAd(EventsCaseVkAd):
    @allure.title("Events view page Test")
    def test_events_page(self):

        assert self.events_page.find(EventsLocators.EVENTS_HEADER).is_displayed(), "Заголовок не отображается"

    @allure.title("upcoming view test")
    def test_upcoming_events_page(self):

        assert self.events_page.find(EventsLocators.UPCOMING_CONTAINER).is_displayed(), "Предстоящие события не отображаются"

    @allure.title('past view test')
    def test_past_events_page(self):

        assert self.events_page.find(EventsLocators.PAST_CONTAINER).is_displayed(), "Прошедшие события не отображаются"

    @allure.title("Click upcoming test")
    def test_click_upcoming_events_page(self):

        self.events_page.click(EventsLocators.CLOSE_NOTIFICATION)

        title = self.events_page.get_text(EventsLocators.MAIN_EVENT_TITLE)
        self.events_page.move_to_element(EventsLocators.MAIN_EVENT_HREF)
        self.events_page.click(EventsLocators.MAIN_EVENT_HREF)
        self.events_page.move_to_element(EventsLocators.EVENT_TITLE)
        new_title = self.events_page.get_text(EventsLocators.EVENT_TITLE)

        assert title == new_title, "Перешли не на то мероприятие"
