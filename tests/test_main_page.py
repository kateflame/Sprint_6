import pytest
import allure
from locators.main_page_locators import MainPageLocators
from data import *
from pages.main_page import MainPage

# класс с автотестом


@allure.title("Тесты на проверку вопросов")
@allure.description("Проверем что правильно получены ответы на вопросы")
class TestMainPage:
    @pytest.mark.parametrize("num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_and_answer(self, main_page, num):
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.accept_cookies()
        assert main_page.check_question_and_answer(num) == answer_data[num]
