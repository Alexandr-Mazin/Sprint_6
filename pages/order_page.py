from locators.order_locators import OrderLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def entry_name_form(self, test_user):
        self.wait_visibility_element(OrderLocators.name_field)
        self.enter_text(OrderLocators.name_field, test_user[0])

    @allure.step('Ввод фамилии')
    def entry_surname_form(self, test_user):
        self.enter_text(OrderLocators.surname_field, test_user[1])

    @allure.step('Ввод адреса')
    def entry_address_form(self, test_user):
        self.enter_text(OrderLocators.input_address, test_user[2])

    @allure.step('Выбор метро')
    def entry_metro_form(self, test_user):
        self.click_element(OrderLocators.input_metro)
        self.enter_text(OrderLocators.input_metro, test_user[3])
        self.click_element(OrderLocators.select_metro)

    @allure.step('Ввод телефона')
    def entry_phone_form(self, test_user):
        self.enter_text(OrderLocators.input_phone, test_user[4])

    @allure.step('Нажатие далее')
    def click_next_button(self):
        self.click_element(OrderLocators.button_next)

    # Ожидание второго поля
    def wait_visibility_dzen(self):
        self.wait_visibility_element(OrderLocators.input_date)

    @allure.step('Ввод даты')
    def entry_data_form(self, test_user):
        self.wait_visibility_element(OrderLocators.input_date)
        self.click_element(OrderLocators.input_date)
        self.enter_text(OrderLocators.input_date, test_user[5])
        self.click_element(OrderLocators.clic_date)


    @allure.step('Выбор срока')
    def entry_time_form(self, test_user):
        self.click_element(OrderLocators.time_order)
        self.click_element(OrderLocators.time_one_day)

    @allure.step('Выбор цвета')
    def entry_color_form(self, test_user):
        self.click_element(OrderLocators.checkbox_black)

    @allure.step('Ввод комментария')
    def entry_comment_form(self, test_user):
        self.enter_text(OrderLocators.input_comment, test_user[6])

    @allure.step('Нажатие кнопки заказать')
    def click_order_finish_button(self):
        self.click_element(OrderLocators.button_order_finish)

    @allure.step('Нажатие Да в подтверждении заказа')
    def click_button_verification(self):
        self.click_element(OrderLocators.button_verification_order)

    # Проверка, что заказ оформлен
    def order_finish(self):
        return self.get_text_element(OrderLocators.order_finish)

    # Скролл до заказа
    def scroll_order(self):
        self.scroll_element(OrderLocators.order_button_2)