import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = 'chrome'
        self.url = "https://useinsider.com/"
        self.wait = None

    def setUp(self):
        self.driver = self.get_driver(self.driver)
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.driver.get(self.url)
        self.driver.maximize_window()

    def get_driver(self, driver_name):
        if driver_name == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        elif driver_name == 'firefox':
            return webdriver.Firefox()
        elif driver_name == 'safari':
            return webdriver.Safari()
        else:
            raise ValueError(f"Unsupported driver: {driver_name}")
