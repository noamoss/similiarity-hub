def test_homepage(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'Hello, World!?'
