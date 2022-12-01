from django.db import models


# Create your models here.
class PersonaRecogida(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    edad = models.IntegerField()
