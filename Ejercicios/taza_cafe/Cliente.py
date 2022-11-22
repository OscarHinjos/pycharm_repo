import Persona
import logging as log

log.basicConfig(filename='logs/bar.log', encoding='utf-8', level=log.DEBUG)
import TooColdTemperatureException
import TooColdTemperatureException


class Cliente(Persona.Persona):

    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)

    def tomar_taza(self, taza_cafe):
        def tomar_taza(self, tazacafe):
            log.info("El cliente {} se está tomado la taza de cafe".format(self.nombre))
            if tazacafe.temperatura > 60:
                # log.info("El cliente {} ha dicho que el cafe estaba muy caliente".format(self.nombre))
                raise TooHotTemperatureException("Cafe muy caliente")
            elif tazacafe.temperatura < 40:
                # log.info("El cliente {} ha dicho que el cafe estaba muy frio".format(self.nombre))
                raise TooColdTemperatureException("Cafe muy frio")


cliente1 = Cliente("Juana", "2222B")
