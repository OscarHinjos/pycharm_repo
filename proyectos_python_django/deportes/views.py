from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def deportes(request):
    contenido = {'titulo_pagina': 'Actualidad', 'descripcion': 'text'}
    return render(request, 'deportes.html', contenido)


def mundial(request):
    dic_equipos = [
        {'Seleccion': 'España', 'Continente': 'Europa', 'Mun_Ganados': 1},
        {'Seleccion': 'Brasil ', 'Continente': 'America', 'Mun_Ganados': 5},
        {'Seleccion': 'Alemania  ', 'Continente': 'Europa', 'Mun_Ganados': 4},

    ]
    equipos = {'listado_equipos': dic_equipos}
    return render(request,'InfoMundial/infoMundial.html', equipos)