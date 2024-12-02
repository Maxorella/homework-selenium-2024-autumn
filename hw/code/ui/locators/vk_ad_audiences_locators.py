from selenium.webdriver.common.by import By


class AudiencesLocators:
    # кнопка сайты в меню
    GO_AUDIENCES_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[1]/a[3]')

    # up menu
    UP_MENU_AUDIENCES_BTN = (By.XPATH, '//*[@id="tab_audience"]')
    UP_MENU_USER_LIST_BTN = (By.XPATH, '//*[@id="tab_audience.users_list"]')
    UP_MENU_OFFLINE_CONVERSION_BTN = (By.XPATH, '//*[@id="tab_audience.offline_conversion"]')

    # создать аудитории
    UP_MENU_CREATE_AUDIENCE_BTN = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[1]/div[1]/button') #/span/span

    # троеточие
    TRI_TOCH = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[1]/div[1]/div')

    # Фильтр
    FILTER_TEXT = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[1]/div[2]/button/span/span[2]')

    # кнопка поделиться
    SHARE_BTN = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[1]/button[1]')

    # DELETE
    DELETE_BTN = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[1]/button[2]')  # /span/span/svg

    # SEARCH FIELD
    SEARCH_FIELD = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]')

    # 'Сохраняйте пользователей по их действиям в аудитории. Аудитории можно использовать в кампаниях, чтобы показать рекламу тем, кого она точно заинтересует'
    # текст на странице
    BIG_TEXT_AUDIENCES = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[2]/div/div/h4/div/span')

    # создать аудиторию посередине
    CREATE_AUDIENCE_WINDOW_BTN = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[2]/div/div/div[2]/div/button')  # /span/span


    # ------

    # Создание аудитории
    CREATE_AUDIENCE_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/form/div[1]/h2')

    # Название поле
    NAME_AUDIENCE_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/div[1]/div/section[1]/div/span/input')
    # span с ошибкой (Напишите текст не больше 255 символов)
    NAME_AUDIENCE_ERROR_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/div[1]/div/section[1]/div/span[2]')

    # добавить источник
    ADD_IST_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/div[1]/div/section[2]/div/button')  # /span/span

    # подписчики сообществ
    SOOBS_SUBSC_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/section/div[10]')  # /span/span

    # поле поиска сообщества
    SEARCH_FIELD_SOOBS = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/section/div/div[1]/div/span/input')

    # ничего не нашлось
    NOTH_FOUND_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/section/div/div[1]/div/div/span')

    # Показать все плашка
    SHOW_ALL_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/section/div/div[1]/div/div')

    # div с lmao
    ADD_LMAO_BTN = (By.XPATH, '//*[@id="react-collapsed-panel-:rl:"]/div/div[1]')
    # подписчики сообществ
    Subsc_title_text = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/h2')

    # save btn
    SAVE_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/button[1]')
    # save2 btn
    SAVE2_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/div[2]/div/button[1]')
    # aud название
    AUD_TITLE_TEXT = (By.XPATH, '//*[@id="audience"]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/h5')
