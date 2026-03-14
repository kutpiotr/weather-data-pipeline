import logging

from app.settings import LOG_LEVEL

def get_logger(name):
    logging.basicConfig(
        level=getattr(logging,LOG_LEVEL.upper(),logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger(name)