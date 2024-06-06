def test_row_endpoint(client):
    response = client.put("/table/append/row")

    assert response.status_code == 200
