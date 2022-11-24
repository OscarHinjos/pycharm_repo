from abc import ABC, abstractmethod
from metodos import *


class Persona:
    def __int__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


p = Persona('aaa', 'ccc')

print(p.nombre)
