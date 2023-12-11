import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Перейти на сайт')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Проверить видимость элемента')
    def element_is_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элемент')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Переключиться на вторую вкладку браузера')
    def switch_to_second_tab_in_browser(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Проскроллить страницу до элемента')
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

