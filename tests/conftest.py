import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    service = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=Service(service))
    yield browser
    browser.quit()
