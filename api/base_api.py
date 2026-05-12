import requests


class BaseApi:
    base_url = 'https://restful-api.dev'
    endpoint: str
    response: requests.Response

    def check_status_is_(self, status):
        return self.response.status_code == status
