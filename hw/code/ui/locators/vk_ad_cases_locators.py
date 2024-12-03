from selenium.webdriver.common.by import By


class CasesLocators:
    # Заголовок
    CASES_HEADER = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div/div[1]/div/h1')
    CLOSE_NOTIFICATION = (By.CLASS_NAME, 'NotificationModal_cancel__yzE1d')
