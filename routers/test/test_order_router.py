from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)


def test_get_all_orders():
  response = client.get('/orders')
  print(response.json())
  assert response.status_code == 200
  assert response.json() == [{'order_id': 1, 'customer_id': 1, 'items_ordered': [{'product_id': 1, 'product_name': 'Rocky bites', 'product_price': '100.0','quantity_available': 5}, {'product_id': 2, 'product_name': 'Minimie', 'product_price': '50.0', 'quantity_available': 10}]}]




def test_create_order():
  response = client.post('/orders', json={'customer_id' : 2, 'items_ordered': [1,1]})
  assert response.status_code == 201
  assert response.json() == {'message': 'New Order Created', 'data': {'order_id': 2, 'customer_id': 2, 'items_ordered': [1, 1]}}





