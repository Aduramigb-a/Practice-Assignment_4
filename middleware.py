from fastapi import Request
import time
# using loggers in middlewares for more info
from logger import logger

async def ecommerce_emiddleware(request: Request, call_next):
  logger.info("Starting Request")
  start_time = time.time()
  response = await call_next(request)
  process_time = time.time() - start_time
  response.headers["X-Process-Time"] = str(process_time)
  logger.info(f"Ended Request. Process time: {process_time}")
  return response
