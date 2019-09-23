from pom.base_pom import BasePOM


class BaseModal(BasePOM):

    def __init__(self, driver_wrapper, container_locator):
        self.container_locator = container_locator
        super().__init__(driver_wrapper)

    def is_displayed(self):
        self.driver_wrapper.wait_element_to_be_visible(self.container_locator)
