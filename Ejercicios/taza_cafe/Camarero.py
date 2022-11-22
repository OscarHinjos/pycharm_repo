import Persona
import taza_cafe
from random import *
import logging as log
log.basicConfig(filename='logs/bar.log',encoding='utf-8', level=log.INFO)


class Camarero(Persona.Persona):

    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)

    def servir_cafe(self):
        log.info(f"El camarero sirve al cliente el cafe")
        taza_cafe1 = taza_cafe.Taza_Cafe(taza_cafe.tipo_cafe_aleatorio(), randint(0,100))
        log.info(f"El camarero crea un {taza_cafe1.tipo_cafe}")
        return taza_cafe1


camarero1 = Camarero("Juan", "111A")


