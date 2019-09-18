import unittest
from selenium import webdriver
from custom_config import Config
from steps.signup import SignupStep
from steps.onboarding import OnboardingStep
from steps.question_pool import QuestionPool
# from libs.account_kit import result_available, background_run
from libs.account_kit import background_run
from utilities.driver_wrapper import DriverWrapper
import threading


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.question_pool = QuestionPool()
        self.question_pool.update_all_tests()

        # self.account_kit_thread = threading.Thread(target=background_run)
        # self.account_kit_thread.setDaemon(True)

        self.driver = DriverWrapper.get_driver()

        self.signup_step = SignupStep(self.driver)
        self.onboarding_step = OnboardingStep(self.driver)

    def test_on_boarding_flow(self):
        self.driver.get(Config.BASE_EXPERT_URL)
        self.driver.maximize_window()

        self.signup_step.expert_signup()
        self.signup_step.expert_verify_email()

        background_run()
        # self.account_kit_thread.start()
        # result_available.wait()

        self.onboarding_step.on_boarding_flow()

    def tearDown(self):
        self.driver.close()
        self.question_pool.reset_all_tests()
        # TODO: reset to original question pool


if __name__ == '__main__':
    unittest.main()
