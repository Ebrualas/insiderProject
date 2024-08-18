from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage
from pages.quality_assurance import QualityAssurance


class CareersPage(BasePage):
    insider_locations_text = (By.CSS_SELECTOR, "#career-our-location .category-title-media")
    insider_teams = (By.XPATH, "//*[text()='See all teams']")
    insider_life = (By.XPATH, "//*[text()='Life at Insider']")
    insider_quality_assurance = (By.XPATH, "(text()='Quality Assurance'")

    def __init__(self, driver=None):
        super().__init__(driver)
        if driver:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.insider_locations_text))
        self.wait.until(ec.visibility_of_element_located(self.insider_teams))
        self.wait.until(ec.visibility_of_element_located(self.insider_life))

    def click_insider_teams(self):
        teams = self.driver.find_elements_by_xpath(self.insider_teams)
        self.driver.execute_script("arguments[0].scrollIntoView();", teams)
        self.wait.until(EC.element_to_be_clickable(self.insider_teams)).click()

    def click_insider_quality_assurance(self):
        self.wait.until(EC.element_to_be_clickable(self.insider_quality_assurance)).click()
        return QualityAssurance(self.driver)

