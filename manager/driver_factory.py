from selenium import webdriver
from manager.driver_wrapper import DriverWrapper


def get_browser_wrapper(browser_name):
    if browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    _set_up_driver(driver)
    return DriverWrapper(driver)


def _set_up_driver(driver):
    driver.maximize_window()


