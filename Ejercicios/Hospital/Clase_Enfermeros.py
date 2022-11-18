import Clase_Persona


class Enfermeros(Clase_Persona.Persona):

    def __init__(self, nombre, apellido, dni,planta_trabajo):
        super().__init__(nombre, apellido, dni)
        self.planta_trabajo = planta_trabajo


    def atender(self, pacientes):
        pacientes_consulta = {}
        for paciente in pacientes:
            print(f"{self.nombre} atiende al paciente {paciente.nombre} y lo lleva a consulta")
            pacientes_consulta[paciente.nombre] = paciente.sintomas
        return pacientes_consulta    

        

enfermero1 = Enfermeros("Julian","Perez","3333C",5,)
enfermero2 = Enfermeros("Luna","Navarro","4444C",2,)      

dicionario_enfermeros = [enfermero1,enfermero2]
