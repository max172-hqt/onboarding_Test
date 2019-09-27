from pom.base.base_pom import BasePOM
from selenium.common.exceptions import TimeoutException


class BaseModal(BasePOM):
    container = None

    def __init__(self, driver_wrapper, check_is_displayed=True):
        super().__init__(driver_wrapper, check_is_displayed)

    def is_displayed(self):
        if self.container is None:
            raise Exception("Missing container")

        try:
            self.driver_wrapper.wait_element_to_be_visible(self.container)
            return True
        except TimeoutException:
            print("Take too long")
            return False
