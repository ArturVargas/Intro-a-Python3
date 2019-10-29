

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