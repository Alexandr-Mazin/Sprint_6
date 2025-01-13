from selenium.webdriver.common.by import By

class OrderLocators:

    #Кнопка заказать верхняя
    order_button_1 = (By.CLASS_NAME, 'Button_Button__ra12g')
    # Кнопка заказать нижняя
    order_button_2 = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    # Поле Имя
    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Поле Фамилия
    surname_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Поле Адрес
    input_address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Поле Станция метро
    input_metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Список метро
    select_metro = (By.XPATH, './/li[@class="select-search__row"]')
    # Поле телефон
    input_phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка далее
    button_next = (By.XPATH, '//button[text()="Далее"]')

    # Поле Когда привезти
    input_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    clic_date = (By.XPATH, '//div[contains(text(),"10")]')
    # Поле Срок аренды
    time_order = (By.XPATH, './/div[text()="* Срок аренды"]')
    # Выбор одного дня
    time_one_day = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text() ='сутки']")
    # ЧБ чёрный
    checkbox_black = (By.ID, 'black')
    # ЧБ серый
    checkbox_grey = (By.ID, 'grey')
    # Поле комментарий
    input_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка заказать
    button_order_finish = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Кнопка подтверждения заказа
    button_verification_order = (By.XPATH, '//button[text()="Да"]')

    # Окно заказа
    order_finish = (By.XPATH, ".//div[text()='Заказ оформлен']")
