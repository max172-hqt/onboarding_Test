from pom.base_modal import BaseModal
from selenium.webdriver.common.by import By


class TermAndConditionModalLocator:
    container = By.ID, "modal-terms-and-conditions"
    term_and_condition_next_btn_locator = By.CSS_SELECTOR, "button[type='submit']"


lc = TermAndConditionModalLocator


class TermAndConditionModal(BaseModal):

    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper, lc.container)

    def click_next(self):
        next_btn_terms_conditions = self.driver_wrapper.wait_element_to_be_clickable(
            lc.term_and_condition_next_btn_locator
        )

        next_btn_terms_conditions.click()
