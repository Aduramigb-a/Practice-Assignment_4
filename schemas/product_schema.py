from pydantic import BaseModel
from decimal import Decimal

class AllProducts(BaseModel):
  product_id: int
  product_name: str
  product_price: Decimal
  quantity_available: int


class CreateProduct(BaseModel):
  product_name: str
  product_price: Decimal
  quantity_available: int




# all products database
all_products = {
  1: AllProducts(product_id=1, product_name="Rocky bites", product_price=Decimal("100.0"), quantity_available=5),
  2: AllProducts(product_id=2, product_name="Minimie", product_price=Decimal("50.0"), quantity_available=10)
  }