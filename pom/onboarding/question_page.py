from pom.onboarding.onboarding_page import OnboardingPage
from selenium.webdriver.common.by import By


class QuestionPage(OnboardingPage):

    container = By.CSS_SELECTOR, "#onboarding-test-answer-screen"
    answers_radio_locator = By.CSS_SELECTOR, ".expert-onboarding-answers li input"
    progress_text_locator = By.CSS_SELECTOR, "#onboarding-test-question-progress span"
    continue_test_btn_locator = By.XPATH, "//button[text()='CONTINUE']"

    def is_displayed(self):
        return (super().is_displayed()
                and
                self.driver_wrapper.is_element_visible(self.container))

    def answer_test(self, answer_correct=True):
        for i in range(self._get_num_questions()):
            answer_list = self.driver_wrapper.wait_elements_to_be_visible(
                self.answers_radio_locator
            )

            answer = answer_list[0] if answer_correct else answer_list[1]

            self.driver_wrapper.wait_until(
                lambda wd: not answer.is_selected()
            )

            answer.click()
            continue_btn = self.driver_wrapper.wait_element_to_be_clickable(
                self.continue_test_btn_locator
            )

            continue_btn.click()

    def _get_num_questions(self):
        """
        Number of question in the current test
        """
        progress_text = self.driver_wrapper.wait_element_to_be_visible(
            self.progress_text_locator
        )

        return int(progress_text.text[-1])

