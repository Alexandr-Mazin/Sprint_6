from pages.questions_page import QuestionsPage
from conftest import driver
from data import TextData
import pytest
import allure


class TestMainResponse:

    @allure.description(
        'Проверяем что когда нажимаешь на стрелочку, открывается соответствующий текст в разделе «Вопросы о важном»')
    @allure.title('Проверка текста в блоке «Вопросы о важном»')
    @pytest.mark.parametrize('question_number, expected_answer', TextData.questions_response)
    def test_response_text(self, driver, question_number, expected_answer):
        questions_page = QuestionsPage(driver)
        questions_page.scroll_questions()
        questions_page.click_questions(question_number)
        assert questions_page.get_text_response(question_number) == expected_answer