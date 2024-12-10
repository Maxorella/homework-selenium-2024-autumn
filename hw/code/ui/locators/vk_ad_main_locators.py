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
    SURNAME_NAME_DIV_MAXORELLA = (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div/div/div') # div с Именем Фамилией текущего аккаунта