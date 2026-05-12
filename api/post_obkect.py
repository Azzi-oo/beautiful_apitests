import requests

from api.base_api import BaseApi


class PostObjects(BaseApi):
    endpoint = '/objects'
    
    def create_object(self, payload):
        self.response = requests.post(
            self.base_url + self.endpoint,
            json=payload
        )
        
    def check_name_is_(self, name):
        assert self.response.json()['name'] == name
