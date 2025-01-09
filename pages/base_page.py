from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Проскроллить до элемента
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    #Подождать прогрузки элемента
    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))

    #Кликнуть на элемент
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    #Ввести значение в поле ввода
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    #Получить текст на элементе
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    #Перейти на другую вкладку
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    #Проверить отображение элемента
    def check_displaying_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()