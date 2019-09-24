from pom.base.base_modal import BasePOM
from selenium.webdriver.common.by import By


class EmailVerificationModal(BasePOM):

    account_kit_iframe_locator = By.XPATH, "//body[@class='landing-expert']/div/iframe[1]"
    account_kit_next_btn_locator = By.CSS_SELECTOR, "button[type='submit']"

    def is_displayed(self):
        return self.driver_wrapper.is_iframe_displayed(self.account_kit_iframe_locator)
        # return True

    def send_email_verification(self):
        """
        Send Account Kit verification email
        """
        self.driver_wrapper.switch_to_frame_and_perform_action(
            self.account_kit_iframe_locator,
            self._click_next
        )

    def _click_next(self):
        next_btn = self.driver_wrapper.wait_element_to_be_clickable(
            self.account_kit_next_btn_locator
        )

        next_btn.click()
