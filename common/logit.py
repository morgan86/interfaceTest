import logging


def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("example_logger")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("../interfaceTest/logs/test.log")

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


def exception(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object

    @exception(logger)
    def zero_divide():
        1 / 0
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception
                err = "There was an exception in function: "
                err += func.__name__
                logger.exception(err)

                # re-raise the exception
                raise

        return wrapper

    return decorator
