import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler("logs/bbd.log"),
                    log.StreamHandler()
                ])

def debug(*message):
    log.debug(message)


def info(*message):
    log.info(message)


def warn(*message):
    log.warning(message)


def error(*message):
    log.error(message)


def critical(*message):
    log.critical(message)