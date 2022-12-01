from django.db import models


# Create your models here.
# BBD
# Clase que herede de model

class Persona(models.Model):
    # Definir atributos y de que tipo son
        # CharField --> Texto
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)
    """
    1.Una vez se tengan los datos siguientes comandos:
    python .\manage.py makemigrations
    
    2.asegurarse de que es lo que quieres :
    python .\manage.py sqlmigrate bienvenida 0001
    
    3.ejecutar cambios
    python .\manage.py migrate
    """

    def __str__(self):
        return f"{self.id}   {self.nombre}  " \
               f"{self.apellidos}   {self.dni}  " \
               f"{self.email}"




