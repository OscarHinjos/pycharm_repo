from conexion_bbd import *
from logs import *
def actualizar_personas(valor):
    nuevo_valor = f'%{valor}'
    cambio = f'@{valor}'
    try:
        conexion = conexion_bbd()
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "UPDATE `personas` SET `email` = CONCAT(left(`personas`.`email`, locate('@', `personas`.`email`) - 1), %s) WHERE `personas`.`email` NOT LIKE %s"
                cursor.execute(sentencia, (cambio, nuevo_valor))
                conexion.commit()
                registros_actualizados = cursor.rowcount
                log.debug(f'Registros Actualizados: {registros_actualizados}')
    except Exception as e:
        log.error(f'Ocurrió un error: {e}')
    finally:
        cursor.close()
        conexion.close()
        log.info("Fin")