from loguru import logger

logger.add("../../logs/app.log", level="DEBUG", format="{time} - {level} - {message} - "
                                                       "in function: {function} - File: {file}")
