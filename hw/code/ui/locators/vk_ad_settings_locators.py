from selenium.webdriver.common.by import By


class SettingsLocators:
    SETTINGS_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/section/a')

    # Телефон
    TELE_TEXT = (By.XPATH, '//*[@id="settings"]/div/form/section[3]/div[2]/div[1]/h2')

    # Email
    EMAIL_TEXT = (By.XPATH, '//*[@id="settings"]/div/form/section[3]/div[2]/div[2]/div[1]/div/h5')

    # Добавить email
    EMAIL_LINK = (By.XPATH, '//*[@id="settings"]/div/form/section[3]/div[2]/div[2]/div[2]/div/div[2]/div/span')

    # ФИО
    FIO_LINK = (By.XPATH, '//*[@id="settings"]/div/form/section[4]/div[2]/div[1]/h2/span[1]')

    # ИНН
    INN_LINK = (By.XPATH, '//*[@id="settings"]/div/form/section[4]/div[2]/div[2]/h2/span[1]')

    # Название кабинета
    NAZB_CAB = (By.XPATH, '//*[@id="settings"]/div/form/section[5]/div[2]/div[1]/h2/span')

    # Язык интерфейса
    LANG_INT = (By.XPATH, '//*[@id="settings"]/div/form/section[5]/div[2]/div[2]/div/h2/span')

    # Связанные кабинеты
    SVYAZ_CAB = (By.XPATH, '//*[@id="settings"]/div/form/section[6]/div[1]/h2')

    # Выйти из других устройств
    EXIT_OTHER_USTR = (By.XPATH, '//*[@id="settings"]/div/form/section[8]/button/span/span')

    # Удалить кабинет
    DELETE_CAB_BTN = (By.XPATH, '//*[@id="settings"]/div/form/section[9]/button/span/span')

    # Уведомления
    UVEDOML_BTN = (By.XPATH, '//*[@id="tab-settings.notifications"]')

    # Способы получения
    SPOS_POLUCH = (By.XPATH, '//*[@id="settings.notifications"]/div/div[2]/div[1]/h2')

    # Сообщение в Telegram
    MESS_TELEG = (By.XPATH, '//*[@id="settings.notifications"]/div/div[2]/div[1]/div[2]/div/div[2]/div/span/div')

    # Основные
    OSNOVN = (By.XPATH, '//*[@id="settings.notifications"]/div/div[2]/div[1]/section[1]/h2')

    # Новости и акции
    NEWS_DISC = (By.XPATH, '//*[@id="settings.notifications"]/div/div[2]/div[1]/section[2]/h2')


    # Права доступа
    PRAVA_BTN_MENU = (By.XPATH, '//*[@id="tab-settings.access"]/span')

    # Добавить кабинет
    ADD_CAB_BTN_TEXT = (By.XPATH, '//*[@id="settings.access"]/div/div[2]/div/div[2]/button/span/span')

    # Подробнее
    PODROBN_TEXT = (By.XPATH, '//*[@id="settings.access"]/div/div[2]/div/h4/div/span/a')

    # История изменений кнопка
    HIST_BTN_MENU = (By.XPATH, '//*[@id="tab-settings.logs"]')

    # История изменений
    HIST_BTN_MENU_SPAN = (By.XPATH, '//*[@id="tab-settings.logs"]/span')

    # Здесь будет храниться история изменений в кабинете
    HIST_TAB_TEXT = (By.XPATH, '//*[@id="settings.logs"]/div/div[2]/div/div[2]/div/div/h4/div/span')