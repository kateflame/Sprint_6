from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import *


# описание базовых методов для всех страниц
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    # перейти на необходмиый url
    def go_to_url(self, url):
        self.driver.get(url)

    # найти элемент на странице и вернуть его
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # скролить до элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)

        self.driver.execute_script(
            """
                arguments[0].scrollIntoView({
                    behavior: 'instant',
                    block: 'start'
                });
            """,
            element,
        )

    # кликнуть на элемент
    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # добавить текст в поле
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # получить текс из элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # форматировать локатор
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    # переключение на новую вкладку
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
