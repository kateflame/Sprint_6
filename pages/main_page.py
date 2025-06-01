import allure
from locators.main_page_locators import *
from pages.base_page import *
from data import *
import time


# класс для главной страницы 'https://qa-scooter.praktikum-services.ru/'
class MainPage(BasePage):
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIES)

    @allure.step("Клик на вопрос")
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num
        )
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step("Получение ответа на вопрос")
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Проверяем ответ")
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    def click_order_button(self, locator):
        self.click_to_element(locator)

    def click_button_for_redirect_page(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)

    def get_bottom_order_button_text(self):
        return self.get_text_from_element(MainPageLocators.TAKE_ORDER_BUTTON_BOTTOM)
