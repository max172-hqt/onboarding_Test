import unittest
from selenium import webdriver
from custom_config import Config
from steps.signup import SignupStep
from steps.onboarding import OnboardingStep


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.signup_step = SignupStep(self.driver)
        self.onboarding_step = OnboardingStep(self.driver)

    def test_on_boarding_flow(self):
        self.driver.get(Config.BASE_EXPERT_URL)
        self.driver.maximize_window()

        self.signup_step.expert_signup()
        self.signup_step.expert_verify_email()

        self.onboarding_step.on_boarding_flow()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
