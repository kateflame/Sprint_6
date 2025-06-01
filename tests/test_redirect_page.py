import pytest
from selenium import webdriver
from pages.main_page import *
from pages.order_page import *
from data import *
from locators.main_page_locators import *
from locators.order_page_locators import *
import allure


@allure.title("Тест на проверку редиректа на тестовую страницу тренажера")
@allure.description(
    "Проверяем что происходит переход по клику на тестовую страницу тренажера"
)
class TestRedirectToMainPage:
    def test_redirect_logo_scooter(self, main_page, redirect_from_order_page):
        main_page.go_to_url(URL_ORDER_PAGE)
        redirect_from_order_page.redirect_test_url()
        text = main_page.get_bottom_order_button_text()
        assert text == "Заказать"


@allure.title("Тест на проверку редиректа на главную страницу Дзена")
@allure.description(
    "Проверяем что происходит переход по клику на лого яндекса на главную страницу Дзена"
)
class TestRedirectPage:
    def test_redirect_yandex_logo(self, main_page, redirect_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.click_button_for_redirect_page()
        text = redirect_page.redirect_to_dzen()
        assert text == "Новости"
