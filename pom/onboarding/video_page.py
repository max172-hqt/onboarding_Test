from pom.onboarding.onboarding_page import OnboardingPage
from selenium.webdriver.common.by import By


class VideoPage(OnboardingPage):

    video_locator = By.CSS_SELECTOR, ".video"
    continue_video_btn_locator = By.CSS_SELECTOR, ".expert-onboarding-background-video + .btn"

    def is_displayed(self):
        return (super().is_displayed()
                and
                self.driver_wrapper.is_element_visible(self.video_locator))

    def watch_video(self):
        """
        We can assume the Continue button is only enabled when
        expert finishes watching the video
        """
        continue_video_btn = self.driver_wrapper.wait_element_to_be_clickable(
            self.continue_video_btn_locator
        )

        continue_video_btn.click()
