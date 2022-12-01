from django.contrib import admin

from bienvenida.models import Persona

# Register your models here.
# Registrar los modelos que se creen para poder utilizarlos desde el panel de administracion
admin.site.register(Persona)  # clase de models
