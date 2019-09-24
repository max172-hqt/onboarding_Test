from pom.base.base_pom import BasePOM
from selenium.common.exceptions import TimeoutException


class BaseModal(BasePOM):

    def __init__(self, driver_wrapper, container_locator, check_is_displayed=True):
        self.container_locator = container_locator
        super().__init__(driver_wrapper, check_is_displayed)

    def is_displayed(self):
        try:
            self.driver_wrapper.wait_element_to_be_visible(self.container_locator)
            return True
        except TimeoutException:
            print("Take too long")
            return False
