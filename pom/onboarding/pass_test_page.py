from pom.onboarding.onboarding_page import OnboardingPage
from selenium.webdriver.common.by import By


class PassTestPage(OnboardingPage):

    container = By.CSS_SELECTOR, "#onboarding-test-passed-screen"
    continue_pass_btn_locator = By.CSS_SELECTOR, "#onboarding-test-passed-screen button"

    def is_displayed(self):
        return (super().is_displayed()
                and
                self.driver_wrapper.is_element_visible(self.container))

    def click_continue(self):
        continue_btn = self.driver_wrapper.wait_element_to_be_clickable(
            self.continue_pass_btn_locator
        )
        continue_btn.click()
