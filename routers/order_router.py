from fastapi import APIRouter, Depends

from schemas.order_schema import all_orders, CreateOrder, AllOrders, OrderStatus

from services.order_service import order_service

order_router = APIRouter()



@order_router.get('/', status_code=200)
def list_all_orders():
  response = order_service.parse_order(all_orders)
  return response


# creating an order but will verify if the product is avialable
@order_router.post('/', status_code=201)
def create_order(data_in: CreateOrder):
  order_id = len(all_orders) + 1
  new_order = AllOrders(order_id=order_id, customer_id=data_in.customer_id, items_ordered=data_in.items_ordered)
  all_orders.append(new_order)
  return {'message': 'New Order Created', 'data': new_order}


# Creating status
@order_router.put('/process_order/{order_id}', status_code=201)
def process_order(order_id: int = Depends(order_service.does_order_exist)):
  for order in all_orders:
    if order.order_id == order_id:
      order.status = OrderStatus.completed.value
      return {'message': 'successful', 'data': order}


@order_router.put('/process_order/{order_id}', status_code=201)
def process_order(order_id: int = Depends(order_service.does_order_exist)):
    for order in all_orders:
        if order.order_id == order_id:  # Use order_id instead of id
            order.status = OrderStatus.completed.value
            return {'message': 'successful', 'data': order}
