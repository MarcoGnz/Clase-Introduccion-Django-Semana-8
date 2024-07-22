#código comentado para una mejor comprensión:

# Importaciones necesarias desde Django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Ejemplo  # Importamos el modelo Ejemplo desde el archivo models.py
from .forms import EjemploForm  # Importamos el formulario EjemploForm desde el archivo forms.py

# Función de vista para mostrar "Hola Mundo"
def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")  # Retorna una respuesta HTTP simple con el texto "Hola Mundo"

# Función de vista para crear un nuevo objeto Ejemplo
def crear_ejemplo(request):
    if request.method == 'POST':  # Verifica si el método de la solicitud es POST
        form = EjemploForm(request.POST)  # Crea una instancia del formulario con los datos del POST
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el formulario en la base de datos
            return redirect('lista_ejemplos')  # Redirige a la vista de lista de ejemplos
    else:
        form = EjemploForm()  # Crea una instancia vacía del formulario
    return render(request, 'basic_CRUD/crear_ejemplo.html', {'form': form})  # Renderiza el template con el formulario

# Función de vista para listar todos los objetos Ejemplo
def lista_ejemplos(request):
    ejemplos = Ejemplo.objects.all()  # Obtiene todos los objetos Ejemplo de la base de datos
    return render(request, 'basic_CRUD/lista_ejemplos.html', {'ejemplos': ejemplos})  # Renderiza el template con la lista de ejemplos

# Función de vista para editar un objeto Ejemplo existente
def editar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)  # Obtiene el objeto Ejemplo por ID o devuelve un error 404 si no existe
    if request.method == 'POST':  # Verifica si el método de la solicitud es POST
        form = EjemploForm(request.POST, instance=ejemplo)  # Crea una instancia del formulario con los datos del POST y el objeto existente
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el formulario en la base de datos
            return redirect('lista_ejemplos')  # Redirige a la vista de lista de ejemplos
    else:
        form = EjemploForm(instance=ejemplo)  # Crea una instancia del formulario con el objeto existente
    return render(request, 'basic_CRUD/editar_ejemplo.html', {'form': form, 'ejemplo': ejemplo})  # Renderiza el template con el formulario y el objeto

# Función de vista para eliminar un objeto Ejemplo existente
def eliminar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)  # Obtiene el objeto Ejemplo por ID o devuelve un error 404 si no existe
    if request.method == 'POST':  # Verifica si el método de la solicitud es POST
        ejemplo.delete()  # Elimina el objeto de la base de datos
        return redirect('lista_ejemplos')  # Redirige a la vista de lista de ejemplos
    return render(request, 'basic_CRUD/eliminar_ejemplo.html', {'ejemplo': ejemplo})  # Renderiza el template de confirmación de eliminación con el objeto
