import pytest
from selenium import webdriver
from data import Url

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.url_scooter)
    yield driver
    driver.quit()