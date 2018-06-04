import logging
import functools
import os
import datetime
import pathlib

from data_connections import get_config


def logger_set_up(file_name):
    """
     Set up function for logging of autonoms files
    """
    # get logs folder path from config
    path = pathlib.Path(get_config('config')['logs_path'])

    # get current date in same format as current log files for filename
    dt = datetime.datetime.today().strftime('%Y_%m_%d')

    # create logging instance
    logger = logging.getLogger(file_name)

    # set logging level
    logger.setLevel(logging.DEBUG)

    # ensure folders present
    try:
        (pathlib.Path("{}".format(path)) / dt).mkdir(parents=True, exist_ok=True)
    except:
        print ('probably some windows path bug?')
    # set handlers for stdout and file logging
    stdout_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("{}/{}/{}.log".format(path, dt, os.path.basename(file_name)[:-3]))

    # set formatter for both handlers
    formatter = logging.Formatter('[%(asctime)s]: {}: %(levelname)s: %(message)s'.format(
                                  os.path.basename(file_name)))

    # Add formatter to handlers
    stdout_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger


class log_with(object):
    """
        Logging decorator that allows logging of every function called
        Parameter should be a logging instance created by calling the logger_set_up() from within the
        module the decorator will be used
    """

    ENTRY_MESSAGE = "Starting {}"
    EXIT_MESSAGE = "Exiting {}"

    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        """
            Returns a wrapper that logs start and end of function
        """

        @functools.wraps(func)
        def wrapper(*args, **kwgs):
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))

            f_result = func(*args, **kwgs)
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))

            return f_result
        return wrapper