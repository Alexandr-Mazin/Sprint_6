from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
import allure

class LogoPage(BasePage):

    @allure.step('Клик на лого Самокат')
    def click_logo_scooter(self):
        self.click_element(LogoLocators.scooter_logo)

    # Получить текущий URL
    def get_url(self):
        return self.driver.current_url

    @allure.step('Клик на лого Яндекс')
    def click_logo_yandex(self):
        self.click_element(LogoLocators.yandex_logo)

    def switch_tab_yandex(self):
        self.switch_tab()

    def wait_visibility_dzen(self):
        self.wait_visibility_element(LogoLocators.dzen_logo)