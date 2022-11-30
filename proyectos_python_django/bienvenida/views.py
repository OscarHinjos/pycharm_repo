from django.shortcuts import render


# Create your views here.
def bienvenido(request):

    return render(request, 'bienvenida.html')


def listar_datos(request):
    listado_alumnos = [
        {'Nombre': 'Nombre1', 'Apellidos': 'Apellidos1', 'DNI': '111A'},
        {'Nombre': 'Nombre2', 'Apellidos': 'Apellidos2', 'DNI': '222B'},
        {'Nombre': 'Nombre2', 'Apellidos': 'Apellidos3', 'DNI': '333C'},
    ]
    contexto = {'listado_alumnos': listado_alumnos}
    return render(request,"gestion/alumnos.html",contexto)