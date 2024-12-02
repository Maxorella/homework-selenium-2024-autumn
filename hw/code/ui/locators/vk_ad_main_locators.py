from selenium.webdriver.common.by import By


class AuthLocators:
    GO_TO_LK_BTN = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol") # кнопка перейти в личный кабинет
    GO_WITH_EMAIL_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/div/form/div[2]/div[1]/section/div/div[2]/div/button[2]') # кнопка продолжить с mail.ru
    EMAIL_ENTER_FIELD = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/form/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div/input') # поле ввода почты
    ENTER_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/form/div[2]/div[2]/div[3]/div/div/div[1]/button') # кнопка войти
    ENTER_OTHER_WAY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/form/div[2]/div/div[6]/button[2]') # кнопка войти другим способом
    PASSWORD_ENTER_FIELD = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/form/div[2]/div/div[2]/div/div/div/div/div/input') # поле ввода пароля
    ENTER_PASSWORD_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/form/div[2]/div/div[3]/div/div/div[1]/button') # кнопка войти после ввода пароля
    SURNAME_NAME_DIV = (By.CLASS_NAME, 'c1150') # div с Именем Фамилией текущего аккаунта


class MainPageNoLoginNavbarLoc:
    # лого
    MAIN_PAGE_LOGO_BTN = (By.CLASS_NAME, 'content_home__VLt6p')
    # svg лого
    SVG_LOGO = (By.TAG_NAME, 'SVG')
    # кнопка новости
    MAIN_PAGE_HEADER_NEWS_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[2]/div/a')
    # кнопка полезные материалы
    MAIN_PAGE_USEFUL_MATERIALS_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/a')
    # кнопка мероприятия
    MAIN_PAGE_EVENTS_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/a')
    # кнопка видеокурсы
    MAIN_PAGE_VIDEOCOURSES_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[3]/div[2]/div/div[3]/a')
    # кнопка сертификаты
    MAIN_PAGE_CERRTIFICATES_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[3]/div[2]/div/div[4]/a')
    # кнопка кейсы
    MAIN_PAGE_CASES_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[4]/div/a')
    # кнопка форум идей
    MAIN_PAGE_IDEAS_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[5]/div/a')
    # блок обучние
    MAIN_PAGE_ADUCATION = (By.CLASS_NAME, 'item_item__0CD1p')
    # кнопка монетизация
    MAIN_PAGE_MONETIZATION_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[6]/div/a')
    # кнопка справка
    MAIN_PAGE_REFERENCE_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[2]/div/div/a')
    # кнопка в главный кабинет
    MAIN_PAGE_GO_TO_LK_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[2]/a')
    # плашка обучение
    STUDY_POPUP = (By.XPATH, '//*[@id="classic-layout"]/div[1]/div/header/div/div[2]/div/div[1]/div[3]/div[1]/span')