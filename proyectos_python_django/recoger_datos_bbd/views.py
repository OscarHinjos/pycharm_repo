from django.forms import modelform_factory
from django.shortcuts import render
from recoger_datos_bbd.models import PersonaRecogida

ClienteForm = modelform_factory(PersonaRecogida, exclude=[])#guarda automaticamente los datos del formulario


# Create your views here.
def recoger_datos(request):
    mensaje = ''
    if request.method == "POST":
        try:
            """
            nombre = request.POST['nombre']
            apellido = request.POST['apellidos']
            edad = request.POST['edad']
            print(f"{nombre} | {apellido} | {edad}")
            mensaje = 'Cliente almacenado correctamente'
            persona = PersonaRecogida(nombre=nombre, apellidos=apellido, edad=edad)
           """
            persona_form = ClienteForm(request.POST)
            persona_form.save()  # Guardar en la bbd
            mensaje = f"Cliente almacenado correctamente"
        except Exception as e:
            mensaje = f"Error al almacenar el cliente {e}"


    persona_form = ClienteForm()

    contexto = {'mensaje': mensaje, 'persona_form': persona_form}
    return render(request, 'formulario.html', contexto)

