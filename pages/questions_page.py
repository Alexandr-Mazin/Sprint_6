from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_locators import QuestionLocators
from pages.base_page import BasePage
import allure


class QuestionsPage(BasePage):

    #Проскроллить до секции "Вопросы о важном"
    def scroll_questions(self):
        self.scroll_element(QuestionLocators.question_section)

    @allure.step('Кликнуть на номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_questions(self, data):
        self.click_element(QuestionLocators.questions_number[data])

    @allure.step('Получить текст нужного номера ответа в аккордеоне')
    def get_text_response(self, data):
        return self.get_text_element(QuestionLocators.response_number[data])