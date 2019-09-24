from pom.base.base_pom import BasePOM
from selenium.common.exceptions import TimeoutException


class BasePage(BasePOM):

    def __init__(self, driver_wrapper, base_url, check_is_displayed=True):
        self.base_url = base_url
        super().__init__(driver_wrapper, check_is_displayed)

    def open(self):
        self.driver_wrapper.open(self.base_url)

    def is_displayed(self):
        try:
            self.driver_wrapper.wait_until(
                lambda dw: self.base_url in self.driver_wrapper.current_url()
            )
            return True
        except TimeoutException:
            print("Take too long")
            return False
