from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)


def test_get_customer():
    # Testing the correct '/' route
    response = client.get('/customers')
    # Debugging output to see the error message
    print(response.json())  # Optional for debugging
    assert response.status_code == 200
    assert response.json() == {'message': 'successful', 'data': [{'customer_id': 1, 'customer_username': 'Olumighty', 'customer_address': '7, mighty str'}, {'customer_id': 2, 'customer_username': 'Oriade', 'customer_address': '7, Ade str'}]}

def test_create_customer():
    response = client.post('/customers', json={'customer_username': 'Yussuf Baba', 'customer_address': '3, baba str'})
    assert response.status_code == 201
    assert response.json().get('data').get('customer_username') == 'Yussuf Baba'
    assert response.json() == {'message': 'Customer Created Successfully', 'data': {'customer_id': 3,
        'customer_username': 'Yussuf Baba', 'customer_address': '3, baba str'}}


def test_edit_customer():
    response = client.put('/customers/1', json={'customer_id': 1, 'customer_username': 'Omoarde', 'customer_address': '1, Arde str'})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'message': 'Customer Updated Successfully', 'data': {'customer_id': 1,'customer_username': 'Omoarde', 'customer_address': '1, Arde str'}}

