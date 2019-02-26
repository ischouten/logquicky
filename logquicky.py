import logging
from logging.handlers import RotatingFileHandler
import sys

def get(logger_name):
  return logging.getLogger(logger_name)


def add(logger_name, file=None, rewrite=False, screen=True, level=logging.INFO):
    log = logging.getLogger(logger_name)

    logging.addLevelName(30, "WARN")

    logging.addLevelName(logging.WARN, "\033[35m%s\033[0m" % logging.getLevelName(logging.WARN))
    logging.addLevelName(logging.INFO, "\033[32m%s\033[0m" % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.ERROR, "\033[31m%s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.DEBUG, "\033[34m%s\033[0m" % logging.getLevelName(logging.DEBUG))

    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    if file:
        file_handler = RotatingFileHandler(file, mode='a', maxBytes=1000000, backupCount=2, encoding='utf-8')
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

    if screen:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        if rewrite:
            stream_handler.terminator = ""
        log.addHandler(stream_handler)

    log.setLevel(level)

    return log
