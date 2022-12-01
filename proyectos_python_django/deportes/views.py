from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def deportes(request):
    contenido = {'titulo_pagina': 'Actualidad', 'descripcion': 'text'}
    return render(request, 'deportes.html', contenido)


def mundial(request):
    dic_equipos = [{'Seleccion': 'España', 'Continente': 'Europa', 'Mun_Ganados': 1},
                   {'Seleccion': 'Brasil ', 'Continente': 'America', 'Mun_Ganados': 5},
                   {'Seleccion': 'Alemania  ', 'Continente': 'Europa', 'Mun_Ganados': 4},

                   ]

    if request.method == 'POST':

        accion = request.POST.get('accion', '')
        print(accion)
        if accion == 'guardar':
            n_selecion = request.POST['seleccion']
            n_continente = request.POST['continente']
            n_mundiales = request.POST['num_mundiales']
            n_equipo = {'Seleccion': n_selecion, 'Continente': n_continente, 'Mun_Ganados': n_mundiales}

            dic_equipos.append(n_equipo)
        elif accion == 'filtrar':
            g_dato = request.POST['filtro']
            dic_equipos = list(filter(lambda equipo: equipo['Continente'] == g_dato,dic_equipos))


    elif request.method == "GET":
        pass

    equipos = {'listado_equipos': dic_equipos, }

    return render(request, 'InfoMundial/infoMundial.html', equipos)


def addTeam(request):
    return render(request, 'InfoMundial/AñadirSeleccion/addTeam.html')
