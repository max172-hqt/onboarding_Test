from pom.base_page import BasePage
from selenium.webdriver.common.by import By
from pom.pages.landing_page._signin_component import SigninComponent
from custom_config import Config


class LandingPageLocators:
    login_btn = By.CSS_SELECTOR, ".navbar-btn"


lc = LandingPageLocators


class LandingPage(BasePage):

    base_url = Config.BASE_EXPERT_URL

    def __init__(self, driver_wrapper):
        self._signin_component = SigninComponent(driver_wrapper)
        super().__init__(driver_wrapper, self.base_url)

    def click_login(self):
        self.driver_wrapper.click(lc.login_btn)

    def sign_up(self, email, password):
        self._signin_component.is_displayed()
        self._signin_component.sign_up(email, password)
