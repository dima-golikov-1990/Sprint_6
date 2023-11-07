from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_ORDER_PAGE_IN_TOP_PAGE = (By.XPATH, "(//button[text()='Заказать'])[1]") # кнопка "Заказать" в верхней части страницы
    LOCATOR_ORDER_PAGE_IN_BOTTOM_PAGE = (By.XPATH, "(//button[text()='Заказать'])[2]")  # кнопка "Заказать" в нижней части страницы
    LOCATOR_YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI') # лого "Яндекс"
    LOCATOR_SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR') # лого "Самокат"

    def get_accordeon_locator(self, accordeon_text):
        return (By.XPATH, "//*[text()='" + accordeon_text + "']")

    def get_panel_locator(self, panel_text):
        return (By.XPATH, "//p[text()='" + panel_text + "']")