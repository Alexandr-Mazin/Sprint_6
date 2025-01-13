from selenium.webdriver.common.by import By

class QuestionLocators:

    question_section = (By.XPATH, '//div[contains(text(),"Вопросы о важном")]')
    questions_number = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]']
    }

    response_number = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }
