def test_ready_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.json
    assert 'status' in data
    assert 'time' in data


def test_http_exception(client):
    response = client.get('/notfound')
    assert response.status_code == 404
    data = response.json
    assert data['error'] == 'NotFound'
    assert data['message'] == '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'