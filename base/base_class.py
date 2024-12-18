import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Метод отображения URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """Метод сохранения скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screnshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\79803\\PycharmProjects\\TheStore\\screen\\' + name_screenshot)

