import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    '''
    after register
        redirect to login
        user exists in db
    '''
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert "http://localhost/auth/login" == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "select * from user where username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'User test is already registered'),
))
def test_register_validate_input(client, username, password, message):
    '''
    all required fields provided

    user not already registerd
    '''
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    '''
    login page available when not logged in

    after login
        redirect to index
        user in session
    '''
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    '''
    invalid credentials
    '''
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    '''
    after logout
        user not in session
    '''
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session

