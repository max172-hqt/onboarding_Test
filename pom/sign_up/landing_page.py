from pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from custom_config import Config


class LandingPage(BasePage):

    login_btn = By.CSS_SELECTOR, ".navbar-btn"
    base_url = Config.BASE_EXPERT_URL

    def open_login_modal(self):
        self.driver_wrapper.click(self.login_btn)
