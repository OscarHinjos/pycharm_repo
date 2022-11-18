import Clase_Doctor as CDoctor
import Clase_Pacientes as CPacientes
import Clase_Enfermeros as CEnfermos
from random import *


class Consulta():

    def __init__(self,doctor):
        self.doctor = doctor
    

    def diagnostico(self, paciente_sintomas):
        to_habitacion = {}
        print("Los doctores proceden a diagnosticar a los pacientes")
        print("===============================================")
        for paciente in paciente_sintomas:
            numero_random = randint(0,10)
            numero_random_habitacion = randint(1,300)
            if numero_random > 7:
                print(f"Al paciente {paciente.nombre} se le deriva a la habitacion: {numero_random_habitacion}")
                to_habitacion[numero_random_habitacion] = paciente.nombre 
            else:
                print(f"Al paciente {paciente.nombre} se le mando a casa")    
        print("===============================================")
        return to_habitacion 
        


consulta = Consulta(CDoctor.dicionario_doctores)


