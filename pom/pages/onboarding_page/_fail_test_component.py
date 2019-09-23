from pom.base_pom import BasePOM
from selenium.webdriver.common.by import By


class FailTestPageComponentLocator:
    container = By.CSS_SELECTOR, "#onboarding-test-failed-screen"
    retry_btn_locator = By.CSS_SELECTOR, ".btn-danger.btn-onboarding"


lc = FailTestPageComponentLocator


class FailTestPageComponent(BasePOM):

    def is_displayed(self):
        self.driver_wrapper.wait_elements_to_be_visible(lc.container)

    def click_retry(self):
        retry_button = self.driver_wrapper.wait_element_to_be_clickable(
            lc.retry_btn_locator
        )
        retry_button.click()
