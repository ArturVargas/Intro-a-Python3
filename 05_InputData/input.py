
name = input("Your Name: ")
print(f"Hello {name}")

age = input("Your Age: ")

# try:
#   if int(age) >= 18:
#     print(f"You are an adult")
# except ValueError:
#   print("No es un número")

# num1 = input("Da un número: ")
# num2 = input("Da otro número: ")
# try:
#   op = input("Escoge una operación: /n 1.Suma 2.Multiplicación 3.Potencia")
#   if int(op) == 1:
#     print(int(num1) + int(num2))

#   if int(op) == 2:
#     for x in range(int(num2)):
#      print(int(num1) * (x+1))

#   if int(op) == 3:
#     print(pow(int(num1), int(num2)))

# except ValueError:
#   print("No es un número")


#Calculadora 2
num1 = float(input("Da un número: "))
num2 = float(input("Da otro número: "))

def suma(a, b):
  print(a + b)
 
def mult(a, b):
  for x in range(b):
     print(a * (x+1))

def pot(x, y):
   print(pow(int(x), int(y)))

oper = int(input("Elige una opcion: 1.Suma 2.Multiplicación 3.Potencia "))
if oper == 1:
  suma(num1, num2)
elif oper == 2:
  mult(num1, num2)
elif oper == 3:
  pot(num1, num2)
else:
  print("opcion no valida")

