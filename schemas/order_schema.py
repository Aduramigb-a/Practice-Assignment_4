from pydantic import BaseModel

class AllOrders(BaseModel):
  order_id: int
  customer_id: int
  items_ordered: list[int]



class CreateOrder(BaseModel):
  customer_id: int
  items_ordered: list[int]

# IN memory database
all_orders: list[AllOrders] = [AllOrders(order_id=1, customer_id=1, items_ordered=[1, 2])]
