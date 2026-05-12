import requests

from api.base_api import BaseApi


class PostObjects(BaseApi):
    endpoint = '/objects'

    def create_object(self, payload):
        self.response = requests.post(
            self.base_url + self.endpoint,
            json=payload
        )

    def get_object(self, obj_id):
        self.response = requests.get(
            f'{self.base_url}{self.endpoint}/{obj_id}'
        )

    def update_object(self, obj_id, payload):
        self.response = requests.put(
            f'{self.base_url}{self.endpoint}/{obj_id}',
            json=payload
        )

    def delete_object(self, obj_id):
        self.response = requests.delete(
            f'{self.base_url}{self.endpoint}/{obj_id}'
        )

    def check_name_is_(self, name):
        assert self.response.json()['name'] == name

    def get_id(self):
        return self.response.json()['id']
