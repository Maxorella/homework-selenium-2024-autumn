from selenium.webdriver.common.by import By


class PixelLocators:
    CREATE_PIX_NOPIX_BTN = (By.XPATH, '//*[@class="vkuiPlaceholder__action"]//button')
    DOMEN_INPUT = (By.XPATH, '//*//input[@placeholder="Домен сайта"]')
    ADD_PIXEL_BTN = (By.XPATH, '//*[@class="vkuiModalCardBase__actions"]//button')
    CHOICE_CREATE_NEW_PIX_BTN = (By.XPATH, '//*//div[@role="button" and contains(@class,"FlowSelectStep_cell__LXV8m")][2]')
    CLOSE_CREATED_BTN = (By.XPATH, '//*//div[@aria-label = "Закрыть"]')
    CREATED_PIX_URL = (By.XPATH, '//*[@id="pixels"]//a[@href and contains(text(), "tean.homes")]') # tean.homes

    # 2 тест
    POINT_3_BTN = (By.XPATH, '//div[@class="BaseTable__body"]//button[@aria-label="More"]')
    AUD_SPIS = (By.CLASS_NAME, 'BaseTable__body')
    DELETE_DROPPED_BTN = (By.XPATH, '//div[contains(@class,"PopoverContent_root")]//label[2]')
    SUBMIT_DELETE_BTN = (By.XPATH, '//button[contains(normalize-space(.), "Удалить")]')
    TITLE_NO_PIX = (By.XPATH, '//*[@id="pixels"]//h2[contains(text(), "Нет привязанных пикселей трекинга")]')

    # 3 тест

    EDIT_DROPPED_BTN = (By.XPATH, '//*[@id=":rb:"]//label[1]')
    EDIT_NAME_INPUT = (By.XPATH, '//*[@id="_modal_28"]//input')
    EDIT_SUBMIT_BTN = (By.XPATH, '//*[@id="_modal_28"]//button[contains(normalize-space(.), "Изменить")]')
    PIXEL_TITLE = (By.XPATH, '//*[@id="pixels"]//div[@title="tean auth"]//span[contains(text(), "tean auth")]')

    # 4 тест

    SETTINGS_BTN = (By.XPATH, '//*[@id="pixels"]//a[contains(text(), "Настройка")]')
    ADD_EVENT_NO_OTHER_BTN = (By.XPATH, '//*[@id="pixels.events"]//button')

    EVENT_NAME_INPUT = (By.XPATH, '//*[@id="root"]//input[@placeholder="Введите название"]')
    CATEGORY_INPUT = (By.XPATH, '//*[@id="root"]//input[@placeholder="Выберите категорию"]')

    # 5 тест
    # SETTINGS_BTN
    AUDITORY_TAGS_BTN = (By.XPATH, '//*[@id="tab_pixels.audience_tags"]')
    CREATE_AUDITORY_TAG_BTN = (By.XPATH, '//*[@id="pixels.audience_tags"]//button[normalize-space(.)="Создать аудиторный тег"]')
    TAG_NAME_INPUT = (By.XPATH, '//*/span/input')
    SUBMIT_CREATE_BTN = (By.XPATH, '//*/button[2]')
    TAG_NAME_CREATED_AUDITORY = (By.XPATH, '//*[@id="pixels.audience_tags"]//div[@class="BaseTable__row-cell-text" and contains(text(), "mytag_name")]')
