
# Cuando un error ó excepción ocurren, normalmete Python 
# se detiene y genera un mensaje de error.
# Estas excepciones se pueden manejar usando la instruccion "try":

try:
  print(x)
except:
  print("X no esta definida")

print("Continua con la ejecucion del programa.")

#print(x)

## Manejando varias execpciones.
try:
  print(x)
except NameError:
  print("La Variable x no esta definida")
except:
  print("Algo más salio mal")

try:
  number = int(input("Da un número: "))
  print(number)
except ValueError:
  print("El valor dado no es número")
finally:
  print("Termino el bloque de try/except")

# finally se ejecuta independientemente de si el bloque
# try/except genera un error o no.

