from fastapi import APIRouter

from schemas.order_schema import all_orders, CreateOrder, AllOrders

from services.order_service import order_service

order_router = APIRouter()



@order_router.get('/')
def list_all_orders():
  response = order_service.parse_order(all_orders)
  return response


# creating an order but will verify if the product is avialable
@order_router.post('/')
def create_order(data_in: CreateOrder):
  order_id = len(all_orders) + 1
  new_order = AllOrders(order_id=order_id, customer_id=data_in.customer_id, items_ordered=data_in.items_ordered)
  all_orders.append(new_order)
  return {'message': 'New Order Created', 'data': new_order}