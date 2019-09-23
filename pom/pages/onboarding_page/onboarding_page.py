from pom.base_page import BasePage
from selenium.webdriver.common.by import By
from pom.pages.onboarding_page._video_component import VideoComponent
from pom.pages.onboarding_page._question_component import QuestionPageComponent
from pom.pages.onboarding_page._fail_test_component import FailTestPageComponent
from pom.pages.onboarding_page._pass_test_component import PassTestPageComponent
from custom_config import Config


class OnboardingPageLocator:
    onboarding_start_btn_locator = By.CSS_SELECTOR, ".expert-onboarding .btn-onboarding"


lc = OnboardingPageLocator


class OnboardingPage(BasePage):

    base_url = "/onboarding"

    def __init__(self, driver_wrapper):

        self._video_component = VideoComponent(driver_wrapper)
        self._question_component = QuestionPageComponent(driver_wrapper)
        self._pass_test_component = PassTestPageComponent(driver_wrapper)
        self._fail_test_component = FailTestPageComponent(driver_wrapper)

        super().__init__(driver_wrapper, self.base_url)

    def start_onboarding_test(self):
        start_btn = self.driver_wrapper.wait_element_to_be_clickable(
            lc.onboarding_start_btn_locator
        )
        start_btn.click()

    def pass_policy_test(self):
        for i in range(Config.NUM_MINI_POLICY_TESTS):
            self._video_component.is_displayed()
            self._video_component.watch_video()

            self._question_component.is_displayed()
            self._question_component.answer_test()

            self._pass_test_component.is_displayed()
            self._pass_test_component.click_continue()

    def perform_excel_core_test(self, passing=True):
        self._question_component.is_displayed()

        if passing:
            self._question_component.answer_test(answer_correct=True)
        else:
            self._question_component.answer_test(answer_correct=False)

    def is_success_page_displayed(self):
        self._pass_test_component.is_displayed()
        self._pass_test_component.click_continue()

    def is_fail_page_displayed(self):
        self._fail_test_component.is_displayed()
