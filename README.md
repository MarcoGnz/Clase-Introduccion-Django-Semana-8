# Clase Introducción Django

## 1. ¿Qué es Django? (5 min)
Django es un framework web de alto nivel basado en Python. Proporciona herramientas y estructuras para desarrollar aplicaciones web de manera rápida y eficiente. Algunas características clave incluyen su ORM (Object-Relational Mapping), manejo de URLs, autenticación, y un sistema de plantillas.

Un framework es un conjunto de herramientas, guías y estructuras predefinidas que se utilizan para desarrollar y organizar software de manera eficiente. Funciona como una especie de "esqueleto" o plataforma base, sobre la cual los programadores y desarrolladores pueden construir y personalizar sus aplicaciones.

ORM (Object-Relational Mapping) es una técnica de programación que permite convertir los datos de un lenguaje de programación orientado a objetos al formato utilizado en una base de datos relacional. Esta técnica facilita la interacción entre ambos sistemas y permite a los desarrolladores trabajar con objetos y clases en lugar de escribir consultas SQL.

## 2. Instalar Django (5 min)
Antes de instalar Django, asegúrate de tener Python y pip instalados. Luego, sigue estos pasos:
- Instala virtualenv: `pip install virtualenv`
- Crea un entorno virtual: `python -m venv env_no_global`
- Activa el entorno virtual: `.\env_no_global\Scripts\activate`
- Instala Django: `pip install Django==4.0`
- Instala psycopg2 (para la conexión a PostgreSQL): `pip install psycopg2`

## 3. Iniciar un Proyecto (5 min)
Crea un nuevo proyecto con el siguiente comando:
```
django-admin startproject nombre_del_proyecto
```
Explora la estructura de directorios generada.

## 4. Iniciar el Servidor (5 min)
Para iniciar el servidor de desarrollo, ejecuta:
```
python manage.py runserver
```
Accede a la página de bienvenida de Django en tu navegador.

## 5. Crear una Aplicación y Configurar URLs (10 min)
Crea una nueva aplicación con:
```
python manage.py startapp nombre_de_la_aplicacion
```
Configura las URLs en `urls.py` del proyecto y la aplicación.

En `urls.py` del proyecto:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('nombre_de_la_aplicacion.urls')),
]
```

En `urls.py` de la aplicación:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
]
```

## 6. Mostrar "Hola Mundo" con HttpResponse (5 min)
Crea una vista básica en `views.py`:
```python
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola Mundo")
```
Enlaza la vista en `urls.py`.

## 7. ¿Qué es MTV (Model-Template-View)? (5 min)
MTV es el patrón de diseño utilizado por Django:
- **Modelo (Model)**: Maneja operaciones de base de datos y cálculos de datos.
- **Plantilla (Template)**: Genera la salida HTML que ve el usuario.
- **Vista (View)**: Actúa como intermediario entre el Modelo y la Plantilla.
  
<img width="1204" alt="mtv" src="https://github.com/user-attachments/assets/852e38f3-1757-4773-b7ac-96348df50f7b">


## 8. Conexión a una Base de Datos PostgreSQL (10 min)
Configura la base de datos en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
**comandos postgres**:
crear rol:
```
CREATE USER sample_user WITH PASSWORD 'password';
```
otorgar permiso:
```
ALTER ROLE sample_uer CREATEDB;
```
para ver roles y permisos:
```
\du;
```
Crear base de datos con sample user:
```
CREATE DATABASE sample_database;
```
Aplica migraciones para crear la estructura de la base de datos:
```
python manage.py makemigrations
python manage.py migrate
```

## 9. CRUD (Create, Read, Update, Delete) (10 min)
Breve explicación de cada operación.

Agrega la aplicación en `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
]
```

Crear un modelo en `app/models.py`:
```python
from django.db import models

class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
```

Registrar el modelo en `app/admin.py`:
```python
from django.contrib import admin
from .models import Ejemplo

admin.site.register(Ejemplo)
```

Crear vistas para CRUD:
En `app/views.py`:
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Ejemplo
from .forms import EjemploForm

def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def crear_ejemplo(request):
    if request.method == 'POST':
        form = EjemploForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ejemplos')
    else:
        form = EjemploForm()
    return render(request, 'basic_CRUD/crear_ejemplo.html', {'form': form})

def lista_ejemplos(request):
    ejemplos = Ejemplo.objects.all()
    return render(request, 'basic_CRUD/lista_ejemplos.html', {'ejemplos': ejemplos})

def editar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)
    if request.method == 'POST':
        form = EjemploForm(request.POST, instance=ejemplo)
        if form.is_valid():
            form.save()
            return redirect('lista_ejemplos')
    else:
        form = EjemploForm(instance=ejemplo)
    return render(request, 'basic_CRUD/editar_ejemplo.html', {'form': form, 'ejemplo': ejemplo})

def eliminar_ejemplo(request, id):
    ejemplo = get_object_or_404(Ejemplo, id=id)
    if request.method == 'POST':
        ejemplo.delete()
        return redirect('lista_ejemplos')
    return render(request, 'basic_CRUD/eliminar_ejemplo.html', {'ejemplo': ejemplo})

```

Crear un formulario en `app/forms.py`:
```python
from django import forms
from .models import Ejemplo

class EjemploForm(forms.ModelForm):
    class Meta:
        model = Ejemplo
        fields = ['nombre', 'descripcion']
```

Configurar URL para la vista de creación en `app/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ejemplos, name='lista_ejemplos'),
    path('crear/', views.crear_ejemplo, name='crear_ejemplo'),
    path('editar/<int:id>/', views.editar_ejemplo, name='editar_ejemplo'),
    path('eliminar/<int:id>/', views.eliminar_ejemplo, name='eliminar_ejemplo'),
]
```

Crear plantilla para la vista de creación en `app/templates/app/crear_ejemplo.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Crear Ejemplo</title>
</head>
<body>
    <h1>Crear Nuevo Ejemplo</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
```
`lista_ejemplos.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Ejemplos</title>
</head>
<body>
    <h1>Lista de Ejemplos</h1>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            {% for ejemplo in ejemplos %}
            <tr>
                <td>{{ ejemplo.nombre }}</td>
                <td>{{ ejemplo.descripcion }}</td>
                <td>
                    <a href="{% url 'editar_ejemplo' ejemplo.id %}">Editar</a>
                    <a href="{% url 'eliminar_ejemplo' ejemplo.id %}">Eliminar</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="{% url 'crear_ejemplo' %}">Crear Nuevo Ejemplo</a>
</body>
</html>
```
`editar_ejemplo.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Editar Ejemplo</title>
</head>
<body>
    <h1>Editar Ejemplo: {{ ejemplo.nombre }}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
    <a href="{% url 'lista_ejemplos' %}">Cancelar</a>
</body>
</html>

```
`eliminar_ejemplo.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Eliminar Ejemplo</title>
</head>
<body>
    <h1>¿Estás seguro de que quieres eliminar "{{ ejemplo.nombre }}"?</h1>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Eliminar</button>
    </form>
    <a href="{% url 'lista_ejemplos' %}">Cancelar</a>
</body>
</html>
```


## 10. Superusuario y Administrador de Páginas (5 min)
Crea un superusuario con:
```
python manage.py createsuperuser
```
Utiliza el panel de administración para gestionar tus páginas.

