

# REST API en Python DJANGO
Django es un framework de desarrollo web que permite desarrollar aplicaciones con una estructura bastante limpia y de forma rapida

## Pasos Para crear un Proyecto con Django
* Creamos la carpeta que contendra nuestro proyecto
  -- En mi caso la llame "REST_PY"
* Dentro de la carpeta "REST_PY" Creare un ambiente virtual    desde la terminal.
  -- `python3 -m venv restEnv` "restEnv" es el nombre de mi ambiente virtual.
* Activamos nuestro ambiente virtual.
  -- `source restEnv/bin/activate` 
* Usaremos pip para instalar Django **pip se instala por defecto con python**
  -- `pip install django` esto puede tardar unos minutos.
* Cuando se termine de instalar django crearemos un proyecto.
  -- `django-admin startproject _Nombre_de_tu_Proyecto` es este caso el nombre de mi proyecto es "API".

La estructura que tendremos es la siguiente:
* REST_PY
  *  |_____API
  *  |       |_____API
  *  |       |_____mage.py
  *  |  
  *  |_____restEnv

* Ahora para levantar nustro proyecto nos colocamos a nivel de la carpeta API REST_PY/API y ejecutamos `./manage.py runserver`
  -- esto nos permite correr nuestro servidor local de django
  **Por defecto corre en localhost:8000**

* Ahora editaremos settings.py.
  -- En ALLOWED_HOSTS agregamos un asterisco para que nos permita hacer peticiones desde cualquie parte:
    ALLOWED_HOSTS = ['*']
  -- En LANGUAJE_CODE podemos cambaiar el idioma de la pagina a español:
    LANGUAGE_CODE = 'es'
  __ Podemos cambiar la zona horaria tambien:
    TIME_ZONE = 'America/Mexico_City'
 
* Como siguiente paso crearemos una app con django que se refiere a un modulo o submodulo de nuestro proyecto.
[Ver más...](https://stackoverflow.com/questions/19350785/what-s-the-difference-between-a-project-and-an-app-in-django-world) `./manage.py startapp nombre_de_tu_app` en este caso usaré books como nombre de mi app.
**Haré un ejemplo de una libreria**

`` Ahora tenemos dentro de REST_PY/API las carpetas API y books ``
* Dentro de la Carpeta "books" tenemos más archivos de python que usaremos más adelante, por el momento nos interesa el archivo `models.py` que nos ayudara a crear una tabla para nuestra base de datos.

* Crearemos un modelo de lo que sera nuestra tabla, para crear los modelos en python usamos clases.

* Despues de tener nuestro modelo, agregamos nuestra app a settings.py que se encuentra en: REST_PY/API/API/settings.py en el arreglo de INSTALLED_APPS

* Una vez agregada nuestra app en mi caso es "books" hacemos las migraciones desde la terminal con: `./manage.py makemigrations`
  * -- nos regresa un mensaje de Create model Libro donde Libro es el nombre de nuestra clase de models.
  * Los errores más comunes en este punto son por el tipo de datos, asegurate de tenerlos bien escritos.

* Para que el cambio se vea reflejado en la bd tenemos que ejecutar el comando `./manage.py migrate` esto hace que el modelo que acabamos de hacer se convierta en una tabla. 

* Dentro de la carpeta de nuestra app "books" encontraremos un archivo admin.py el cual nos permite registrar nuestros modelos
y manejarlos desde el administrador por defecto de django

* Regresamos a nuestra terminal y ejecutamos `./manage.py createsuperuser` 
    * Nos pedira un nombre de usuario, un correo que podemos omitir, un password y confirmar el password
    * Para ver como funciona el admin de django volvemos a levantar nuestro server local `./mange.py runserver`
    * Visitamos la direccion **localhost:8000/admin** donde nos pedira los datos del super usuario que acabamos de crear.

* En el panel de administracion se muestra nuestro modelo Libros
al hacer click en el nos muestra un boton donde podemos empezar a cargar datos a nuestra BD      

* Instalaremos 2 librerias más que nos permitiran hacer una API
    * la primera es [Django Rest Framework](https://www.django-rest-framework.org/) `pip install djangorestframework`
    * la otra es [Django Cors Headers](https://pypi.org/project/django-cors-headers/) `pip install django-cors-headers`

* Una vez instaladas iremos al archivo settings.py y añadiremos estas librerias en el arreglo de Installed Apps.

* Para poder usar python como una API necesitamos serializar nuestros modelos en un formato JSON para que sea compatible con diferentes frameworks de frontend.
  * Creamos un archivo serializers.py dentro de la app books
  en este archivo lo que haremos es decirle que campos queremos serializar en nustro caso seran todos.

* Despues en el archivo views.py crearemos un [ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#viewsets), un VIewSet es una interfaz que tiene Rest Framework y nos permite trabajar con los diferentes metodos, para trabajar con los registros que estamos serializando

* Una vez creado nuestro ViewSet iremos al archivo urls.py que esta en nuestra carpeta API. aqui crearemos la ruta correspondiente

* Por ultimo corremos nuevamente nuestro servidor y visitamos la ruta que acabamos de crear `localhost:8000/books/` si todo sale bien, veremos una pantalla con el registro que insertamos anteriormente desde el admin pero en formato json.

* Podemos probar nuestra API haciendo una peticion desde Postman de tipo POST a la url `localhost:8000/books/`

### Happy Hacking :D!



