from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from custom_config import Config
from utilities.driver_wrapper import DriverWrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SignupStep:

    login_btn_locator = By.CSS_SELECTOR, ".navbar-btn"
    signup_link_locator = By.CSS_SELECTOR, "p.has-account > a"
    email_field_locator = By.CSS_SELECTOR, ".signup-form input[name='email']"
    password_field_locator = By.CSS_SELECTOR, ".signup-form input[name='password']"
    confirm_password_field_locator = By.CSS_SELECTOR, ".signup-form input[name='confirmPassword']"
    signup_btn_locator = By.XPATH, "//button[contains(text(), 'SIGN UP')]"
    account_kit_iframe_locator = By.XPATH, "//body[@class='landing-expert']/div/iframe[1]"
    account_kit_next_btn_locator = By.CSS_SELECTOR, "button[type='submit']"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.dw = DriverWrapper(self.driver)

    def expert_signup(self):
        login_button = self.dw.get_element(self.login_btn_locator)
        login_button.click()
        signup_link = self.dw.get_element(self.signup_link_locator)
        signup_link.click()

        email_field = self.dw.get_element(self.email_field_locator)
        password_field = self.dw.get_element(self.password_field_locator)
        confirm_password_field = self.dw.get_element(self.confirm_password_field_locator)

        email = self._generate_email()
        email_field.send_keys(email)
        password_field.send_keys(Config.TEST_GOOGLE_PASSWORD)
        confirm_password_field.send_keys(Config.TEST_GOOGLE_PASSWORD)

        signup_btn = self.dw.get_element(self.signup_btn_locator)
        signup_btn.click()

    def expert_verify_email(self):
        driver = self.driver

        try:
            self.dw.wait_iframe_available_and_switch_to_it(self.account_kit_iframe_locator)
            # WebDriverWait(driver, 10).until(
            #     EC.frame_to_be_available_and_switch_to_it(self.account_kit_iframe_locator)
            # )

            next_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.account_kit_next_btn_locator)
            )

            next_btn.click()

            driver.switch_to.default_content()
        except TimeoutException:
            print("Loading took too much time!")

    @staticmethod
    def _generate_email():
        current_timestamp = time.time()
        return "testautomation.gotitpro+expert_+{}@gmail.com".format(current_timestamp)
