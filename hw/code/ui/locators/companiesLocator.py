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
    STRATEGY = (By.XPATH, '//*[@data-name="autobidding_mode"]/div')
    STRATEGY_SELECT = (By.XPATH, '//*[@data-name="autobidding_mode"]/div/select')
    STRATEGY_SELECTED = (By.XPATH, '(//*[@class="vkuiCustomSelectInput__container"])[2]/span')

    # Группы объявлений
    FAST_CHOICE_REGIONS = (By.XPATH, '//*[@class="RegionsQuickSelection_wrapper__7kX9f"]/button[2]')
    CHOSEN_REGION = (By.XPATH, '//*[@class="RegionsList_wrapper__wuqdC"]/div/span/h4')
    REGION_SEARCH = (By.XPATH, '//*[@data-testid="search"]')
    SEARCH_RESULT = (By.XPATH, '//*[@class="composite_unit__1W0jc"]/div[2]')
    NUMBER_CHOSEN = (By.CLASS_NAME, 'RegionsSelector_selectedRegionsCount__LWBfS')

    # Демография
    DEMOGRAPHY_CONTAINER = (By.XPATH, '//*[@class="GroupForm_layout__2FvbV"]/section[1]/div[1]/div')

    SEX_CONTAINER = (By.XPATH, '//*[@data-name="sex"]')
    MALE_SEX = (By.XPATH, '//*[@data-name="sex"]/label[2]') #'//*[@data-name="sex"]/label[2]/input'
    MALE_SEX_INPUT = (By.XPATH, '//*[@data-name="sex"]/label[2]/input')
    AGE_FROM = (By.XPATH, '//*[@class="RangeSelector_container__HX-gb"]/div[1]')
    AGE_TO = (By.XPATH, '//*[@class="RangeSelector_container__HX-gb"]/div[2]')

    # Интересы и поведение
    INTEREST_AND_BEHAVIOUR_CONTAINER = (By.XPATH, '//*[@class="GroupForm_layout__2FvbV"]/section[2]/div[1]/div')
    INTEREST_CONTAINER = (By.XPATH, '(//*[@class="InterestsSubSection_wrap__fUg-P"])[1]')
    INTEREST_INPUT = (By.XPATH, '//*[@class="ChipsSelect_wrapper__m9y64"]/span/div/label/input')
    FIRST_SEARCH_INTEREST = (By.XPATH, '//*[@class="vkuiCustomScrollView__box"]/div[1]')
    CHOSEN_INTEREST = (By.XPATH, '//*[@aria-label="Авто"]/div/span')
    DELETE_CHOSEN_INTEREST = (By.XPATH, '//*[@aria-label="Авто"]/div/button')
    ADD_EXCLUDES = (By.XPATH, '//*[@data-name="interests"]/button')
    EXCLUDES_INPUT = (By.XPATH, '(//*[@class="ChipsSelect_wrapper__m9y64"])[2]/span/div/label/input')
    INTEREST_ERROR = (By.XPATH, '//*[@data-name="interests"]/span/div')
    DELETE_INTEREST = (By.XPATH, '(//div[contains(@class, "InterestsSubSection_header__6qVgB")])[1]//*[local-name()="svg"]')
    ADD_INTEREST = (By.XPATH, '(//*[@class="InterestsSubSection_wrap__fUg-P"])[1]/div//*[local-name()="svg"]')


    # Ключевые фразы
    KEY_PHRASES_CONTAINER = (By.XPATH, '(//*[@class="InterestsSubSection_wrap__fUg-P"])[2]')
    PHRASES_SUGGEST = (By.XPATH, '//*[@class="SuggestionsButton_button__b3AJw"]/div')
    INPUT_KEY_PHRASES = (By.XPATH, '(//*[@placeholder="Введите фразу и нажмите Enter"])[1]')
    INPUT_MINUS_PHRASES = (By.XPATH, '(//*[@placeholder="Введите фразу и нажмите Enter"])[2]')
    PHRASES_WARNINGS = (By.CLASS_NAME, 'SuggestionsDuplicates_duplicatesWarningLine__nfXaa')
    SEARCH_PERIOD = (By.XPATH, '//*[@max="30"]')
    FIELDS_CONTAINER = (By.CLASS_NAME, 'InterestsSubSection_content__VfrET')
    DELETE_KEY_PHRASES = (By.XPATH, '(//div[contains(@class, "InterestsSubSection_header__6qVgB")])[2]//*[local-name()="svg"]')
    ADD_KEY_PHRASES = (By.XPATH, '(//div[contains(@class, "InterestsSubSection_header__6qVgB")])[2]//*[local-name()="svg"]')

    # Сообщества
    COMMUNITIES_CONTAINER = (By.XPATH, '(//*[@class="InterestsSubSection_wrap__fUg-P"])[3]')
    COMMUNITIES_INPUT = (By.XPATH, '//*[@placeholder="Введите название сообщества"]')
    VK_COMMUNITIES = (By.XPATH, '(//*[@class="GroupHeader_title__H0bce"])[1]')
    OK_COMMUNITIES = (By.XPATH, '(//*[@class="GroupHeader_title__H0bce"])[2]')
    FIRST_SEARCHED = (By.XPATH, '(//*[@class="GroupContent_content__8BBSf"])[1]/div[1]')
    FIRST_SEARCHED_OK = (By.XPATH, '(//*[@class="GroupContent_content__8BBSf"])[2]/div[1]')
    COMMUNITY_COUNTER = (By.XPATH, '//*[@class="AppsAndGroupsForm_header__HNNOB"]/h4[1]')
    DELETE_GROUP = (By.XPATH, '//*[@class="Selected_item__DdUMQ"]/div')
    SELECTED_GROUP = (By.CLASS_NAME, 'Selected_item__DdUMQ')
    CANCEL_BTN = (By.XPATH, '//*[@class="AppsAndGroupsForm_header__HNNOB"]/h4[2]')
    COMMUNITIES_DELETE_ALL = (By.CLASS_NAME, 'InterestsSubSection_deleteIcon__DPjpZ')
    OPEN_COMMUNITIES = (By.XPATH, '(//div[contains(@class, "InterestsSubSection_header__6qVgB")])[3]//*[local-name()="svg"]')

    # Музыканты
    MUSICIANS_CONTAINER = (By.XPATH, '(//*[@class="InterestsSubSection_wrap__fUg-P"])[4]')
    MUSICIANS_INPUT = (By.XPATH, '//*[@placeholder="Введите название музыканта"]')
    FIRST_MUSICIAN = (By.XPATH, '//*[@class="VariantsList_list__dyFBd"]/div[1]')
    DONE_MUSICIANS_SEARCH = (By.CLASS_NAME, 'SearchInputDropdown_dropdownAction__Uk6t-')
    SELECTED_MUSICIAN_COUNTER = (By.XPATH, '//*[@class="Header_header__iyI-k"]/h4[1]')
    DELETE_SEARCHED_MUSICIAN = (By.XPATH, '//*[@class="Selected_item__Po+fb"]/div')
    SELECTED_MUSICIAN = (By.CLASS_NAME, 'Selected_item__Po+fb')
    MUSICIANS_DELETE_ALL = (By.XPATH, '//*[@class="Header_header__iyI-k"]/h4[2]')
    MUSICIANS_TRASH_BEAN = (By.CLASS_NAME, 'InterestsSubSection_deleteIcon__DPjpZ')
    OPEN_MUSICIANS = (
    By.XPATH, '(//div[contains(@class, "InterestsSubSection_header__6qVgB")])[4]//*[local-name()="svg"]')


    # Объявления
    ADVERTISEMENT_SETTINGS = (By.CLASS_NAME, 'AdForm_settings__GMx6v')
    TITLE = (By.XPATH, '(//div[contains(@class, "EditableTextField__textField")])[1]/p')
    SHORT_DESCRIPTION = (By.XPATH, '(//div[contains(@class, "EditableTextField__textField")])[2]/p')
    ABOUT = (By.XPATH, '(//div[contains(@class, "EditableTextField__textField")])[5]/p')
    MEDIAFILES_BUTTON = (By.XPATH, '(//*[@role="group"])[2]/button[1]')
    MEDIA_PICTURE = (By.XPATH, '(//*[@class="ImageItem_image__wFT85"])[2]')
    ADD_PICTURES = (By.XPATH, '//*[@data-testid="submit"]')
    IMAGES = (By.XPATH, '//*[@class="MediaContentList_flexContainer__-CZU8"]/div[3]')
    AI_IMAGE = (By.XPATH, '(//*[@class="AdMediaPreview_autogenIcon__UdC42"])[1]')
    COMPANY_NAME_ = (By.XPATH, '(//*[@class="vkuiSimpleCell__content"])[1]//span')

    # Все кампании
    COMPANY_NAME = (By.XPATH, '//*[@class="nameCellContent_content__TyfEC"]/button')
    SELECT_ALL = (By.XPATH, '(//*[@class="BaseTable__header-row"])[2]/div[1]/label/div[2]')
    # SELECT_ALL = (By.XPATH, '//*[@id="adPlan"]/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/label/div[2]')
    ACTIONS = (By.XPATH, '//*[@data-testid="select-options"]')
    DELETE_ACTION = (By.XPATH, '//*[@data-testid="archive"]')
    COMPANY_STRING = (By.XPATH, '(//*[@class="BaseTable__body"])[1]')
    COMPANY_OPTIONS = (By.XPATH, '//*[@data-testid="actions"]')
    COMPANY_DUPLICATE = (By.XPATH, '//*[@data-testid="copy"]')
    CLOSE_SUGGEST = (By.XPATH, '//*[@aria-label="Закрыть"]')
    REDACT_OBJECT = (By.XPATH, '//*[@data-name="objective"]')
    DONT_SAVE_DRAFT = (By.XPATH, '//*[@data-testid="cancel"]')

    # Для удаления всех кампаний
    BASE_PAGE = (By.XPATH, '//*[@class="header_left__cv9bp"]/button')
    COMPANIES = (By.XPATH, '//*[@data-route="dashboardV2"]')
    DUPLICATED_NAME = (By.XPATH, '(//*[@class="nameCellContent_content__TyfEC"])[1]/button')

