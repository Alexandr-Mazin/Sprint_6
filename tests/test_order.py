from locators.order_locators import OrderLocators
from pages.order_page import OrderPage
from data import TextData
from conftest import driver
import pytest
import allure

class TestOrder:

    @allure.description(
        'Проверяем что позитивный сценарий оформления заказа с двумя наборами данных')
    @pytest.mark.parametrize('button, test_data',
                             [
                                (OrderLocators.order_button_1, TextData.test_user_1),
                                (OrderLocators.order_button_2, TextData.test_user_2)
                             ]
                             )

    def test_order(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_order()
        order_page.click_element(button)
        order_page.entry_name_form(test_data)
        order_page.entry_surname_form(test_data)
        order_page.entry_address_form(test_data)
        order_page.entry_metro_form(test_data)
        order_page.entry_phone_form(test_data)
        order_page.click_next_button()

        order_page.entry_data_form(test_data)
        order_page.entry_time_form(test_data)
        order_page.entry_color_form(test_data)
        order_page.entry_comment_form(test_data)
        order_page.click_order_finish_button()
        order_page.click_button_verification()

        assert 'Заказ оформлен' in order_page.order_finish()