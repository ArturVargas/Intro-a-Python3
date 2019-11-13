
## Programación Funcional

```
Es un paradigma de Programación que nos permite construir software de solamente funciones.
La programacion funcional es declarativa, tiende a ser más predecible, concisa y facil de leer.
Se compone de funciones puras(No usas librerias, funciones o procedimientos externos).
```

### Programación Declarativa e Imperativa
 
 * Declarativa: Declaras una base de conocimiento, restricciones ó afirmaciones para resolver el problema pero no dices como llegar a la solución,

 * Imperativa: Declaras un algortimo y una serie de instrucciones o pasos para llegar a una solución.

```console
Tipicamente en la programación funcional no se usan ciclos, se opta por usar recursion. 
La recursion es un concepto matematico que significa "feeding into itself". Con una funcion recursiva la funcion se llama a si misma como una subfuncion.
```

* Ej:
  ```console
  def factorial(n):
    #Caso Base: 1! = 1 && 0! = 1
    if n <=1 :
      return 1
    #Caso Recursivo: n! = n * (n-1)!
    else:
      return n * factorial(n-1)
  ```