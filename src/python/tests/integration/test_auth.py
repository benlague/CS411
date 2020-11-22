import os

import pytest
import requests

HOST = os.environ.get('API_HOST', 'http://localhost:8001')
USER_ENDPOINT = '/api/auth/user'
REGISTER_ENDPOINT = '/api/auth/register'
LOGIN_ENDPOINT = '/api/auth/login'


@pytest.fixture
def session():
    return requests.Session()


@pytest.mark.run(order=1)
def test_register_user(session):
    body = {
        "email": "user@email.com",
        "password": "123",
        "first_name": "Foo",
        "last_name": "Baz"
    }
    resp = session.post(url=f'{HOST}{REGISTER_ENDPOINT}', json=body)
    assert resp.status_code == 201


@pytest.mark.run(order=2)
def test_login_user(session):
    body = {
        "email": "user@email.com",
        "password": "123",
    }
    resp = session.post(url=f'{HOST}{LOGIN_ENDPOINT}', json=body)
    assert resp.status_code == 200
    assert 'session' in resp.cookies


@pytest.mark.run(order=3)
def test_get_user(session):
    resp = session.get(url=f'{HOST}{USER_ENDPOINT}')
    user_data = resp.json()
    assert resp.status_code == 200
    assert user_data.get('email') == 'user@email.com'


@pytest.mark.run(order=4)
def test_update_user(session):
    body = {
        "first_name": "buz"
    }
    resp = session.post(url=f'{HOST}{USER_ENDPOINT}', json=body)
    assert resp.status_code == 202


@pytest.mark.run(order=5)
def test_get_user_after_update(session):
    resp = session.get(url=f'{HOST}{USER_ENDPOINT}')
    user_data = resp.json()
    assert resp.status_code == 200
    assert user_data.get('first_name') == 'buz'


@pytest.mark.run(order=6)
def test_delete_user(session):
    resp = session.delete(url=f'{HOST}{USER_ENDPOINT}')
    assert resp.status_code == 204
    assert 'session' not in resp.cookies
