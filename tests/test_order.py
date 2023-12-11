import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
class TestOrder:
    @allure.title('Заказ самоката с использованием кнопки "Заказать" в верхней части страницы')
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в верхней части страницы')
    def test_order_scooter_in_page_top(self, driver):
        arendator = {'Имя': 'Василий', 'Фамилия': 'Иванов', 'Адрес': 'Москва, ул. Ольховская, 14, стр. 1',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494395',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 1234'}

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()

        main_page.order_button_is_visible()
        main_page.click_order_button_in_page_top()

        order_page.order_page_one_is_opened()

        order_page.enter_name(arendator['Имя'])
        order_page.enter_surname(arendator['Фамилия'])
        order_page.enter_address(arendator['Адрес'])
        order_page.select_station(arendator['Станция'])
        order_page.enter_phone(arendator['Телефон'])

        order_page.click_button_next()

        order_page.order_page_two_is_opened()

        order_page.enter_when(arendator['Когда привезти'])
        order_page.select_period(arendator['Срок аренды'])
        order_page.select_color(arendator['Цвет самоката'])
        order_page.enter_comment(arendator['Комментарий для курьера'])

        order_page.click_button_order()

        order_page.modal_window_is_visible()

        order_page.click_button_yes()

        assert order_page.order_number_is_visible() == True

    @allure.title('Заказ самоката с использованием кнопки "Заказать" в нижней части страницы')
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в нижней части страницы')
    def test_order_scooter_in_page_bottom(self, driver):
        arendator = {'Имя': 'Петр', 'Фамилия': 'Сидоров', 'Адрес': 'Москва, ул. Ольховская, 24, стр. 2',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494323',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 5678'}

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()

        main_page.order_button_is_visible()
        main_page.click_order_button_in_page_bottom()

        order_page.order_page_one_is_opened()

        order_page.enter_name(arendator['Имя'])
        order_page.enter_surname(arendator['Фамилия'])
        order_page.enter_address(arendator['Адрес'])
        order_page.select_station(arendator['Станция'])
        order_page.enter_phone(arendator['Телефон'])

        order_page.click_button_next()

        order_page.order_page_two_is_opened()

        order_page.enter_when(arendator['Когда привезти'])
        order_page.select_period(arendator['Срок аренды'])
        order_page.select_color(arendator['Цвет самоката'])
        order_page.enter_comment(arendator['Комментарий для курьера'])

        order_page.click_button_order()

        order_page.modal_window_is_visible()

        order_page.click_button_yes()

        assert order_page.order_number_is_visible() == True