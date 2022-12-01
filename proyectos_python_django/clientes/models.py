from django.db import models

"""
      1.Una vez se tengan los datos siguientes comandos:
      python .\manage.py makemigrations

      2.asegurarse de que es lo que quieres :
      python .\manage.py sqlmigrate cliente 0001

      3.ejecutar cambios
      python .\manage.py migrate
"""


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} | {self.nombre} |" \
               f"{self.apellidos} | {self.dni} | " \
               f"{self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=40)
    marca = models.CharField(max_length=60)
    color = models.CharField(max_length=9)
    combustible = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.matricula} |" \
               f"{self.marca} | {self.color} | " \
               f"{self.combustible} | {self.cliente}"
