from custom_config import Config
import json
from admin_api_request.requests_wrapper import AdminRequest


class QuestionPool:

    def __init__(self):
        self.new_policy_pool = Config.MOCK_POLICY_TAXONOMY
        self.new_subject_pool = Config.MOCK_SUBJECT_TAXONOMY
        self.old_pools = {}

    @staticmethod
    def _get_all_tests():
        """
        :return: json response of all tests
        """
        get_all_tests_req = AdminRequest()
        get_all_tests_req.set_path("admin/onboarding-tests")
        get_all_tests_req.params = {'funnel': 'A'}

        return get_all_tests_req.http_get()['data']

    @staticmethod
    def _get_test_by_name(test_name):
        """
        Get json response of test based on test name
        :param test_name: Test name
        :return: Test json response
        """
        tests = QuestionPool._get_all_tests()
        matches = [test for test in tests if test_name in test['name']]
        return matches[0] if len(matches) == 1 else None

    @staticmethod
    def _get_all_tests_name():
        """
        :return: List of tests on Funnel A
        """
        tests = QuestionPool._get_all_tests()
        matches = [test['name'] for test in tests]
        return matches

    @staticmethod
    def _get_test_by_id(test_id):
        get_test_by_id_req = AdminRequest()
        get_test_by_id_req.set_path(f"admin/onboarding-tests/{test_id}")
        url = get_test_by_id_req.url
        return url, get_test_by_id_req.http_get()['data']

    def update_all_tests(self):
        list_test_name = QuestionPool._get_all_tests_name()

        for test_name in list_test_name:
            test = QuestionPool._get_test_by_name(test_name)
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

        url, test_response = QuestionPool._get_test_by_id(test['id'])

        self.old_pools.update({test['name']: test_response['pools']})

        if "Policy" in test['name']:
            test_response = self._build_req_payload(test_response, self.new_policy_pool)
        else:
            test_response = self._build_req_payload(test_response, self.new_subject_pool)

        update_test_req = AdminRequest()
        update_test_req.url = url
        update_test_req.add_headers({'Content-Type': 'application/json'})
        print(update_test_req.headers)
        update_test_req.payload = test_response
        response = update_test_req.http_put()
        print('response' + str(response))

    @staticmethod
    def _build_req_payload(test_response, pools):
        test_response['pools'] = pools
        test_response.pop('name')
        test_response.pop('status')
        test_response.pop('subject_id')

        return json.dumps(test_response)

    def reset_all_tests(self):
        list_test_name = QuestionPool._get_all_tests_name()

        for test_name in list_test_name:
            test = QuestionPool._get_test_by_name(test_name)
            self._reset_test(test)

    def _reset_test(self, test):
        if 'id' not in test or 'VBA' in test['name']:
            return

        url, test_response = QuestionPool._get_test_by_id(test['id'])
        original_pools = self.old_pools[test['name']]
        test_response = self._build_req_payload(test_response, original_pools)

        update_test_req = AdminRequest()
        update_test_req.url = url
        update_test_req.add_headers({'Content-Type': 'application/json'})
        update_test_req.payload = test_response

        response = update_test_req.http_put()
        print('response' + str(response))



