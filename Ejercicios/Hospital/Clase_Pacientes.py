#Importaciones
import Clase_Persona
from random import *

#Funcion que elige un sintoma aleatorio de enfermedades y lo devuelve
def enfermedad_aleatoria():
    lista_enfermedades = ["Absceso pulmonar","Abetalipoproteinemia","Acantosis nigricans","Acefalía"]
    ramdom_enfermedad = choice(lista_enfermedades)
    return ramdom_enfermedad

#Clase paciente
class Pacientes(Clase_Persona.Persona):

    def __init__(self, nombre, apellido, dni, sintomas):
        super().__init__(nombre, apellido, dni)
        self.sintomas = sintomas



#Pacientes
paciente1 = Pacientes("Sara","Vera","5555D",enfermedad_aleatoria())
paciente2 = Pacientes("Juanjo","Diaz","6666F",enfermedad_aleatoria())
paciente3 = Pacientes("Andres","Casco","7777G",enfermedad_aleatoria())
paciente4 = Pacientes("Delia","Iglesias","8888H",enfermedad_aleatoria())

#Lista con los pacientes
lista_pacientes = [paciente1,paciente2,paciente3,paciente4]