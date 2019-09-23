from pom.base_modal import BasePOM
from selenium.webdriver.common.by import By
from libs.account_kit import background_run


class EmailVerificationModalLocator:
    account_kit_iframe_locator = By.XPATH, "//body[@class='landing-expert']/div/iframe[1]"
    account_kit_next_btn_locator = By.CSS_SELECTOR, "button[type='submit']"


lc = EmailVerificationModalLocator


class EmailVerificationModal(BasePOM):

    def is_displayed(self):
        self.driver_wrapper.switch_to_frame_and_perform_action(
            lc.account_kit_iframe_locator,
            self._click_next
        )

    @staticmethod
    def verify_email():
        background_run()

    def _click_next(self):
        """
        Send Account Kit verification email
        """
        next_btn = self.driver_wrapper.wait_element_to_be_clickable(
            lc.account_kit_next_btn_locator
        )
        next_btn.click()
