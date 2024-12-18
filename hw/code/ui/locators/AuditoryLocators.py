from selenium.webdriver.common.by import By


class AuditoryLocators:

    # 1 тест

    CREATE_AUDITORY_BUTTON = (By.XPATH, '(//*[@id="audience"]//button[contains(normalize-space(.), "Создать аудиторию")])[1]')

    AUDITORY_NAME_INPUT = (By.XPATH, '//*[@id="root"]//input[@type="text"]')

    ADD_IST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(normalize-space(.), "Включить источник")]')

    PHRASES_OPTION = (By.XPATH, '//*[@id="root"]//div[@role="button" and .//span[text()="Ключевые фразы"]]')

    PHRASES_TITLE_INPUT = (By.XPATH, '//*[@id="root"]//input[@value="Ключевые фразы"]')
    PHRASES_PLUS_INPUT = (By.XPATH, '(//*[@id="root"]//textarea[@placeholder="Введите фразу и нажмите Enter"])[1]')

    # общая причем!! [2] придется оставить мб можно как-то и лучше сделать
    SAVE_BTN = (By.XPATH, '(//*[@id="root"]//button[.//span[text()="Сохранить"]])[2]')

    CANCEL_EDIT_BTN = (By.XPATH, '//*[@id="root"]//button[@data-testid="cancel"]')

    SAVE_2_BTN = (By.XPATH, '(//*[@id="root"]//button[.//span[text()="Сохранить"]])[1]')

    AUD_TITLE_H5 = (By.XPATH, '(//*[@id="audience"]//h5)[2]') # кликнуть и в редакт

    PHRASE_IN_EDIT = (By.XPATH, '(//*[@id="root"]//div[@class="SourcesGroup_groupSources__7Xjh8"]//div[@class="InfoRow_content__LN5Bb"])[1]')

    TITLE_IN_EDIT = (By.XPATH, '//*[@id="root"]//div[@class="SourceListItem_card__VcdHk"]//h4')

    # удаление аудитории

    AUD_IN_LIST = (By.XPATH, '//*[@id="audience"]//div[contains(@class, "NameCell_wrapper__hxqrL")]')
    POINT_3 = (By.XPATH, '//*[@id="audience"]//button[@aria-label="More"]')

    # TODO мб промах
    DELETE_DROPPED_BTN = (By.XPATH, '//div[contains(@class,"PopoverContent_root")]//label[3]')

    DELETE_SUBMIT_BTN = (By.XPATH, '//*[contains(@id, "_modal_")]//button[2]')

    NO_AUD_LABEL = (By.XPATH, '//*[@id="audience"]//h2')



    #

    SOOBS_SUBSC_BTN = (By.XPATH, '//*[@id="root"]//section/div[@role="button"]//span[contains(text(), "Подписчики сообществ")]')
    ADD_AS_LIST_BTN = (By.XPATH, '//*[@id="root"]//button[contains(@class, "AddGroupList_iconAfter__OqwYK")]')

    VK_SOOBS_BTN = (By.XPATH, '//*[@id="root"]//div[@role="button" and .//span[contains(text(), "Сообщества ВКонтакте")]]')
    TEXT_AREA = (By.XPATH, '//textarea[starts-with(@placeholder, "Например:")]')

    #ADD_BTN = (By.XPATH, '//*//form//button[normalize-space(.) = "Добавить" and @type="submit"]')
    # TODO на странице есть две кнопки сохранить абсолютно одинаковые, в одинаковых футерах лежат(div), как отличить их - не знаю.....
    ADD_BTN = (By.XPATH, '//*//form//button[normalize-space(.) = "Добавить" and @type="submit"]')
    CLOSE_BTN = (By.XPATH, '//*//div[@role="button" and @aria-label="Закрыть"]')

    SUBMIT_CREATE_BTN = (By.XPATH, '//*[@id="root"]//form//button[@type="submit"]')

    # lmao
    LMAO_SPAN = (By.XPATH, '//*[@id="audience"]//h5[contains(@class, "NameCell_name__lgrNA")]')

    # 1 тест
