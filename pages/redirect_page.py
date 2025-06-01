from pages.base_page import *
from pages.order_page import *
from locators.main_page_locators import *
from locators.order_page_locators import *
from locators.redirect_page_locators import *


from data import *

# проверить клик на яндек ведет на сайт тестового тренажера


class RedirectmainUrl(BasePage):
    def redirect_test_url(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)


class RedirectDzenUrl(BasePage):

    # проверить клик на яндек ведет на сайт дзена
    def redirect_to_dzen(self):
        # переклчение на новую вкладку
        self.switch_to_new_window()
        # проверка
        text = self.get_text_from_element(MainRedirectLocatorsDzen.YANDEX_SEARCH)
        return text
