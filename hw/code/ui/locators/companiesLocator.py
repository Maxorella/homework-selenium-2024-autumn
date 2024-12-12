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

    # Демография
    DEMOGRAPHY_CONTAINER = (By.ID, 'react-collapsed-toggle-:rt:')
    SEX_CONTAINER = (By.XPATH, '//*[@data-name="sex"]')
    MALE_SEX = (By.XPATH, '//*[@data-name="sex"]/label[2]')
    AGE_FROM = (By.XPATH, '//*[@class="RangeSelector_container__HX-gb"]/div[1]')
    AGE_TO = (By.XPATH, '//*[@class="RangeSelector_container__HX-gb"]/div[2]')

    # Интересы и поведение
    INTEREST_AND_BEHAVIOUR_CONTAINER = (By.ID, 'react-collapsed-toggle-:ru:')
    INTEREST_CONTAINER = (By.ID, 'react-collapsed-toggle-:r3v:')
    INTEREST_INPUT = (By.ID, '10_4')
    FIRST_SEARCH_INTEREST = (By.XPATH, '//*[@class="vkuiCustomScrollView__box"]/div[1]')
    CHOSEN_INTEREST = (By.XPATH, '//*[@aria-label="Авто"]/div/span')
    DELETE_CHOSEN_INTEREST = (By.XPATH, '//*[@aria-label="Авто"]/div/button')
    ADD_EXCLUDES = (By.XPATH, '//*[@data-name="interests"]/button')
    EXCLUDES_INPUT = (By.ID, '10_7')
    INTEREST_ERROR = (By.XPATH, '//*[@data-name="interests"]/span/div')
    DELETE_INTEREST = (By.XPATH, '//*[@id="react-collapsed-toggle-:r3f:"]/svg')

    # Ключевые фразы
    KEY_PHRASES_CONTAINER = (By.ID, 'react-collapsed-toggle-:r40:')
    PHRASES_SUGGEST = (By.XPATH, '//*[@class="SuggestionsButton_button__b3AJw"]/div')
    INPUT_KEY_PHRASES = (By.XPATH, '//*[@id="react-collapsed-panel-:r40:"]/div[2]/div[1]/span/textarea')
    INPUT_MINUS_PHRASES = (By.XPATH, '//*[@id="react-collapsed-panel-:r40:"]/div[2]/div[2]/div/span/textarea')
    PHRASES_WARNINGS = (By.CLASS_NAME, 'SuggestionsDuplicates_duplicatesWarningLine__nfXaa')
    SEARCH_PERIOD = (By.XPATH, '//*[@max="30"]')
    FIELDS_CONTAINER = (By.CLASS_NAME, 'InterestsSubSection_content__VfrET')
    DELETE_KEY_PHRASES = (By.XPATH, '//*[@id="react-collapsed-toggle-:r4g:"]/svg')

    # Сообщества
    COMMUNITIES_CONTAINER = (By.ID, 'react-collapsed-toggle-:r4j:')
    COMMUNITIES_INPUT = (By.XPATH, '//*[@placeholder="Введите название сообщества"]')
    VK_COMMUNITIES = (By.XPATH, '//*[@id="react-collapsed-toggle-:r51:"]/div/div[2]')
    OK_COMMUNITIES = (By.XPATH, '//*[@id="react-collapsed-toggle-:r52:"]/div/div[2]')
    FIRST_SEARCHED = (By.XPATH, '//*[@id="react-collapsed-panel-:r51:"]/div/div[1]')
    FIRST_SEARCHED_OK = (By.XPATH, '//*[@id="react-collapsed-panel-:r52:"]/div/div[1]')
    COMMUNITY_COUNTER = (By.XPATH, '//*[@class="AppsAndGroupsForm_header__HNNOB"]/h4[1]')
    DELETE_GROUP = (By.XPATH, '//*[@class="Selected_item__DdUMQ"]/div')
    SELECTED_GROUP = (By.CLASS_NAME, 'Selected_item__DdUMQ')
    CANCEL_BTN = (By.XPATH, '//*[@class="AppsAndGroupsForm_header__HNNOB"]/h4[2]')
    COMMUNITIES_DELETE_ALL = (By.XPATH, '//*[@id="react-collapsed-toggle-:r4j:"]/svg')

    # Музыканты
    MUSICIANS_CONTAINER = (By.ID, 'react-collapsed-toggle-:r4k:')
    MUSICIANS_INPUT = (By.XPATH, '//*[@placeholder="Введите название музыканта"]')
    FIRST_MUSICIAN = (By.XPATH, '//*[@class="VariantsList_list__dyFBd"]/div[1]')
    DONE_MUSICIANS_SEARCH = (By.CLASS_NAME, 'SearchInputDropdown_dropdownAction__Uk6t-')
    SELECTED_MUSICIAN_COUNTER = (By.XPATH, '//*[@class="Header_header__iyI-k"]/h4[1]')
    DELETE_SEARCHED_MUSICIAN = (By.XPATH, '//*[@class="Selected_item__Po+fb"]/div')
    SELECTED_MUSICIAN = (By.CLASS_NAME, 'Selected_item__Po+fb')
    MUSICIANS_DELETE_ALL = (By.XPATH, '//*[@class="Header_header__iyI-k"]/h4[2]')
    MUSICIANS_TRASH_BEAN = (By.XPATH, '//*[@id="react-collapsed-toggle-:r2q:"]/svg')


