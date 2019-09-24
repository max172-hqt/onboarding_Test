from pom.base.base_page import BasePage


class OnboardingPage(BasePage):

    base_url = "/onboarding"

    def __init__(self, driver_wrapper, check_is_displayed=True):
        super().__init__(driver_wrapper, self.base_url, check_is_displayed)
