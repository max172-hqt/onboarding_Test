from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_config import Config
import time


class SignupStep:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def expert_signup(self):
        driver = self.driver

        login_button = driver.find_element_by_css_selector(".navbar-btn")
        login_button.click()
        signup_link = driver.find_element_by_css_selector("p.has-account > a")
        signup_link.click()

        email_field = driver.find_element_by_css_selector(".signup-form input[name='email']")
        password_field = driver.find_element_by_css_selector(".signup-form input[name='password']")
        confirm_password_field = driver.find_element_by_css_selector(".signup-form input[name='confirmPassword']")

        email = self._generate_email()
        print(email)
        email_field.send_keys(email)
        password_field.send_keys(Config.TEST_GOOGLE_PASSWORD)
        confirm_password_field.send_keys(Config.TEST_GOOGLE_PASSWORD)

        signup_btn = driver.find_element_by_xpath("//button[contains(text(), 'SIGN UP')]")
        signup_btn.click()

    def expert_verify_email(self):
        driver = self.driver

        try:
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//body[@class='landing-expert']/div/iframe[1]"))
            )

        except TimeoutException:
            print("Loading took too much time!")

        try:
            next_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )

            next_btn.click()
            driver.switch_to.default_content()

        except TimeoutException:
            print("Loading took too much time!")


    @staticmethod
    def _generate_email():
        current_timestamp = time.time()
        return "testautomation.gotitpro+expert_+{}@gmail.com".format(current_timestamp)
