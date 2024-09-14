# Question: why are we doing deep copy
import copy
from fastapi import HTTPException
from schemas.product_schema import all_products
from schemas.order_schema import CreateOrder, all_orders

class EditOrders():
  # method for parsing orders
  @staticmethod
  def parse_order(all_orders):
    # deep copy of original order
    copied_order = copy.deepcopy(all_orders)
    # looping copied order
    for single_order in copied_order:
      modified_order = []
      # fetching product 'value' with ordered items as 'keys'
      for digit in single_order.items_ordered:
        product = all_products.get(digit)
        # append the product data to a new list
        modified_order.append(product)
        # save the new list to the items orderd to return products directly
      single_order.items_ordered = modified_order
    return copied_order
  
  # method for checking product availability before creating an order
  @staticmethod
  def check_avialability(data_in: CreateOrder):
    product_ids = data_in.items_ordered
    for product_id in product_ids:
      product = all_products.get(product_id)
      if product.quantity_available < 1:
        raise HTTPException(status_code=400, detail="Product No Longer Available")
    return data_in

  @staticmethod
  def does_order_exist(order_id: int):
    order_set = set()
    for order in all_orders:
      order_set.add(order_id)
    if not order_id in order_set:
      raise HTTPException(status_code=405, detail='order does not exit')
    return order_id




order_service = EditOrders()