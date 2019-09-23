from pom.base_pom import BasePOM
from selenium.webdriver.common.by import By


class QuestionPageComponentLocator:
    container = By.CSS_SELECTOR, "#onboarding-test-answer-screen"
    answers_radio_locator = By.CSS_SELECTOR, ".expert-onboarding-answers li input"
    progress_text_locator = By.CSS_SELECTOR, "#onboarding-test-question-progress span"
    continue_test_btn_locator = By.XPATH, "//button[text()='CONTINUE']"


lc = QuestionPageComponentLocator


class QuestionPageComponent(BasePOM):

    def is_displayed(self):
        self.driver_wrapper.wait_element_to_be_visible(lc.container)

    def answer_test(self, answer_correct=True):
        for i in range(self._get_num_questions()):
            answer_list = self.driver_wrapper.wait_elements_to_be_visible(
                lc.answers_radio_locator
            )

            answer = answer_list[0] if answer_correct else answer_list[1]

            self.driver_wrapper.wait_until(
                lambda wd: not answer.is_selected()
            )

            answer.click()
            continue_btn = self.driver_wrapper.wait_element_to_be_clickable(
                lc.continue_test_btn_locator
            )

            continue_btn.click()

    def _get_num_questions(self):
        """
        Number of question in the current test
        """
        progress_text = self.driver_wrapper.wait_element_to_be_visible(
            lc.progress_text_locator
        )

        return int(progress_text.text[-1])

