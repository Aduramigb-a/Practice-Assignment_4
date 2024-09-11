# import python built in module logging
import logging

# import sys for stream handlers which will make logs appear at the console
import sys

# create a logger object in the module
logger = logging.getLogger()

# create the formater: This tells how the log messages will look
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')


# create the handlers: They descide where the logs go to, screen(console) or file
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')


# add formaters to the handlers to determine how they'll show
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)



# Now assign the handlers to the logger object to tell it what to do each time it is being logged
logger.handlers = [stream_handler, file_handler]


# set logger level. Minimum important message to provide
logger.setLevel(logging.INFO)



# N:B -- A logger can be added anywhere in the application to provide more context. Maybe before raising an error. Just import the logger and choose your message type E.g Warning