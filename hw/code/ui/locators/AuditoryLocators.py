from selenium.webdriver.common.by import By


class AuditoryLocators:
    CREATE_AUDITORY_BUTTON = (By.XPATH, '//*[@id="audience"]//button[contains(normalize-space(.), "Создать аудиторию")]')
    AUDITORY_NAME_INPUT = (By.XPATH, '//*[@id="root"]//input[@type="text"]')
    ADD_IST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(normalize-space(.), "Добавить источник")]')
    SOOBS_SUBSC_BTN = (By.XPATH, '//*[@id="root"]//section/div[@role="button"]//span[contains(text(), "Подписчики сообществ")]')
    ADD_AS_LIST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(@class, "AddGroupList_iconAfter__OqwYK")]')

    VK_SOOBS_BTN = (By.XPATH, '//*[@id="root"]//div[@role="button" and .//span[contains(text(), "Сообщества ВКонтакте")]]')
    TEXT_AREA = (By.XPATH, '//textarea[starts-with(@placeholder, "Например:")]')

    #ADD_BTN = (By.XPATH, '//*//form//button[normalize-space(.) = "Добавить" and @type="submit"]')
    # TODO на странице есть две кнопки сохранить абсолютно одинаковые, в одинаковых футерах лежат(div), как отличить их - не знаю.....
    ADD_BTN = (By.XPATH, '//*//form//button[normalize-space(.) = "Добавить" and @type="submit"]')
    CLOSE_BTN = (By.XPATH, '//*//div[@role="button" and @aria-label="Закрыть"]')

    SAVE_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/button[1]')
    SUBMIT_CREATE_BTN = (By.XPATH, '//*[@id="root"]//form//button[@type="submit"]')

    # lmao
    LMAO_SPAN = (By.XPATH, '//*[@id="audience"]//h5[contains(@class, "NameCell_name__lgrNA")]')
