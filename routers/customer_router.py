from fastapi import APIRouter, HTTPException, Depends
from schemas.custormer_schema import all_customers, CreateCustomer, AllCustommers
from services.customer_service import check_username
customer_router = APIRouter()


# get all customer
@customer_router.get('/', status_code=200)
def show_all_customers():
  return {'message': 'successful', 'data': all_customers}


#create new customer
@customer_router.post('/', status_code=201)
def create_new_customer(data_in: CreateCustomer = Depends(check_username)):
  customer_id = len(all_customers) + 1
  new_customer = AllCustommers(customer_id=customer_id, customer_username=data_in.customer_username, customer_address=data_in.customer_address)
  all_customers.append(new_customer)
  return {'message': 'Customer Created Successfully', 'data': new_customer}

# Updating a Customer
@customer_router.put('/{customer_id}', status_code=200)
def update_customer(customer_id: int, data_in: CreateCustomer ):
  for customer in all_customers:
    if customer.customer_id == customer_id:
      customer.customer_username = data_in.customer_username
      customer.customer_address = data_in.customer_address
      return {'message': 'Customer Updated Successfully', 'data': customer}
  raise HTTPException(status_code=404, detail="Customer not found")
