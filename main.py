from fastapi import FastAPI
# Enabling middleware to work efficiently on importing using starlette
from starlette.middleware.base import BaseHTTPMiddleware


# importing middleware
from middleware import ecommerce_emiddleware
# importing Routers
from routers.customer_router import customer_router
from routers.product_router import product_router
from routers.order_router import order_router
from logger import logger

app = FastAPI()

# this logger for starting the app/ refresh
logger.info("Starting App")


# Including middleware to app
app.add_middleware(BaseHTTPMiddleware, dispatch=ecommerce_emiddleware)
# Including Routers
app.include_router(router=customer_router, prefix="/customer", tags=["Customer"])
app.include_router(router=product_router, prefix="/products", tags=["Products"])
app.include_router(router=order_router, prefix="/orders", tags=["Orders"])


# Initializing
@app.get('/')
def home():
  return "Welcome"