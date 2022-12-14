import logging as log
from fileinput import filename

#log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler("logs/orquesta.log"),
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

def genera_mensaje(mensajes):
    reply = ""
    for mensaje in mensajes:
        reply += str(mensaje)

    return reply