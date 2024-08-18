from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage


class HomePage(BasePage):
    insider_logo = (By.CSS_SELECTOR, "#navigation .container-fluid .navbar-brand")
    demo_button = (By.CSS_SELECTOR, "#desktop_hero_24 .home_cta_container")
    demo_text = (By.CSS_SELECTOR, "#desktop_hero_24 .d-flex p")
    company_button = (By.CSS_SELECTOR, "ul[class='navbar-nav'] li:nth-child(6)")
    career_button = (By.XPATH, "//*[text()='Careers']")

    def __init__(self, driver=None):
        super().__init__(driver)
        if driver:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.check()

    def check(self):
        self.wait.until(EC.visibility_of_element_located(self.insider_logo))
        self.wait.until(EC.visibility_of_element_located(self.demo_button))
        self.wait.until(EC.visibility_of_element_located(self.demo_text))

    def click_company_button(self):
        self.wait.until(EC.element_to_be_clickable(self.company_button)).click()

    def click_career_button(self):
        self.wait.until(EC.element_to_be_clickable(self.career_button)).click()
