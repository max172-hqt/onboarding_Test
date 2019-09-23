from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from custom_config import Config
import os


class DriverWrapper:
    default_wait_time = 10

    def __init__(self, driver):
        """
        Temporarily set type for Type hinting feature to work

        :type driver: webdriver.Firefox
        """
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def wait_element_to_be_clickable(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_element_to_be_present(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def wait_element_to_be_visible(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_elements_to_be_visible(self, locator, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_until(self, condition, time=default_wait_time):
        return WebDriverWait(self.driver, time).until(
            condition
        )

    def switch_to_frame_and_perform_action(self, locator, action, time=default_wait_time):
        """
        Switch to Iframe, perform action and switch back
        :param locator: Iframe locator
        :param action: Custom function
        :param time
        """
        try:
            WebDriverWait(self.driver, time).until(
                EC.frame_to_be_available_and_switch_to_it(locator)
            )

            action()
            self.driver.switch_to.default_content()

        except TimeoutException:
            print("Loading took too much time!")

    def get_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException:
            print("Element not found")

    def get_elements(self, locator):
        return self.driver.find_element(*locator)

    def fill_in_text_field(self, text_field_locator, text):
        el = self.get_element(text_field_locator)
        el.send_keys(text)

    def click(self, locator):
        el = self.get_element(locator)
        el.click()

    def shutdown(self):
        self.driver.quit()

    def screen_shot(self, timestamp, scenario, step):
        screenshot_name = os.path.join(
            Config.SCREEN_SHOT_DIR,
            "{} {} {}.png".format(timestamp, scenario, step)
        )
        result = self.driver.save_screenshot(screenshot_name)

        if result:
            print("Save successfully")
        else:
            print("Error")
