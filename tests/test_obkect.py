from api.post_obkect import PostObjects
import pytest


payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
    }


def test_create_object():
    new_object_api = PostObjects()
    new_object_api.create_object(payload)
    assert new_object_api.check_status_is_(200)
    assert new_object_api.check_name_is_(payload['name'])


@pytest.mark.parametrize('name', ['ok', 'long', ''])
def test_create_objec_name(name):
    new_object_api = PostObjects()
    payload['name'] = name
    new_object_api.create_object(payload)
    assert new_object_api.check_status_is_(200)
    assert new_object_api.check_name_is_(name)

    