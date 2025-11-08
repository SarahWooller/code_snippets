
import logging

def simple_logger(log_filename="test.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_filename) # file handler for all messages
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler() # console handler for errors
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \n%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

logger = simple_logger()