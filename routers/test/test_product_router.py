from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)


def test_get_all_product():
  response = client.get('/products')
  assert response.status_code == 200
  assert response.json() == {'message': 'Successful', 'data': {'1': {'product_id': 1, 'product_name': 'Rocky bites', 'product_price': '100.0', 'quantity_available': 5}, '2': {'product_id': 2, 'product_name': 'Minimie', 'product_price': '50.0', 'quantity_available': 10}}}





def test_create_product():
  response = client.post('/products', json={'product_name': 'chicken', 'product_price': '1000', 'quantity_available': 10})
  assert response.status_code == 201
  assert response.json() == {'message': 'Product Created Successfully', 'data': {'product_id': 3, 'product_name': 'chicken', 'product_price': '1000', 'quantity_available': 10}}



def test_edit_product():
  response = client.put('/products/3', json={'product_name': 'Happy Happy', 'product_price': '100', 'quantity_available': '150'})
  assert response.status_code == 200
  assert response.json() == {'message': 'Update Successful', 'data': {'product_id': 3,'product_name': 'Happy Happy', 'product_price': '100', 'quantity_available': 150}}


def test_wrong_id_inputed():
  response = client.put('/products/9', json={'product_name': 'chicken', 'product_price': '1000', 'quantity_available': 1})
  assert response.status_code == 404
  assert response.json() == {'detail' : 'Id Not Found!'}
