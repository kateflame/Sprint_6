import pytest
from selenium import webdriver
from pages.main_page import *
from pages.order_page import *
from data import *
from locators.main_page_locators import *
from locators.order_page_locators import *
import allure


@allure.title("Тесты на проверку заказа")
@allure.description(
    "Проверяем что заказы оформлены успешно по клику и на верхнюю и на нижнюю кнопки Заказать"
)
class TestOrderPage:

    @pytest.mark.parametrize(
        "locator, data",
        [
            (MainPageLocators.TAKE_ORDER_BUTTON_TOP, user_data_1),
            (MainPageLocators.TAKE_ORDER_BUTTON_BOTTOM, user_data_2),
        ],
    )
    def test_create_order(self, main_page, order_page, locator, data):
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.accept_cookies()
        main_page.click_order_button(locator)
        order_page.set_order_part_one(data)
        success_order = order_page.set_order_part_two(data)
        assert success_order_phrase in success_order
