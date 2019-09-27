from pom.base.base_page import BasePage
from selenium.webdriver.common.by import By


class SubjectTestPage(BasePage):

    base_url = "/subjects"
    subject_test_buttons_locator = By.CSS_SELECTOR, ".expert-onboarding-subjectbox .btn-onboarding-start"

    def start_excel_core(self):
        start_btn_list = self.get_subject_test_buttons()
        if len(start_btn_list) > 0:
            excel_start_btn = start_btn_list[0]
            excel_start_btn.click()

    def get_subject_test_buttons(self):
        return self.driver_wrapper.wait_elements_to_be_visible(
            self.subject_test_buttons_locator
        )
