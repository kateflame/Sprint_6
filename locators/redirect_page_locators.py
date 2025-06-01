from selenium.webdriver.common.by import By





class MainRedirectLocatorsDzen:
    YANDEX_SEARCH = [
        By.XPATH,
        '//div[@data-testid="floor-title-text" and contains(text(), "Новости")]',
    ]
