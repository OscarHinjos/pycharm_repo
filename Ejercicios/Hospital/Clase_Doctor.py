import Clase_Persona

class Doctor(Clase_Persona.Persona):

    def __init__(self, nombre, apellido, dni,especialidad):
        super().__init__(nombre, apellido, dni)
        self.especialidad = especialidad


doctor1 = Doctor("Jose","Lopez","1111A","Cardiología")
doctor2 = Doctor("Natalia","Garcia","2222A","Dermatología")

dicionario_doctores = {"Doctor1": doctor1, "Doctor2": doctor2}