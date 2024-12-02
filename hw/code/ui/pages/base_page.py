import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    # login_locators = AuthPageLocators()  # не нужно
    url = 'https://ads.vk.com/'  # урл страницы, c которой начинаю

    def is_opened(self, url='', trunc=0, timeout=15):
        if url == '':
            url = self.url
        started = time.time()
        while time.time() - started < timeout:
            if trunc != 0:
                if self.driver.current_url[:trunc] == url:
                    return True
            else:
                if self.driver.current_url == url:
                    return True
        raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()


    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('EnterField')
    def enter_field(self, locator, value, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step('ClearEnterField')
    def clear_enter_field(self, locator, value, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step('EnterFieldReturn')
    def enter_field_return(self, locator, value, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    @allure.step('GetText')
    def get_text(self, locator, timeout=2) -> str:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('GetAttr')
    def get_attribute(self, locator, attribute, timeout=2) -> str:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    def move_to_element(self, locator):
        elem = self.find(locator)
        self.actions.move_to_element(elem).perform()

    def is_element_not_present(self, locator, timeout=2) -> bool:
        """
        Проверяет, что элемента НЕТ или он НЕВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент отсутствует или невидим, False, если он присутствует и видим.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True  # Элемент невидим или отсутствует
        except TimeoutException:
            return False  # Элемент видим

    def element_presented(self, locator, timeout=2) -> bool:
        """
        Проверяет, что элемента  ВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент виден, False, если он невиден или его нету.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True  # Элемент видим
        except TimeoutException:
            return False  # Элемент невидим