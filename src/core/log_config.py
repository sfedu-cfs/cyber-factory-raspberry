import os

from loguru import logger

log_file = os.path.join(os.path.dirname(__file__), "../../log/app.log")
logger.add(log_file, level="DEBUG", format="{time} - {level} - {message} - "
                                           "in function: {function} - File: {file}")
