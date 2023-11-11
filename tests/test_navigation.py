import allure
from pages.main_page import MainPage
class TestNavigation:
    @allure.title('Проверка навигации при нажатии на лого "Яндекс"')
    @allure.description('Проверка перехода на страницу "Яндекс.Дзен" при нажатии на лого "Яндекс"')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()

        main_page.yandex_logo_is_visible()
        main_page.click_yandex_logo()

        main_page.switch_to_second_tab_in_browser()

        assert 'dzen.ru' in driver.current_url

    @allure.title('Проверка навигации при нажатии на лого "Самокат"')
    @allure.description('Проверка перехода на главную страницу при нажатии на лого "Самокат"')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()

        main_page.scooter_logo_is_visible()
        main_page.click_scooter_logo()

        main_page.switch_to_second_tab_in_browser()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'