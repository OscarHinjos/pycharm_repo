import MySQLdb
from logs import log


def conexion_bbd():
    try:
        mybd = MySQLdb.connect(
            host="localhost",
            user="root",
            password="password",
            database="curso_python")
    except MySQLdb.Error as mybde:
        log.error("La conexion con la base de datos no se pudo realizar")

    else:
        log.info("Conexion establecida")

    return mybd
