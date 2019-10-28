# En python podemos crear clases para representar datos de
# de forma mas especifica.

class Student:
# todas las clases tienen una fincion __init__(), la cual se 
#ejecuta siempre que la clase es inicializada.
  def __init__(self, name, major, gpa, is_aproved):
    #El parametro self es una referencia a la instacia actual
    # de la clase y es usado para acceder a las variables que pertenecen
    # a la clase # No es necesario llamarlo self, pero debe ser el primer parametro.
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_aproved = is_aproved

class Person:
  def __init__(obj, name, age):
    obj.name = name
    obj.age = age

## Object Functions

class Students:
  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa

  def is_aproved(self):
    if self.gpa >= 4:
      return True
    else:
      return False
    