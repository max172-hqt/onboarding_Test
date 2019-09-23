from pom.base_pom import BasePOM
from selenium.webdriver.common.by import By


class PassTestPageComponentLocator:
    container = By.CSS_SELECTOR, "#onboarding-test-passed-screen"
    continue_pass_btn_locator = By.CSS_SELECTOR, "#onboarding-test-passed-screen button"


lc = PassTestPageComponentLocator


class PassTestPageComponent(BasePOM):

    def is_displayed(self):
        self.driver_wrapper.wait_element_to_be_visible(lc.container)

    def click_continue(self):
        continue_btn = self.driver_wrapper.wait_element_to_be_clickable(
            lc.continue_pass_btn_locator
        )
        continue_btn.click()
