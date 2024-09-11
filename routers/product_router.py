from fastapi import APIRouter, HTTPException
from schemas.product_schema import all_products, CreateProduct, AllProducts


product_router = APIRouter()


# get all produc
@product_router.get('/', status_code=200)
def get_all_products():
  return {'message': 'Successful', 'data': all_products}


# create new product
@product_router.post('/', status_code=202)
def create_product(data_in: CreateProduct):
  product_id = len(all_products) + 1
  new_product = AllProducts(product_id=product_id, product_name=data_in.product_name, product_price=data_in.product_price, quantity_available=data_in.quantity_available)
  all_products[product_id] = new_product
  return {'message': 'Product Created Successfully', 'data': new_product}


# edit a product
@product_router.put('/{product}', status_code=200)
def edit_product(validate_id: int, data_in: CreateProduct):
  product = all_products.get(validate_id)
  if product:
    product.product_name = data_in.product_name
    product.product_price = data_in.product_price
    product.quantity_available == data_in.quantity_available
    return {'message': 'Update Successful', 'data': product}
  raise HTTPException(status_code=404, detail='Id Not Found!')