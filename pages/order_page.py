from data import *
from pages.base_page import *
from locators.main_page_locators import *
from locators.order_page_locators import *
import allure


# класс для страницы заказа самоката 'https://qa-scooter.praktikum-services.ru/order'
class OrderPage(BasePage):

    # нажать на поле Станция метро и выбрать нужную станцию
    def set_undergraund_station(self):
        self.click_to_element(OrderPageLocators.DROPDOWN_UNDERGROUND_STATION)
        self.find_element_with_wait(OrderPageLocators.DROPDOWN_MOSCOW_METRO)
        # Получаем все элементы списка станций метро
        stations = self.driver.find_elements(*OrderPageLocators.DROPDOWN_MOSCOW_METRO)
        # Выбираем случайную станцию
        random.choice(stations).click()

        # нажать на поле c datepicker

    def set_data_for_delivery(self):
        self.add_text_to_element(OrderPageLocators.INPUT_DATA, data_for_order)
        # кликаем в рандомное место, чтобы закрыть датапикер
        self.click_to_element(OrderPageLocators.TEXT_ABOUT_RENT)

        # нажать на поле Срок аренды

    def set_duration_for_rent(self):
        self.click_to_element(OrderPageLocators.DROPDOWN_DURATION_RENT)
        self.click_to_element(OrderPageLocators.THREE_DAY_RENT)

    @allure.step("Заполнена первая форма wizard заказа")
    def set_order_part_one(self, data):
        self.add_text_to_element(OrderPageLocators.INPUT_NAME, data["first_name"])
        self.add_text_to_element(OrderPageLocators.INPUT_LAST_NAME, data["last_name"])
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS, data["full_address"])
        self.set_undergraund_station()
        self.add_text_to_element(
            OrderPageLocators.INPUT_TELEPHONE, data["phone_number"]
        )
        self.click_to_element(OrderPageLocators.BUTTON_FURTHER)

    @allure.step("Заполнена вторая форма wizard заказа")
    def set_order_part_two(self, data):
        self.set_data_for_delivery()
        self.set_duration_for_rent()
        self.click_to_element(OrderPageLocators.INPUT_COLOR_FOR_SCOOTER_BLACK)
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_RENT, data["comment"])
        self.click_to_element(OrderPageLocators.BUTTON_TAKE_ORDER)
        # нажать на кнопку Да в модальном окне "Хотите оформить заказ?"
        self.click_to_element(OrderPageLocators.FIRST_MODAL_WINDOW)
        return self.get_text_from_element(OrderPageLocators.SUCCESS_MODAL_WINDOW)
