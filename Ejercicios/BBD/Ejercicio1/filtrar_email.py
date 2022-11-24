from conexion_bbd import *
from logs import log


def filtro_email(valor):
    log.debug(f"show_mail_filter con parametro {valor}")
    new_value = f'%{valor}'
    try:
        conexion = conexion_bbd()
        cursor = conexion.cursor()
        sentencia = 'SELECT * FROM `personas` WHERE `email` LIKE %s'

        cursor.execute(sentencia, [new_value])
        registros = cursor.fetchall()
        log.info(registros)

    except Exception as e:
        log.error("Error", e)

    finally:
        cursor.close()
        conexion.close()
        log.info("Fin")
