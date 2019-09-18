import html
import re
from selenium import webdriver
import threading

from selenium.webdriver.common.by import By

# from common.browser import get_driver
# from common.config import config

from custom_config import Config
from libs.gmail import GmailService

# result_available = threading.Event()

def _login_with_selenium(url):
    """
    Open link and confirm login via selenium
    :param url: the url to be opened
    :return:
    """
    driver = webdriver.Firefox()

    driver.get(url)
    login_button = None
    try:
        login_button = driver.find_element(
            by=By.CSS_SELECTOR, value='button[type="submit"]'
        )
    except:
        pass

    if login_button is not None:
        login_button.click()

    driver.quit()


def _login_account_kit(mail):
    """
    Find url in the email and the login through that url
    :param mail:
    :return:
    """
    # retrieve message link
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', mail["content"])

    url = ""
    if urls:
        url = html.unescape(urls[0])

    print("Found an email from accountkit for: " + mail["to"])
    print(url)
    _login_with_selenium(url)


def run():
    gmail_service = GmailService(Config.TEST_GOOGLE_EMAIL, Config.TEST_GOOGLE_PASSWORD)
    while True:
        mails = gmail_service.get_latest_unread_emails(sender="Account Kit")
        for mail in mails:
            _login_account_kit(mail)


def background_run():
    gmail_service = GmailService(Config.TEST_GOOGLE_EMAIL, Config.TEST_GOOGLE_PASSWORD)

    while True:
        mails = gmail_service.get_latest_unread_emails(sender="Account Kit")

        if mails:
            for mail in mails:
                _login_account_kit(mail)
            # result_available.set()
            break


if __name__ == '__main__':
    run()
