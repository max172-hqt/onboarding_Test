import os
import time
from datetime import datetime



class Config:

    BROWSER = 'FIREFOX'
    BASE_EXPERT_URL = "https://expert-excel.got-it.io/"
    BASE_ADMIN_API_URL = "https://api.got-it.io/"
    GMAIL_SMTP_SERVER = "imap.gmail.com"
    TEST_GOOGLE_EMAIL = "testautomation.gotitpro@gmail.com"
    TEST_GOOGLE_PASSWORD = "#Test@automation123456"
    NUM_MINI_POLICY_TESTS = 4
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    SCREEN_SHOT_DIR = ROOT_DIR + "/screenshots"

    MOCK_POLICY_TAXONOMY = [{
        "difficulty": "easy",
        "number_of_questions": 2,
        "problem_type": "concept",
        "taxonomy": "Max_Policy_1"
    }]

    MOCK_POLICY_TAXONOMY_2 = [{
        "difficulty": "easy",
        "number_of_questions": 2,
        "problem_type": "concept",
        "taxonomy": "V1.Got It Company Overview"
    }]

    MOCK_SUBJECT_TAXONOMY = [{
        "difficulty": "easy",
        "number_of_questions": 4,
        "problem_type": "concept",
        "taxonomy": "Max_Excel"
    }]

    @staticmethod
    def get_auth_token():
        with open("auth-token.txt") as file:
            return file.read()

    @staticmethod
    def get_current_date_time():
        return datetime.fromtimestamp(time.time())


if __name__ == '__main__':
    print(Config.get_current_date_time())
