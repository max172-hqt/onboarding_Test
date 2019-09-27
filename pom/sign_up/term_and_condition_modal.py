from pom.base.base_modal import BaseModal
from selenium.webdriver.common.by import By


class TermAndConditionModal(BaseModal):

    container = By.ID, "modal-terms-and-conditions"
    term_and_condition_next_btn_locator = By.CSS_SELECTOR, ".modal-footer button.gi-Button--primary"

    def click_next(self):
        next_btn_terms_conditions = self.driver_wrapper.wait_element_to_be_clickable(
            self.term_and_condition_next_btn_locator
        )

        next_btn_terms_conditions.click()
