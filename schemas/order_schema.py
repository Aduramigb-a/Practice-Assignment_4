from pydantic import BaseModel
# using enum for order status
from enum import Enum

# using enum

class OrderStatus(Enum):
  completed = 'COMPLETED'
  pending = "PENDING"


print(OrderStatus.completed.value)


class AllOrders(BaseModel):
  order_id: int
  customer_id: int
  items_ordered: list[int]
  status: str = OrderStatus.pending.value




class CreateOrder(BaseModel):
  customer_id: int
  items_ordered: list[int]

# IN memory database
all_orders: list[AllOrders] = [AllOrders(order_id=1, customer_id=1, items_ordered=[1, 2])]
