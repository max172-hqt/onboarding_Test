from pom.base_pom import BasePOM
from urllib.parse import urlparse


class BasePage(BasePOM):

    def __init__(self, driver_wrapper, base_url):
        self.base_url = base_url
        super().__init__(driver_wrapper)

    def open(self):
        self.driver_wrapper.open(self.base_url)

    def is_displayed(self):
        assert self.base_url in self.driver_wrapper.current_url()
