
# Del archivo Student importa la clase Student
from Student import Student

# Por buenas practicas cada clase deberia estar en su 
# archivo correspondiente, pero para fines practicos lo hice en el mismo
from Student import Person

#Creamos nuestro primer estudiante
# Enviamos los parametros en el mismo orden como los declaramos en la clase
student1 = Student("Arthur", "Phisics", 3.2, False)
student2 = Student("Pam", "Art", 4.5, True)
print(student1.name)


person1 = Person("John", 26)
person1.age = 40
print(person1.name)
print(person1.age)

#######################
## Clase con funcion. ##
from Student import Students as SF

studnt1 = SF("Louis", "Mechanic", 3.5)
studnt2 = SF("Lenna", "Biology", 4.5)

print(studnt1.is_aproved()) #False
print(studnt2.is_aproved()) #True
