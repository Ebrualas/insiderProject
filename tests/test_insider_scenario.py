
from selenium.webdriver import ActionChains
from base.base_test import BaseTest
from pages.careers_page import CareersPage
from pages.home_page import HomePage


class TestInsiderScenario(BaseTest):

    def test_insider_scenario(self):
        print("1. Visit https://useinsider.com/ and check Insider home page")
        home_page = HomePage(self.driver)
        home_page.click_company_button()
        home_page.click_career_button()

        print("2.Go to career page and clicks teams button")
        carriers_page = CareersPage(self.driver)
        carriers_page.click_insider_teams()
        quality_assurance = carriers_page.click_insider_quality_assurance()

        print("3.Go to quality assurance page and selects quality assurance role")
        quality_assurance_departmant = quality_assurance.click_qa_jobs()
        quality_assurance_departmant.click_location_button()
        quality_assurance_departmant.click_location_tr()
        quality_assurance_departmant.click_department_button()

        print("4.Filters the quality assurance jobs")
        quality_assurance_departmant.department_qa()
        jobs = quality_assurance_departmant.get_job_position()
        for job in jobs:
            hover = ActionChains(self.driver).move_to_element(job)
            hover.perform()
            self.assertIn("Quality Assurance", job.get_text())
            self.assertIn("İstanbul, Turkey", job.get_text())
            break

        print("5.Clicks View role and check the Lever Page")
        lever_page = quality_assurance_departmant.click_view_role_button()
        lever_page.click_lever_page_button()

        self.driver.quit()


