# importing library:
import logging

# creating custom logger:
def custom_logger(log_dir):
    """creating custom_logger"""

    log_format = '%(levelname)s %(funcName)s %(asctime)s %(message)s'
    logging.basicConfig(filename=log_dir,
                        level = logging.DEBUG,
                        format = log_format,
                        datefmt = '%m-%d-%Y %I:%M:%S')
    logger = logging.getLogger()

    return logger