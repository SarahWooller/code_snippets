"""Simply sets up a basic logger. By default it will setup the log as path.log in the same directory as
  path.py - the python file calling the logger"""

import logging
import inspect

def simple_logger(log_filename=""):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # set up the path to the filehandler
    if not log_filename:
        caller_filename = [f.filename for f in inspect.stack()][-1]
        log_filename = f"{caller_filename[:-3]}.log"
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


