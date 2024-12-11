from selenium.webdriver.common.by import By


class CompaniesLocator:
    CREATE_NEW_COMPANY = (By.XPATH, '//*[@data-testid="create-button"]')
    CREATE_SITE_ADVERTISE = (By.XPATH, '//*[@data-id="site_conversions"]')
    SITE_HREF = (By.CLASS_NAME, 'vkuiInput__el')
    HREF_ERROR = (By.CLASS_NAME, 'vkuiFormItem__bottom')
    BUDGET_FIELD = (By.XPATH, '//*[@data-testid="targeting-not-set"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@class="vkuiDiv CreateFooter_footerContent__hFvR8"]/div[2]/div[2]/button')
    ERROR_BTN = (By.XPATH, '//*[@class="ErrorsTooltip_tooltipContainer__fl0Xo"]/button')
    ADVERTISE_SITE_ERROR = (By.XPATH, '//*[@data-id="new-site_conversions"]')
    EXPAND_REGION = (By.XPATH, '//*[@data-testid="section-lal"]')
    BUDGET_DUPLICATE = (By.CLASS_NAME, 'FullBudget_valueLabel__3Y22w')
    BUDGET_TIME = (By.XPATH, '//*[@data-testid="budget"]')
    END_DATE = (By.XPATH, '//*[@data-testid="end-date"]')
    DECEMBER_31 = (By.XPATH, '//*[@class="vkuiCalendarDays"]/div[7]/div[2]')
    END_INPUT_DATE = (By.XPATH, '//*[@data-testid="end-date"]/input')
    DECEMBER_2 = (By.XPATH, '//*[@class="vkuiCalendarDays"]/div[3]/div[1]')

    # Группы объявлений
    FAST_CHOICE_REGIONS = (By.XPATH, '//*[@class="RegionsQuickSelection_wrapper__7kX9f"]/button[2]')
    CHOSEN_REGION = (By.XPATH, '//*[@class="RegionsList_wrapper__wuqdC"]/div/span/h4')
    REGION_SEARCH = (By.XPATH, '//*[@data-testid="search"]')
    SEARCH_RESULT = (By.XPATH, '//*[@class="composite_unit__1W0jc"]/div[2]')
    NUMBER_CHOSEN = (By.CLASS_NAME, 'RegionsSelector_selectedRegionsCount__LWBfS')
