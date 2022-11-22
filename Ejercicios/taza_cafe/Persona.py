from abc import ABC,abstractmethod

class Persona(ABC):

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        