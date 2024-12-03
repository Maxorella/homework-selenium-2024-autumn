from selenium.webdriver.common.by import By


class CompaniesLocators:
    CLOSE_EDUCATION_POPAP = (By.XPATH, '//*[@id="_modal_28"]/div/div/div[3]')
    COMPANIES_HREF = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[1]/a[2]')
    CREATE_COMPANY = (By.XPATH, '//*[@class="vkuiPlaceholder__action"]/button')
    CREATE_COMPANY_CONTAINER = (By.ID, 'new_ad_create')
    COMPANY_NAME = (By.CLASS_NAME, 'PlanForm_title__wffcf')
    COMPANY_NAME_TEXT = (By.XPATH, '//*[@class="PlanForm_title__wffcf"]/div/h2')

    CONTINUE_BUTTON = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button')
    ERROR_BUTTON = (By.CLASS_NAME, 'ErrorsTooltip_button__YyIDS')
    ERROR_LOG = (By.CLASS_NAME, 'vkuiTooltipBase__content')

class TargetedActionsLocators:
    SITE_CONTAINER = (By.XPATH, '//*[@data-id="site_conversions"]')
    ADVERTISE_SITE = (By.CLASS_NAME, 'vkuiInput__el')
    ADVERTISE_CONTAINER = (By.CLASS_NAME, 'ObjectiveSelect_list__o-CIf')
    CATALOG_CONTAINER = (By.XPATH, '//*[@data-id="ecomm"]')
    CATALOG_PROPERTIES = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section[2]/form/div[1]')
    MOBILE_CONTAINER = (By.XPATH, '//*[@data-id="mobapps"]')
    MOBILE_INPUT = (By.CLASS_NAME, 'vkuiCustomSelectInput__el')
    COMMUNITY_CONTAINER = (By.XPATH, '//*[@data-id="social"]')
    COMMUNITY_INPUT = (By.CLASS_NAME, 'vkuiCustomSelectInput__el')
    OK_CONTAINER = (By.XPATH, '//*[@data-id="odkl"]')
    OK_INPUT = (By.CLASS_NAME, 'vkuiCustomSelectInput__el')
    DZEN_CONTAINER = (By.XPATH, '//*[@data-id="dzen"]')
    DZEN_INPUT = (By.CLASS_NAME, 'vkuiPlaceholder__action')
    LEAD_CONTAINER = (By.XPATH, '//*[@data-id="leadads"]')
    LEAD_INPUT = (By.CLASS_NAME, 'vkuiCustomSelectInput__el')
    VK_MINI_APPS_CONTAINER = (By.XPATH, '//*[@data-id="miniapps"]')
    VK_MINI_APPS_INPUT = (By.CLASS_NAME, 'vkuiCustomSelectInput__el')
    MUSIC_CONTAINER = (By.XPATH, '//*[@data-id="socialmusic"]')
    MUSIC_INPUT = (By.CLASS_NAME, 'vkuiPlaceholder__action')
    VIDEO_CONTAINER = (By.XPATH, '//*[@data-id="socialvideo"]')
    VIDEO_INPUT = (By.CLASS_NAME, 'vkuiPlaceholder__action')

    CALENDAR_INPUT = (By.XPATH, '//*[@data-test-id="start-date"]')
    CALENDAR_CONTAINER = (By.CLASS_NAME, 'vkuiCalendar')