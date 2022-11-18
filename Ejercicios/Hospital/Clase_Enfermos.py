#Importaciones
import Clase_Persona


class Enfermos(Clase_Persona.Persona):

    def __init__(self, nombre, apellido, dni, enfermedad):
        super().__init__(nombre, apellido, dni)
        self.enfermedad = enfermedad



