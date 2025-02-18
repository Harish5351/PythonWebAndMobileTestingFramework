from selenium.webdriver.support.wait import WebDriverWait


class Basepage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.implicit_wait = 10