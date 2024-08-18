from telnetlib import EC
import ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage


class LeverPage(BasePage):
    lever_page_button = (By.CLASS_NAME, ".postings-btn-wrapper .template-btn-submit")

    def __init__(self, driver=None):
        super().__init__(driver)
        if driver:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.lever_page_button))

    def click_lever_page_button(self):
        self.wait.until(EC.element_to_be_clickable(self.lever_page_button)).click()
