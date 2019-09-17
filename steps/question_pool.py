import requests
from custom_config import Config
import json


class QuestionPool:

    """
        This class will set up precondition for the test
        Given 2 mock pools, for Policy tests and Subject test

        Policy test: Max_Policy_1
        Subject test: Max_Excel

        For each test
        -   Delete current pool
        -   Assign mock pool to the only pool
        -   TODO: Set first answer to be correct, others to be wrong
    """

    headers = {
        'Authorization': Config.get_auth_token(),
        'X-GotIt-Vertical': 'Excel',
        # 'Content-Type': 'application/json'
    }

    def __init__(self):
        self.requests = requests

    def get_test_by_name(self, test_name):
        payload = {'funnel': 'A'}
        url = Config.BASE_ADMIN_API_URL + "/onboarding-tests"
        response = self.requests.get(url, headers=self.headers, params=payload)

        if response.status_code == 200:
            json_response = response.json()['data']
            matches = [test for test in json_response if test_name in test['name']]
            return matches[0] if len(matches) == 1 else None

    def get_all_tests_name(self):
        """
        :return: List of tests on Funnel A
        """
        payload = {'funnel': 'A'}
        url = Config.BASE_ADMIN_API_URL + "/onboarding-tests"
        response = self.requests.get(url, headers=self.headers, params=payload)

        if response.status_code == 200:
            json_response = response.json()['data']
            matches = [test['name'] for test in json_response]
            return matches

    def update_all_tests(self):
        list_test_name = self.get_all_tests_name()

        for test_name in list_test_name:
            test = self.get_test_by_name(test_name)
            self._update_test(test)

    def _update_test(self, test):
        """
        Update current test with mock pool
        -   Get the test object from API
        -   Update the pool and send Put request back to server

        :param test: Current test dictionary
        """
        if 'id' not in test or 'VBA' in test['name']:
            return

        url = Config.BASE_ADMIN_API_URL + "/onboarding-tests/" + str(test['id'])
        print(url)
        get_test_response = self.requests.get(url, headers=self.headers)

        if get_test_response.status_code != 200:
            return

        test_response = get_test_response.json()['data']

        # Build payload
        if "Policy" in test['name']:
            test_response['pools'] = [Config.MOCK_POLICY_TAXONOMY]
        else:
            test_response['pools'] = [Config.MOCK_SUBJECT_TAXONOMY]

        test_response.pop('name')
        test_response.pop('status')
        test_response.pop('subject_id')
        test_response = json.dumps(test_response)

        print(test_response)

        custom_headers = self.headers.copy()
        custom_headers['Content-Type'] = 'application/json'

        update_test_response = self.requests.put(url, headers=custom_headers, data=test_response)
        print(update_test_response.status_code)

        if update_test_response.status_code == 200:
            print('response' + str(update_test_response.json()))


if __name__ == '__main__':
    q = QuestionPool()
    q.update_all_tests()
