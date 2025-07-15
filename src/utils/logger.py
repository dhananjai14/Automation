import logging
import os
from datetime import datetime


# Logging level DEBUG, INFO, WARNING, ERROR 


def get_logger() -> logging.Logger:
    logger = logging.getLogger("main_logger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        os.makedirs("logs", exist_ok=True)
        file_name = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
        file_handler = logging.FileHandler(f"logs/{file_name}.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
