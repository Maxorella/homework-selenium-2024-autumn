import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageNotOpenedException(Exception):
    pass


class BasePage(object):

    url = 'https://ads.vk.com/'  # урл страницы, c которой начинаю

    def is_opened(self, timeout=15):

        url = self.url
        trunc = len(url)
        started = time.time()
        while time.time() - started < timeout:
            if trunc != 0:
                if self.driver.current_url[:trunc] == url:
                    return True
            else:
                if self.driver.current_url == url:
                    return True
        raise PageNotOpenedException(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def refresh_page(self):
        self.driver.refresh()
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=20):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_presence(self, locator, timeout=20):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Wait for click')
    def wait_for_clickable(self, locator, timeout=5):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()


    @allure.step('Click')
    def click(self, element, timeout=15) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(element))
        elem.click()

    @allure.step('Find and click')
    def find_and_click(self, locator, timeout=15) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('EnterField')
    def enter_field(self, locator, value, timeout=20) -> WebElement:
        elem = self.find_presence(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step('Enter field element')
    def enter_field_element(self, element, value, timeout=20) -> WebElement:
        WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
        element.clear()
        element.send_keys(value)

    @allure.step('ClearEnterField')
    def clear_enter_field(self, locator, value, timeout=20) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step('EnterFieldReturn')
    def enter_field_return(self, locator, value, timeout=20) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    @allure.step('GetText')
    def get_text(self, locator, timeout=20) -> str:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Get element text')
    def get_element_text(self, element, timeout=20) -> str:
        self.wait(timeout).until(EC.visibility_of(element))
        return element.text

    @allure.step('GetText')
    def get_text_visible(self, locator, timeout=20) -> str:
        self.wait(timeout).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text


    @allure.step('GetAttr')
    def get_attribute(self, locator, attribute, timeout=20) -> str:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    @allure.step('GetElAttr')
    def get_element_attribute(self, element, attribute, timeout=20) -> str:
        return element.get_attribute(attribute)

    def is_not_present(self, locator, timeout=20) -> bool:
        """
        Проверяет, что элемента НЕТ или он НЕВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент отсутствует или невидим, False, если он присутствует и видим.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True  # Элемент невидим или отсутствует
        except TimeoutException:
            return False  # Элемент видим

    def is_element_not_present(self, element, timeout=20) -> bool:
        """
        Проверяет, что элемента НЕТ или он НЕВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент отсутствует или невидим, False, если он присутствует и видим.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(element))
            return True  # Элемент невидим или отсутствует
        except TimeoutException:
            return False  # Элемент видим

    def is_element_visible(self, element, timeout=20) -> bool:
        """
                Проверяет, что элемента  ВИДИМ на странице в течение указанного времени ожидания.
                :return: True, если элемент виден, False, если он невиден или его нету.
                """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
            return True  # Элемент видим
        except TimeoutException:
            return False  # Элемент невидим


    def element_presented(self, locator, timeout=20) -> bool:
        """
        Проверяет, что элемента  ВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент виден, False, если он невиден или его нету.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True  # Элемент видим
        except TimeoutException:
            return False  # Элемент невидим

    @allure.step('MoveClick')
    def click_move(self, button):
        action = ActionChains(self.driver)
        action.move_to_element(button).click(button).perform()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()