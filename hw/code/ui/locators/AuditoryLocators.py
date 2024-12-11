from selenium.webdriver.common.by import By


class AuditoryLocators:
    CREATE_AUDITORY_BUTTON = (By.XPATH, '//*[@id="audience"]//button[contains(normalize-space(.), "Создать аудиторию")]')
    AUDITORY_NAME_INPUT = (By.XPATH, '//*[@id="root"]//input[@type="text"]')
    ADD_IST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(normalize-space(.), "Добавить источник")]')
    SOOBS_SUBSC_BTN = (By.XPATH, '//*[@id="root"]//section/div[@role="button"]//span[contains(text(), "Подписчики сообществ")]')
    ADD_AS_LIST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(@class, "AddGroupList_iconAfter__OqwYK")]')

    VK_SOOBS_BTN = (By.XPATH, '//*[@id="root"]//div[@role="button" and .//span[contains(text(), "Сообщества ВКонтакте")]]')
    TEXT_AREA = (By.XPATH, '//*[@id="_modal_88"]//textarea')
    ADD_BTN = (By.XPATH, '//*[@id="_modal_88"]//form//button')
    CLOSE_BTN = (By.XPATH, '//*[@id="_modal_88"]//div[@role="button" and @aria-label="Закрыть"]')

    SAVE_BTN = (By.XPATH, '//*[@id="root"]//button[contains(normalize-space(.), "Сохранить")]')
    SUBMIT_CREATE_BTN = (By.XPATH, '//*[@id="root"]//form//button[@type="submit"]')

    # lmao
    LMAO_SPAN = (By.XPATH, '//*[@id="root"]//section//span[contains(@class, "Selected_name")]')
