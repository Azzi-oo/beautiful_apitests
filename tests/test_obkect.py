import pytest

from api.post_obkect import PostObjects

payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
    }


@pytest.mark.parametrize('payload', payload)
def test_create_object(payload):
    new_object_api = PostObjects()
    new_object_api.create_object(payload=payload)
    assert new_object_api.check_status_is_(200)
    assert new_object_api.check_name_is_(payload['name'])


@pytest.mark.parametrize('name', ['ok', 'long', ''])
def test_create_objec_name(name):
    new_object_api = PostObjects()
    payload['name'] = name
    new_object_api.create_object(payload)
    assert new_object_api.check_status_is_(200)
    assert new_object_api.check_name_is_(name)


def test_get_object():
    api = PostObjects()
    api.create_object(payload=payload)
    obj_id = api.get_id()

    api.get_object(obj_id)
    assert api.check_status_is_(200)
    assert api.check_name_is_(payload['name'])


def test_update_object():
    api = PostObjects()
    api.create_object(payload=payload)
    obj_id = api.get_id()

    updated_payload = {
        "name": "Apple MacBook Pro 16 (Updated)",
        "data": {
            "year": 2023,
            "price": 2099.99,
            "CPU model": "Apple M3 Max",
            "Hard disk size": "2 TB"
        }
    }
    api.update_object(obj_id, payload=updated_payload)
    assert api.check_status_is_(200)
    assert api.check_name_is_(updated_payload['name'])


def test_delete_object():
    api = PostObjects()
    api.create_object(payload=payload)
    obj_id = api.get_id()

    api.delete_object(obj_id)
    assert api.check_status_is_(200)
