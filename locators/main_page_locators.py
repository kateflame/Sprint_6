from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIES = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR = (By.ID, "accordion__panel-{}")
    QUESTION_LOCATOR_TO_SCROLL = (By.ID, "accordion__heading-7")

    TAKE_ORDER_BUTTON_TOP = [By.XPATH, "//button[contains(text(), 'Заказать')]"]
    TAKE_ORDER_BUTTON_BOTTOM = [
        By.XPATH,
        '//div[@class ="Home_FinishButton__1_cWm"]/button[@class ="Button_Button__ra12g Button_Middle__1CSJM"]',
    ]

    YANDEX_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    SCOOTER_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
