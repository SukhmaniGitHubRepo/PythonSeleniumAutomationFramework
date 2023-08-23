# Logging means  - You can add logs to the Failure, Information, Error
# Warning to the Users

import logging


def test_print_logs():
    # Creating an object
    logger = logging.getLogger(__name__)

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    # Test messages
    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warning("Its a Warning")
    logger.error("Did you try to divide by zero")
    logger.critical("Internet is down")
