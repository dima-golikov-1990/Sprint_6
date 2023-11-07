import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    @allure.step('Проверить, что первая страница заказа открылась')
    def order_page_one_is_opened(self):
        locator = OrderPageLocators()
        return self.element_is_visible(locator.LOCATOR_SCOOTER_FOR_WHO_TEXT)

    @allure.step('Ввести имя')
    def enter_name(self, name):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_NAME).send_keys(name)

    @allure.step('Ввести фамилию')
    def enter_surname(self, surname):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_SURNAME).send_keys(surname)

    @allure.step('Ввести адрес')
    def enter_address(self, address):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбрать станцию')
    def select_station(self, station):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_STATION).click()
        self.element_is_visible(locator.get_station_locator(station)).click()

    @allure.step('Ввести телефон')
    def enter_phone(self, phone):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_PHONE).send_keys(phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_BUTTON_NEXT).click()

    @allure.step('Проверить, что вторая страница заказа открылась')
    def order_page_two_is_opened(self):
        locator = OrderPageLocators()
        return self.element_is_visible(locator.LOCATOR_ARENDA_TEXT)

    @allure.step('Ввести дату')
    def enter_when(self, when):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_WHEN).send_keys(when)
        self.find_element(locator.LOCATOR_INPUT_WHEN).send_keys(Keys.ENTER)

    @allure.step('Выбрать период')
    def select_period(self, period):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_PERIOD).click()
        self.element_is_visible(locator.get_period_locator(period)).click()

    @allure.step('Выбрать цвет')
    def select_color(self, color):
        locator = OrderPageLocators()
        self.find_element(locator.get_color_locator(color)).click()

    @allure.step('Ввести комментарий')
    def enter_comment(self, comment):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_INPUT_COMMENT).send_keys(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_button_order(self):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_BUTTON_ORDER).click()

    @allure.step('Проверить, что модальное окно открылось')
    def modal_window_is_visible(self):
        locator = OrderPageLocators()
        self.element_is_visible(locator.LOCATOR_WANT_TO_PLACE_ORDER_TEXT)

    @allure.step('Нажать кнопку "Да"')
    def click_button_yes(self):
        locator = OrderPageLocators()
        self.find_element(locator.LOCATOR_BUTTON_YES).click()