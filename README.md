# ClaseDjango

## 1. ¿Qué es Django? (5 min)
Django es un framework web de alto nivel basado en Python. Proporciona herramientas y estructuras para desarrollar aplicaciones web de manera rápida y eficiente. Algunas características clave incluyen su ORM (Object-Relational Mapping), manejo de URLs, autenticación, y un sistema de plantillas.

## 2. Instalar Django (5 min)
Antes de instalar Django, asegúrate de tener Python y pip instalados. Luego, sigue estos pasos:
- Instala virtualenv: `pip install virtualenv`
- Crea un entorno virtual: `python -m venv env_no_global`
- Activa el entorno virtual: `.\env_no_global\Scripts\activate`
- Instala Django: `pip install django`
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
Breve explicación de cada operación. Agrega la aplicación en `INSTALLED_APPS`.
```
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
]
```
Crear un modelo en app/models.py:
```
from django.db import models

class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

```

## 10. Superusuario y Administrador de Páginas (5 min)
Crea un superusuario con:
```
python manage.py createsuperuser
```
Utiliza el panel de administración para gestionar tus páginas.

