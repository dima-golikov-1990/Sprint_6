import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    locator = MainPageLocators()

    @allure.step('Нажать на вопрос')
    def click_question(self, question_text):
        question = self.find_element(self.locator.get_accordeon_locator(question_text))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Проверить, что панель с ответом отображается')
    def panel_text_is_visible(self, panel_text):
        return self.element_is_visible(self.locator.get_panel_locator(panel_text))

    @allure.step('Взять текст с панели')
    def get_panel_text(self, panel_text):
        return self.find_element(self.locator.get_panel_locator(panel_text)).text

    @allure.step('Проверить, что лого "Яндекс" отображается')
    def yandex_logo_is_visible(self):
        return self.element_is_visible(self.locator.LOCATOR_YANDEX_LOGO)

    @allure.step('Проверить, что лого "Самокат" отображается')
    def scooter_logo_is_visible(self):
        return self.element_is_visible(self.locator.LOCATOR_SCOOTER_LOGO)

    @allure.step('Кликнуть лого "Яндекс"')
    def click_yandex_logo(self):
        self.find_element(self.locator.LOCATOR_YANDEX_LOGO).click()

    @allure.step('Кликнуть лого "Самокат"')
    def click_scooter_logo(self):
        self.find_element(self.locator.LOCATOR_SCOOTER_LOGO).click()

    @allure.step('Проверить, что кнопка "Заказать" отображается')
    def order_button_is_visible(self):
        return self.element_is_visible(self.locator.LOCATOR_ORDER_PAGE_IN_TOP_PAGE)

    @allure.step('Нажать кнопку "Заказать" в верхней части страницы')
    def click_order_button_in_page_top(self):
        order_button = self.find_element(self.locator.LOCATOR_ORDER_PAGE_IN_TOP_PAGE)
        order_button.click()

    @allure.step('Нажать кнопку "Заказать" в нижней части страницы')
    def click_order_button_in_page_bottom(self):
        order_button = self.find_element(self.locator.LOCATOR_ORDER_PAGE_IN_TOP_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        order_button.click()
