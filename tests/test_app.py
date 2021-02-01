def test_add_item(client) -> None: 
    # testing invalid cart item
    response_invalid = client.post('/add-item', data=dict(item=1, quantity='bad'))
    assert response_invalid.status_code == 400
    # testing valid cart item
    response_valid = client.post('add-item', data=dict(item=1, quantity=1))
    assert response_valid.status_code == 302

def test_remove_item(client) -> None:
    # testing valid cart item removal
    response_invalid = client.post('/remove-item/1')
    assert response_invalid.status_code == 302

def test_update_quantity(client) -> None:
    # testing invalid query parameters
    response_invalid = client.post('/update-quantity/1?foo=bar')
    assert response_invalid.status_code == 400
    # testing valid query parameters
    response_valid = client.post('/update-quantity/1?action=increment')
    assert response_valid.status_code == 302
