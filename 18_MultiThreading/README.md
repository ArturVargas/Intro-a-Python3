
# Threading en Python

Los hilos en python nos permiten tener diferentes partes de nuestra aplicacion ejecutandose simultaneamente.

## Que es un Thread?
Un tread ó hilo es un flujo de ejecución separado. Esto significa que tu programa tendra dos cosas ejecutando al mismo tiempo.Pero para la mayoria de implementaciones en Python3 los diferentes hilos no se ejecutan al mismo tiempo, solo parece.

Tener multiples tareas corriendo simultaneamente requiere una implementación no estándart de Python, escribir parte de su codigo en un lenguaje de programación diferente o usar multiprocesamiento que conlleva una sobrecarga dicional.

* Más Info: [Real Python](https://realpython.com/intro-to-python-threading/)

## Sincrono Vs Asincrono
* Sincrono: Tenemos dos tareas(Task1, Task2), necesitamos esperar a que finalice la tarea Task1 antes de empezar a ejecutar Task2.

* Asincrono: Podemos iniciar la tarea2 sin tener que esperar a que la tarea1 haya finalizado.
