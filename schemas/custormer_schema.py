from pydantic import BaseModel

# Getting all customer
class AllCustommers(BaseModel):
  customer_id: int
  customer_username: str
  customer_address: str

# Creating customer
class CreateCustomer(BaseModel):
  customer_username: str
  customer_address: str


# In memory database
all_customers: list[AllCustommers] = [AllCustommers(customer_id=1, customer_username="Olumighty", customer_address="7, mighty str"), AllCustommers(customer_id=2, customer_username="Oriade", customer_address="7, Ade str")]
