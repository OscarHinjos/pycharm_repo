"""proyectos_python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bienvenida.views import bienvenido, listar_datos
from deportes.views import deportes, mundial,addTeam

urlpatterns = [
    path('', bienvenido, name='inicio'),
    path('admin/', admin.site.urls),
    path('deportes/', deportes, name='deportes'),
    path('deportes/infoMundial', mundial, name='infoMundial'),
    path('deportes/infoMundial/AñadirSeleccion', addTeam, name='addTeam'),
    path('alumnos/listar_alumnos',listar_datos, name='listado_alumnos')
]
