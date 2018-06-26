from flaskr import create_app

def test_config():
    '''
    testing mode
    '''
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    '''
    hello page content
    '''
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
