from random import *


def tipo_cafe_aleatorio():
    lista_cafes = ["Mocca", "Café irlandés", "Latte", "Expresso", "Solo"]
    cafe = choice(lista_cafes)
    return cafe



class Taza_Cafe():

    def __init__(self, tipo_cafe, temperatura):
        self.tipo_cafe = tipo_cafe
        self.temperatura = temperatura



