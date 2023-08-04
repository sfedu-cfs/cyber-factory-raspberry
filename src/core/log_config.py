import os

from loguru import logger

log_file = os.path.join(os.getcwd(), "logs", "app.log")
logger.add(log_file, level="DEBUG", format="{time} - {level} - {message} - "
                                           "in function: {function} - File: {file}")
