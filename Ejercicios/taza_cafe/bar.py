import Cliente as CL
import Camarero as CA
import taza_cafe as TC
import logging as log
import TooHotTemperatureException
import TooColdTemperatureException

log.basicConfig(filename='logs/bar.log', encoding='utf-8', level=log.DEBUG)


class Bar:

    def __init__(self, camarero):
        self.camarero = camarero

    def acciones_bar(self, cliente):
        try:
            taza_cafe = self.camarero.servir_cafe()
            cliente.tomar_taza(taza_cafe)
        except TooHotTemperatureException as thte:
            log.error(thte.message)
            log.error("El camarero le pone un vaso de agua")
        except TooColdTemperatureException as tcte:
            log.error(tcte.message)
            log.error("El camarero le calienta más el café")
        except Exception as e:
            log.error("Al cliente le pasa algo")
        else:
            log.info("El cliente {} se ha tomado el café muy agusto a {} grados".format(cliente.nombre,
                                                                                        taza_cafe.temperatura))


if __name__ == "__main__":
    bar = Bar(CA.camarero1)
    bar.acciones_bar(CL.cliente1)
