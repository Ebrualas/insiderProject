from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage
from pages.lever_page import LeverPage


class QualityAssuranceDepartmant(BasePage):
    qa_jobs = (By.CLASS_NAME, ".btn-outline-secondary")
    location_button = (By.XPATH, '//span[contains( @class, "select2-selection--single"')
    location_tr = (By.XPATH, '//li[contains( @class, "select2-results__option") and text()="Istanbul, Turkey"]')
    department_button = (By.XPATH, '//span[contains( @class, "select2-selection__rendered"')
    department_qa = (By.XPATH, '//li[contains( @class, "select2-results__option") and text()="Quality Assurance"]')
    jobs_list = (By.CLASS_NAME, "position-list-item")
    view_role = (By.XPATH, "//*[text()='View Role']")


    def __init__(self, driver=None):
        super().__init__(driver)
        if driver:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 15, poll_frequency=1.5)
        self.check()

    def check(self):
        self.wait.until(EC.visibility_of_element_located(self.location_button))
        self.wait.until(EC.visibility_of_element_located(self.department_button))


    def click_qa_jobs(self):
        self.wait.until(EC.element_to_be_clickable(self.qa_jobs)).click()

    def click_location_button(self):
        self.wait.until(EC.element_to_be_clickable(self.location_button)).click()

    def click_location_tr(self):
        self.wait.until(EC.element_to_be_clickable(self.location_tr)).click()

    def click_department_button(self):
        self.wait.until(EC.element_to_be_clickable(self.department_button)).click()

    def click_department_qa(self):
        self.wait.until(EC.element_to_be_clickable(self.department_qa)).click()

    def get_job_position(self):
        jobs = self.driver.find_elements_by_class_name(self.jobs_list)
        self.driver.execute_script("arguments[0].scrollIntoView();", jobs)
        return self.wait.until(EC.element_to_be_clickable(self.jobs_list))

    def click_view_role_button(self):
        self.wait.until(EC.element_to_be_clickable(self.view_role)).click()
        return LeverPage(self.driver)