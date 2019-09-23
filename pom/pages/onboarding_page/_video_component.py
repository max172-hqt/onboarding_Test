from pom.base_pom import BasePOM
from selenium.webdriver.common.by import By


class VideoComponentLocator:
    continue_video_btn_locator = By.CSS_SELECTOR, ".expert-onboarding-background-video + .btn"
    video_locator = By.CSS_SELECTOR, ".video"


lc = VideoComponentLocator


class VideoComponent(BasePOM):

    def is_displayed(self):
        self.driver_wrapper.wait_element_to_be_visible(lc.video_locator)

    def watch_video(self):
        """
        We can assume the Continue button is only enabled when
        expert finishes watching the video
        """
        continue_video_btn = self.driver_wrapper.wait_element_to_be_clickable(
            lc.continue_video_btn_locator
        )
        continue_video_btn.click()
