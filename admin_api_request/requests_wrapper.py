import requests
from requests.exceptions import HTTPError
from custom_config import Config
from urllib.parse import urljoin


class AdminRequest:

    base_url = Config.BASE_ADMIN_API_URL

    default_request_headers = {
        'Authorization': Config.get_auth_token(),
        'X-GotIt-Vertical': 'Excel',
    }

    def __init__(self, url=base_url, headers=None, params=None, payload=None):
        if headers is None:
            self.headers = self.default_request_headers
        else:
            self.headers = headers

        self.requests = requests
        self.url = url
        self.params = params
        self.payload = payload

    def set_path(self, path):
        self.url = urljoin(self.base_url, path)

    def add_headers(self, additional_header_dict=None):
        self.headers = {**self.headers, **additional_header_dict}

    def http_get(self):
        try:
            response = self.requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    def http_put(self):
        try:
            response = self.requests.put(self.url, headers=self.headers, data=self.payload)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()


