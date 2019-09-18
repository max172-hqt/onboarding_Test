from custom_config import Config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DriverWrapper:
    default_browser_name = Config.BROWSER
    default_wait_time = 10

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_driver(browser_name=None):
        if browser_name is not None:
            driver = DriverWrapper.browser_by_name(browser_name)
        else:
            driver = DriverWrapper.browser_by_name(DriverWrapper.default_browser_name)

        return driver

    @staticmethod
    def browser_by_name(browser_name):
        if browser_name == 'FIREFOX':
            driver = webdriver.Firefox()
        elif browser_name == 'CHROME':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        return driver

    def wait_element_to_be_clickable(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_element_to_be_present(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def wait_iframe_available_and_switch_to_it(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

    def get_element(self, locator):
        try:
            by, value = locator
            element = self.driver.find_element(by, value)
            return element
        except NoSuchElementException:
            print("Element not found")
