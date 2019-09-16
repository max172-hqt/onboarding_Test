class Config:
    MOCK_POLICY_TAXONOMY = {
        "difficulty": "easy",
        "number_of_questions": 2,
        "problem_type": "concept",
        "taxonomy": "Max_Policy_1"
    }

    MOCK_POLICY_TAXONOMY_2 = {
        "difficulty": "easy",
        "number_of_questions": 2,
        "problem_type": "concept",
        "taxonomy": "V1.Got It Company Overview"
    }

    MOCK_SUBJECT_TAXONOMY = {
        "difficulty": "easy",
        "number_of_questions": 4,
        "problem_type": "concept",
        "taxonomy": "Max_Excel"
    }

    BASE_ADMIN_API_URL = "https://api.got-it.io/admin"

    @staticmethod
    def get_auth_token():
        with open("../auth-token.txt") as file:
            return file.read()


if __name__ == '__main__':
    print(Config.get_auth_token())
