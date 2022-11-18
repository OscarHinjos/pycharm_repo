import Clase_Doctor as CDoctor
import Clase_Enfermeros as CEnfermero
import Clase_Pacientes as CPaciente
import Clase_Enfermos as CEnfermos
import Clase_consulta as CConsulta

from random import *


class Hospital():

    def __init__(self, nombre, doctores,enfermeros,pacientes):
        self.nombre = nombre
        self.doctores = doctores
        self.enfermeros = enfermeros
        self.pacientes = pacientes
        self.enfermos = enfermeros

    def fichar_entrada(self):
        print("Fichar Doctores: ")
        print("=============================================")
        for clave,nombre_doctor in self.doctores.items():
             print(f"El doctor : {nombre_doctor.nombre} ficha")
        print("=============================================")
        print("Fichar Enfermeros: ")
        print("=============================================")
        for nombre_enfermero in self.enfermeros:
            print(f"El enfermero : {nombre_enfermero.nombre} ficha")     
        print("=============================================")

    def fichar_salida(self):
        print("Fichar Doctores: ")
        print("=============================================")
        for clave,nombre_doctor in self.doctores.items():
             print(f"El doctor : {nombre_doctor.nombre} ficha en la salida")
        print("=============================================")
        print("Fichar Enfermeros: ")
        print("=============================================")
        for nombre_enfermero in self.enfermeros:
            print(f"El enfermero : {nombre_enfermero.nombre} ficha en la salida")     
        print("=============================================")    
    
     
    def elegir_enfermero(self):
        enfermero = choice(self.enfermeros)
        return enfermero

    def devolver_pacientes(self):
        return self.pacientes


    def habitaciones(self, pacientes_habitacion):
        cantidad_pacientes = []
        for numero_habitacion , nombre_paciente in pacientes_habitacion.items():
            if len(cantidad_pacientes) < 3 :
                cantidad_pacientes.append(nombre_paciente)
            else:
                print(f"No quedan habitaciones el paciente: {nombre_paciente} se le derivara a otro hospital")
        if len(cantidad_pacientes) == 0:
            return f"No hay pacientes en nuestras instalacines" 
        else:
            return f"Los pacientes {cantidad_pacientes} estan en nuestras instalaciones"





hospital = Hospital("HOSPITAL 1",CDoctor.dicionario_doctores ,CEnfermero.dicionario_enfermeros,CPaciente.lista_pacientes)


hospital.fichar_entrada()

enfermero_escogido = hospital.elegir_enfermero()
print(f"El enfermero : {enfermero_escogido.nombre}")
print("===============================================")
for enfermero in CEnfermero.dicionario_enfermeros:
    if enfermero == enfermero_escogido:
        enfermero_escogido.atender(hospital.devolver_pacientes())
print("===============================================")

print(hospital.habitaciones(CConsulta.consulta.diagnostico(hospital.devolver_pacientes())))

print("===============================================")

hospital.fichar_salida()
