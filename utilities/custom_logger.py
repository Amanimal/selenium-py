import logging

from utilities.settings import BASE_DIR

path = BASE_DIR / 'logs/automation.log'


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%b %d %Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
