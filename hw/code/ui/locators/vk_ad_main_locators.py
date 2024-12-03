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
    SVG_LOGO = (By.XPATH, '//*[@class="content_logo__GA44t"]/a/svg')
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


class MainPageNoLoginCarouselLoc:

    # div карусели
    CAROUSEL_CONTAINER = (By.CLASS_NAME, 'styles_slider__S9aAm')
    # контейнер кружков карусели
    CAROUSEL_BULLETS_CONTAINER = (By.CLASS_NAME, 'Bullets_wrapper__pQBJR')
    # кнопка взаимодействия
    CAROUSEL_HANDLE_BTN = (By.CLASS_NAME, 'vkuiButton__in')
    # До 10000 бонусов
    MAIN_PAGE_CAROUSEL_TEXT_1_1 = (By.XPATH, '//*[@id="title"]/p[1]')
    # на первую кампанию
    MAIN_PAGE_CAROUSEL_TEXT_1_2 = (By.XPATH, '//*[@id="title"]/p[2]')
    # Акция для тех, у кого еще нет кабинета в VK Рекламе. Переходите по кнопке ниже, чтобы узнать подробности
    MAIN_PAGE_CAROUSEL_TEXT_1_3 = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/p')
    # Получить бонус
    MAIN_PAGE_CAROUSEL_TEXT_1_BTN = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[1]/div[1]/a/button/span[1]/span')

    # кнопка 1
    MAIN_PAGE_CAROUSEL_ROUND_BTN_1 = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[1]')

    # кнопка 2
    MAIN_PAGE_CAROUSEL_ROUND_BTN_2 = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[2]')

    # кнопка 3
    MAIN_PAGE_CAROUSEL_ROUND_BTN_3 = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[3]')

    # Реклама
    MAIN_PAGE_CAROUSEL_TEXT_2_1 = (By.XPATH, '//*[@id="title"]/p[1]')
    # для любых целей
    MAIN_PAGE_CAROUSEL_TEXT_2_2 = (By.XPATH, '//*[@id="title"]/p[2]')
    # вашего бизнеса
    MAIN_PAGE_CAROUSEL_TEXT_2_3 = (By.XPATH, '//*[@id="title"]/p[3]')

    # VK Реклама подходит для продвижения сайтов любой тематики, сообществ ВКонтакте и ОК, мобильных приложений, сбора лидов и охватных кампаний
    MAIN_PAGE_CAROUSEL_TEXT_2_4 = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/p')

class MainPageNoLoginCases:
    # блок кэйсов
    CASES_CONTAINER = (By.CLASS_NAME, 'styles_section__kQovd')
    # примеры кейсов
    CASES_EXAMPLES = (By.CLASS_NAME, 'styles_cols__Iavf_')
    # переход к странице кейсов
    CASES_HREF = (By.CLASS_NAME, 'styles_all__wnH9i')
    # переход к кейсу
    CHOSEN_CASE = (By.CLASS_NAME, 'Case_link__B_za3')
    # заголовок кейса
    CASE_TITLE = (By.CLASS_NAME, 'Case_title__JAisY')
    # заголовок страницы кейса
    CASE_PAGE_TITLE = (By.CLASS_NAME, 'Summary_content__yWIpY')

class MainPageNoLoginCookie:
    # контейнер куки
    COOKIE_CONTAINER = (By.CLASS_NAME, 'CookieBanner_wrapper___Pfqg')

class MainPageNoLoginEducate:
    # контейнер блока
    EDUCATE_CONTAINER = (By.CLASS_NAME, 'GetStarted_wrapper__cTNLj')
    # кнопка блока
    EDUCATE_ABOUT = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[3]/a/div[1]/button/span[1]')

class MainPageNoLoginNews:
    #контейнер блока
    NEWS_CONTAINER = (By.CLASS_NAME, 'News_cols__L6uYy')
    # кнопка блока
    NEWS_ABOUT = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[4]/div/a/div/div[2]/button/span[1]')

class MainPageNoLoginFooter:
    # контейнер футера
    FOOTER_CONTAINER = (By.TAG_NAME, 'footer')
    # лого
    FOOTER_LOGO = (By.CLASS_NAME, 'Footer_logo__pwCXU')
    # переход в аккаунт
    TO_ACCOUNT = (By.CLASS_NAME, 'ButtonCabinet_primary__LCfol')
    # разделы
    FOOTER_SECTIONS = (By.CLASS_NAME, 'Footer_menuTitle__TrNAn')
    FOOTER_SECTIONS_LI = (By.CLASS_NAME, 'Footer_item__uymLH')
    # ссылка на навости
    FOOTER_NEWS = (By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[1]/div[2]/ul/li[1]/a')
    # ссылка на материалы
    FOOTER_MATERIALS = (By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[1]/div[2]/ul/li[3]/a')
    # ссылка на документы
    FOOTER_DOCUMENTS = (By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[1]/div[2]/ul/li[7]/a')
    # лого ВК
    FOOTER_VK_LOGO = (By.CLASS_NAME, 'Footer_logoVKBusiness__dMZUT')
    # social ссылки
    FOOTER_SOCIAL = (By.CLASS_NAME, 'Footer_leftControls__25wO6')
    # переключение языка
    FOOTER_LANGUAGES = (By.CLASS_NAME, 'SelectLanguage_wrapper__id9eU')
    # меню языков
    FOOTER_CHOOSE_LANGUAGES = (By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div/div/div')
    FOOTER_CHOOSE_ENGLISH = (By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div/div/div/h5/div/span[1]')
