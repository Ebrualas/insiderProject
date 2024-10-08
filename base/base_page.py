from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def driver(self):
        return self.driver

