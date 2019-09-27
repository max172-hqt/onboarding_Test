from pom.onboarding.onboarding_page import OnboardingPage
from selenium.webdriver.common.by import By


class WelcomePage(OnboardingPage):

    container = By.CSS_SELECTOR, ".expert-onboarding"
    onboarding_start_btn_locator = By.CSS_SELECTOR, ".expert-onboarding .btn-onboarding"

    def is_displayed(self):
        return (super().is_displayed()
                and
                self.driver_wrapper.is_element_visible(self.container))

    def start_onboarding_test(self):
        start_btn = self.driver_wrapper.wait_element_to_be_clickable(
            self.onboarding_start_btn_locator
        )

        start_btn.click()
