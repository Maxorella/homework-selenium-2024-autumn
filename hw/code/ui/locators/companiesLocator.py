from selenium.webdriver.common.by import By


class CompaniesLocator:
    CREATE_NEW_COMPANY = (By.XPATH, '//*[@data-testid="create-button"]')
    CREATE_SITE_ADVERTISE = (By.XPATH, '//*[@data-id="site_conversions"]')
    SITE_HREF = (By.CLASS_NAME, 'vkuiInput__el')
    BUDGET_FIELD = (By.XPATH, '//*[@data-testid="targeting-not-set"]')