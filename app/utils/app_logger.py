import logging
import logging.handlers as handlers
import os
import sys

from utils.config import cfg


class AppLogger:
    def __init__(self, cfg):
        self.logger = logging.getLogger(cfg.APP_NAME)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        if not os.path.exists(cfg.APP_LOGS_DIR):
            os.makedirs(cfg.APP_LOGS_DIR)
        logHandler = handlers.TimedRotatingFileHandler(os.path.join(cfg.APP_LOGS_DIR, cfg.APP_NAME + '.log'),
                                                       when='midnight', interval=1)
        logHandler.setLevel(logging.INFO)
        logHandler.setFormatter(formatter)
        self.logger.addHandler(logHandler)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(formatter)

        self.logger.addHandler(consoleHandler)


logger = AppLogger(cfg).logger
