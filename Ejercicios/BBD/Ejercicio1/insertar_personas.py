from conexion_bbd import *
from logs import log


def insertar_personas():
    try:
        conexion = conexion_bbd()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO personas (nombre, apellido, email) VALUES(%s,%s,%s)"
                valores = (
                    ('Persona1', 'Apellido1', 'email@hotmail.es'),
                    ('Persona2', 'Apellido2', 'email@gmail.com'),
                    ('Persona3', 'Apellido3', 'email@hotmail.es')
                )
                cursor.executemany(sql, valores)
                conexion.commit()
                registros_insertados = cursor.rowcount
                log.info(f"Registros Insertados: {registros_insertados}")
    except Exception as e:
        log.error(f"Ocurrio un error {e}")
    finally:
        cursor.close()
        conexion.close()
        log.info("Inserts realizados")