from selenium.webdriver.common.by import By


class SitesLocators:
    GO_TO_SITES_BTN = (By.XPATH,
                         '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[2]/div/a[2]')
    # Нет привязанных пикселей трекинга
    NO_PIX_TEXT_1 = (By.XPATH, '//*[@id="pixels"]/div/div/h2')
    # Чтобы вести рекламные кампании с оптимизацией конверсий на сайтах, создайте трекинговый пиксель
    NO_PIX_TEXT_2 = (By.XPATH, '//*[@id="pixels"]/div/div/h4/div/span')

    # Добавить пиксель
    NO_PIX_TEXT_3 = (By.XPATH, '//*[@id="pixels"]/div/div/div[2]/button/span/span')