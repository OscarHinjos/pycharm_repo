#Importaciones
import Clase_Doctor as CDoctor
import Clase_Enfermeros as CEnfermero
import Clase_Pacientes as CPaciente
import Clase_Enfermos as CEnfermos
import Clase_consulta as CConsulta
from random import *

#Clase Hospital
class Hospital():
    #Datos Clase Hospital
    def __init__(self, nombre, doctores,enfermeros,pacientes):
        self.nombre = nombre
        self.doctores = doctores
        self.enfermeros = enfermeros
        self.pacientes = pacientes
        self.enfermos = enfermeros
    #Funcion entrada fichar doctores y enfermeros
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
    #Funcion salida fichar doctores y enfermeros
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
    
    #Funcion devuelve un enfermero aleatorio
    def elegir_enfermero(self):
        enfermero = choice(self.enfermeros)
        return enfermero
    #funcion devuelve un array de pacientes
    def devolver_pacientes(self):
        return self.pacientes

    #funcion evalua si la cantidad de pacientes es <3 si lo es añade a una lista el nombre del paciente a la habitacion si no muestra un 
    #mensaje para derivar al paciente a otro hospital
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




#Objeto hospital
hospital = Hospital("HOSPITAL 1",CDoctor.dicionario_doctores ,CEnfermero.dicionario_enfermeros,CPaciente.lista_pacientes)

#Funcion hospital fichar entrada
hospital.fichar_entrada()

#Escoge un enfermero
enfermero_escogido = hospital.elegir_enfermero()
print(f"El enfermero : {enfermero_escogido.nombre}")
print("===============================================")
#Bucle en el que el enfermero atiende a los pacientes
for enfermero in CEnfermero.dicionario_enfermeros:
    if enfermero == enfermero_escogido:
        enfermero_escogido.atender(hospital.devolver_pacientes())
print("===============================================")
#Muestra En que habitacion deriva a los pacientes
print(hospital.habitaciones(CConsulta.consulta.diagnostico(hospital.devolver_pacientes())))

print("===============================================")
#Funcion hospital fichar salida
hospital.fichar_salida()
