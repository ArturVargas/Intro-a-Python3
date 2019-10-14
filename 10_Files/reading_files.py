
# Abrimos el archivo.
# El argumento r es de read.
data_file = open("./randomFiles/data.txt", "r")

# Nos regresa un Boolean si el archivo se puede leer
# print("Se puede Leer? ")
# print(data_file.readable())

# Nos permite leer el Archivo completo
# print("Contenido del Archivo: ")
#print(data_file.read())

# Nos permite leer por linea el archivo
print("Primeras dos lineas del archivo: ")
# Toma en cuenta los saltos de linea.
print(data_file.readline())
print(data_file.readline())

# Crea un arreglo con el contenido del archivo
#print(data_file.readlines())

for employee in data_file.readlines():
  print(employee)

# ** Al parecer uno no funciona con el otro esto es:
# si ejecuto primero data_file.readline() y despues el for de employee
# regresa solo un resultado **

# ** Debemos asegurarnos de siempre cerrar el archivo. **
data_file.close()