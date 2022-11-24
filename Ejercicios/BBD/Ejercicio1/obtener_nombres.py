from conexion_bbd import *
from logs import log
def obtener_nombres():
    try:
        conexion = conexion_bbd()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "SELECT nombre FROM personas"
                cursor.execute(sql)
                registros = cursor.fetchall()
                for row in registros:
                    log.info(row[0])
    except Exception as e:
        log.error(f"Ocurrio un error: {e}")
    finally:
        cursor.close()
        conexion.close()
        log.info("Fin")