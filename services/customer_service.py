from fastapi import HTTPException
from schemas.custormer_schema import all_customers, CreateCustomer
# using logger in dependency
from logger import logger


# dependency that makes username unique
def check_username(data_in: CreateCustomer):
  for customer in all_customers:
    if customer.customer_username == data_in.customer_username:
      logger.warning("Username Must Be Unique")
      raise HTTPException(status_code=404, detail="Username Already Exist. Please Try Again")
  return data_in


