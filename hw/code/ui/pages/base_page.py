import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

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

    def find_visibility(self, locator, timeout=20):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_located(self, locator, timeout=20):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator, timeout=20):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Wait for click')
    def wait_for_clickable(self, locator, timeout=5):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Click')
    def click(self, element, timeout=15) -> None:
        self.wait(timeout).until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Find and click')
    def find_and_click(self, locator, timeout=15) -> None:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('EnterField')
    def enter_field(self, elem, value) -> None:
        elem.send_keys(Keys.COMMAND + "a") # TODO поменять на control + a, если не на маке :)
        elem.send_keys(Keys.DELETE)
        elem.send_keys(value)

    @allure.step('Enter field element')
    def enter_field_element(self, element, value, timeout=20) -> None:
        WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
        element.clear()
        element.send_keys(value)


    @allure.step('GetText')
    def get_text(self, locator, timeout=20) -> str:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Get element text')
    def get_element_text(self, element, timeout=20) -> str:
        self.wait(timeout).until(EC.visibility_of(element))
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
                Проверяет, что элемента ВИДИМ на странице в течение указанного времени ожидания.
                :return: True, если элемент виден, False, если он невиден или его нет.
                """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
            return True  # Элемент видим
        except TimeoutException:
            return False  # Элемент невидим


    def element_presented(self, locator, timeout=20) -> bool:
        """
        Проверяет, что элемента ВИДИМ на странице в течение указанного времени ожидания.
        :return: True, если элемент виден, False, если он невиден или его нет.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True  # Элемент видим
        except TimeoutException:
            return False  # Элемент невидим

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def wait_elemnt_enabled(self, element, timeout=20) -> bool:
        WebDriverWait(self.driver, timeout).until(
            lambda d: not element.get_attribute('disabled')
        )
        return element

    def select_element(self, element, timeout=20):
        select = Select(element)
        return select