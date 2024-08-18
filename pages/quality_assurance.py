from selenium.webdriver.support import expected_conditions as EC
import ec
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage
from pages.quality_assurance_departmant import QualityAssuranceDepartmant


class QualityAssurance(BasePage):
    qa_jobs = (By.CLASS_NAME, ".btn-outline-secondary")


    def __init__(self, driver=None):
        super().__init__(driver)
        if driver:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.qa_jobs))


    def click_qa_jobs(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.qa_jobs)).click()
            return QualityAssuranceDepartmant(self.driver)
        except exceptions.NoSuchElementException as e:
            print(f"Error: The qa jobs button was not clicked. {e}")