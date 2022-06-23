import os
import logging

LOGGER_TYPE = os.environ.get("LOGGER_TYPE")


def setup_logger():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s | %(message)s")
    handler.setFormatter(formatter)
    if LOGGER_TYPE == "console":
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger = logging.getLogger("authentication_service")
    logger.setLevel(level)
