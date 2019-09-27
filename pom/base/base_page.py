from pom.base.base_pom import BasePOM
from selenium.common.exceptions import TimeoutException


class BasePage(BasePOM):
    base_url = None

    def open(self):
        self.driver_wrapper.open(self.base_url)

    def is_displayed(self):
        if self.base_url is None:
            raise Exception("Base Url empty")

        try:
            self.driver_wrapper.wait_until(
                lambda dw: self.base_url in self.driver_wrapper.current_url()
            )
            return True
        except TimeoutException:
            print("Take too long")
            return False
