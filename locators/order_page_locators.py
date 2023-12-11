from selenium.webdriver.common.by import By

class OrderPageLocators:
    LOCATOR_SCOOTER_FOR_WHO_TEXT = (By.XPATH, "//*[text()='Для кого самокат']")

    LOCATOR_INPUT_NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]") # поле "Имя"
    LOCATOR_INPUT_SURNAME = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]") # поле "Фамилия"
    LOCATOR_INPUT_ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]") # поле "Адрес"
    LOCATOR_INPUT_STATION = (By.XPATH, "//input[contains(@placeholder, 'Станция')]") # поле "Станция"
    LOCATOR_INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]") # поле "Телефон"

    LOCATOR_BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']") # поле "Далее"
    LOCATOR_ARENDA_TEXT = (By.XPATH, "//*[text()='Про аренду']") # заголовок страницы "Про аренду"

    LOCATOR_INPUT_WHEN = (By.XPATH, "//input[contains(@placeholder, 'Когда')]") # поле "Когда"
    LOCATOR_INPUT_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder") # поле "Период"
    LOCATOR_INPUT_COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]") # поле "Комментарий"

    LOCATOR_WANT_TO_PLACE_ORDER_TEXT = (By.XPATH, "//*[text()='Хотите оформить заказ?']") # заголовок модального окна "Хотите оформить заказ?"

    LOCATOR_BUTTON_ORDER = (By.XPATH, "(//button[text()='Заказать'])[2]")
    LOCATOR_BUTTON_YES = (By.XPATH, "//button[text()='Да']") # кнопка "Да"

    LOCATOR_ORDER_NUMBER = (By.XPATH, "//*[text()='Номер заказа']")

    def get_station_locator(self, station):
        return (By.XPATH, "//*[text()='" + station + "']")

    def get_when_locator(self, when):
        return (By.XPATH, "//div[@aria-label='" + when + "']")

    def get_period_locator(self, period):
        return (By.XPATH, "//*[text()='" + period + "']")

    def get_color_locator(self, color):
        return (By.XPATH, "//label[text()='" + color + "']")

