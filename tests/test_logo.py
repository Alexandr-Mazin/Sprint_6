from pages.logo_page import LogoPage
from conftest import driver
import pytest
import allure

class TestLogoScooter:

    @allure.description(
    'Проверяем что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_logo_scooter(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_logo_scooter()
        assert logo_page.get_url() == 'https://qa-scooter.praktikum-services.ru/'

class TestLogoYandex:

    @allure.description(
    'Проверяем что если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_logo_yandex(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_logo_yandex()
        logo_page.switch_tab()
        logo_page.wait_visibility_dzen()
        assert logo_page.get_url() == 'https://dzen.ru/?yredirect=true'