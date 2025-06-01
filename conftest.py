import pytest
from selenium import webdriver

from pages.main_page import *
from pages.order_page import *
from pages.redirect_page import *

from data import *


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page


@pytest.fixture
def redirect_page(driver):
    page = RedirectDzenUrl(driver)
    return page


@pytest.fixture
def redirect_from_order_page(driver):
    page = RedirectmainUrl(driver)
    return page
