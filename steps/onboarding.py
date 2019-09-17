from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_config import Config


class OnboardingStep:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def on_boarding_flow(self):
        """
        -   Pass policy tests
        -   Fail subject test
        -   Pass subject test second attempt
        """
        driver = self.driver

        try:
            next_btn_terms_conditions = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )

            next_btn_terms_conditions.click()

            start_btn_onboarding = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".expert-onboarding .btn-onboarding"))

            )

            start_btn_onboarding.click()
            self._answer_policy_tests()
            self._excel_test_failed_attempt()
            self._excel_test_passed_attempt()

        except TimeoutException:
            print("Take too much time")

    def _answer_policy_tests(self):
        """
        -   For each mini policy test
        -   Watch video
        -   Answer correctly
        """
        for i in range(Config.NUM_MINI_POLICY_TESTS):
            self._watch_video()
            self._answer_questions()

    def _watch_video(self):
        """
        Wait for Continue button to be clickable
        """
        continue_video_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".expert-onboarding-background-video + .btn"))
        )

        continue_video_btn.click()

    def _excel_test_failed_attempt(self):
        """
        -   On Subject page
        -   Take Excel Core test
        -   Choose second answer
        -   Fail test
        """
        driver = self.driver

        start_excel_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h3[text()='Excel']/parent::div//a"))
        )

        start_excel_btn.click()
        self._answer_questions(False)

    def _excel_test_passed_attempt(self):
        """
        -   Click Retry on failed page
        -   Answer correct
        """
        driver = self.driver

        retry_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-danger.btn-onboarding"))
        )
        retry_button.click()
        self._answer_questions()

    def _answer_questions(self, answer_correct=True):
        """
        -   Get number of questions
        -   Wait question loading
        -   For each question, choose first answer
        -   Wait success page and continue
        """
        driver = self.driver

        if answer_correct:
            by_answer_css = ".expert-onboarding-answers li:first-child input"
        else:
            by_answer_css = ".expert-onboarding-answers li:nth-child(2) input"

        progress_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#onboarding-test-question-progress span"))
        )

        # format: '1 of 2'
        question_num = int(progress_text.text[-1])

        for i in range(question_num):
            first_answer = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, by_answer_css))
            )
            first_answer.click()

            continue_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='CONTINUE']"))
            )
            continue_btn.click()

        if answer_correct:
            continue_pass_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#onboarding-test-passed-screen button"))
            )
            continue_pass_btn.click()

