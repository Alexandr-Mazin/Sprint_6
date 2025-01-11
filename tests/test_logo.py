from pages.logo_page import LogoPage
from conftest import driver
import pytest
import allure
from data import Url

class TestLogoScooter:

    @allure.description(
    'Проверяем что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    @allure.title('Проверка перехода при клике на логотип «Самоката»')
    def test_logo_scooter(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_logo_scooter()
        assert logo_page.get_url() == Url.url_scooter

class TestLogoYandex:

    @allure.description(
    'Проверяем что если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    @allure.title('Проверка перехода при клике на логотип «Яндекса»')
    def test_logo_yandex(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_logo_yandex()
        logo_page.switch_tab_yandex()
        logo_page.wait_visibility_dzen()
        assert logo_page.get_url() == Url.url_yandex