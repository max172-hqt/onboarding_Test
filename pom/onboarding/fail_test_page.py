from pom.onboarding.onboarding_page import OnboardingPage
from selenium.webdriver.common.by import By


class FailTestPage(OnboardingPage):

    container = By.CSS_SELECTOR, "#onboarding-test-failed-screen"
    retry_btn_locator = By.CSS_SELECTOR, ".btn-danger.btn-onboarding"

    def is_displayed(self):
        return (super().is_displayed()
                and
                self.driver_wrapper.is_element_visible(self.container))

    def click_retry(self):
        retry_button = self.driver_wrapper.wait_element_to_be_clickable(
            self.retry_btn_locator
        )
        retry_button.click()
