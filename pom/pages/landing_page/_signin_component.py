from pom.base_modal import BaseModal
from selenium.webdriver.common.by import By


class SigninComponentLocator:
    container = By.CSS_SELECTOR, ".login-form-wrapper"
    signup_link = By.CSS_SELECTOR, "p.has-account > a"
    email_field = By.CSS_SELECTOR, ".signup-form input[name='email']"
    password_field = By.CSS_SELECTOR, ".signup-form input[name='password']"
    confirm_password = By.CSS_SELECTOR, ".signup-form input[name='confirmPassword']"
    signup_btn = By.XPATH, "//button[contains(text(), 'SIGN UP')]"


lc = SigninComponentLocator


class SigninComponent(BaseModal):

    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper, lc.container)

    def sign_up(self, email_text, password_text):
        """
        -   Click signup link
        -   Fill in email, password
        -   Click signup button

        :param email_text
        :param password_text
        """
        self.driver_wrapper.click(lc.signup_link)

        self.driver_wrapper.fill_in_text_field(lc.email_field, email_text)
        self.driver_wrapper.fill_in_text_field(lc.password_field, password_text)
        self.driver_wrapper.fill_in_text_field(lc.confirm_password, password_text)

        self.driver_wrapper.click(lc.signup_btn)

    def sign_in(self, email, password):
        pass
