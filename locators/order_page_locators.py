from selenium.webdriver.common.by import By


class OrderPageLocators:

    INPUT_NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    INPUT_ADDRESS = (
        By.XPATH,
        "//input[@placeholder = '* Адрес: куда привезти заказ']",
    )
    DROPDOWN_UNDERGROUND_STATION = (By.CLASS_NAME, "select-search__input")

    DROPDOWN_MOSCOW_METRO = (
        By.XPATH,
        "//li[@role='menuitem']",
    )
    INPUT_TELEPHONE = (
        By.XPATH,
        "//input[@placeholder = '* Телефон: на него позвонит курьер']",
    )
    BUTTON_FURTHER = (By.XPATH, "//button[contains(text(), 'Далее')]")

    TEXT_ABOUT_RENT = (By.CLASS_NAME, "Order_Header__BZXOb")

    INPUT_DATA = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    DATAPICKER_FOR_RENT = (By.CLASS_NAME, "react-datepicker__month")
    DROPDOWN_DURATION_RENT = (
        By.XPATH,
        "//div[@class = 'Dropdown-placeholder' and '* Срок аренды']",
    )

    THREE_DAY_RENT = (By.XPATH, "//div[contains(text(), 'трое суток')]")

    # для черного самоката
    INPUT_COLOR_FOR_SCOOTER_BLACK = (By.ID, "black")

    # коммент для курьера

    COMMENT_FOR_RENT = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")
    # кнопка Заказать

    BUTTON_TAKE_ORDER = (
        By.XPATH,
        "//button[text()='Заказать' and contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]",
    )
    # первое модальное окно, кнопка ДА

    FIRST_MODAL_WINDOW = (
        By.XPATH,
        "//button[text()='Да' and contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]",
    )
    # модальное окно с информацией об успешном заказе

    SUCCESS_MODAL_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    TEXT_SUCCESS_ORDER = (By.CLASS_NAME, "Order_Text__2broi")

    BUTTON_SHOW_ORDER_STATUS = (
        By.XPATH,
        "//button[contains(text(), 'Посмотреть статус')]",
    )
