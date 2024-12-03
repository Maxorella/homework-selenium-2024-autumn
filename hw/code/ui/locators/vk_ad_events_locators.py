from selenium.webdriver.common.by import By


class EventsLocators:
    CLOSE_NOTIFICATION = (By.CLASS_NAME, 'NotificationModal_cancel__yzE1d')
    EVENTS_HEADER = (By.CLASS_NAME, 'Summary_background__PP32c')
    # Контейнер предстоящих мероприятий
    UPCOMING_CONTAINER = (By.XPATH, '//*[@class="pages_content__ycGet"]/div[1]')
    # Прошедшие мероприятия
    PAST_CONTAINER = (By.XPATH, '//*[@class="pages_content__ycGet"]/div[2]')
    # Заголовок мероприятия
    MAIN_EVENT_TITLE = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div[2]/div[1]')
    # Заголовок мероприятия
    EVENT_TITLE = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/article/div[1]/div/div/div/h1')
    # Ссылка на главное мероприятие
    MAIN_EVENT_HREF = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a')
    # Кнопка подробнее
    EVENT_ABOUT = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div[2]/div[3]')