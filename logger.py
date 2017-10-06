import logging
import os

LOG_DIR = 'logs/'
LOG_PATH = '{}test.log'.format(LOG_DIR)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(level=logging.INFO,
                    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", %(message)s}',
                    filename=LOG_PATH,
                    filemode='a+')