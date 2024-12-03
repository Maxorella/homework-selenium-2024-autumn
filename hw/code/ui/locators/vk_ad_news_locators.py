from selenium.webdriver.common.by import By


class NewsLocators:
    # заголовок
    NEWS_HEADER = (By.CLASS_NAME, 'Summary_background__PP32c')
    CLOSE_NOTIFICATION = (By.CLASS_NAME, 'NotificationModal_cancel__yzE1d')
    # about первого элемента
    ABOUT_FIRST = (By.CLASS_NAME, 'vkuiButton__content')
    FIRST_TITLE = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div/div[2]/div/div')
    # title новости
    NEWS_TITLE = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/article/div[1]/div/div/div[1]/h1')
    # Всего новостей
    NEWS_TOTAL = (By.CLASS_NAME, 'Pagination_totalText__27nVh')
    # Текущая страница
    NEWS_CURRENT_PAGE = (By.CLASS_NAME, 'vkuiPagination__page--current')
    NEWS_SECOND_PAGE = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[3]/div/div/nav/ul/li[3]/div')
    # Следующая страница
    NEXT_PAGE = (By.CLASS_NAME, 'vkuiPagination__nextButtonContainer')
    # Предыдущая страница
    PREV_PAGE = (By.XPATH, '//*[@class="vkuiPagination__prevButtonContainer"]/button')
    # last page
    LAST_PAGE = (By.XPATH, '//*[@class="vkuiPagination__list"]/li[6]')
