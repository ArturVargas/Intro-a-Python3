
# Abrimos el archivo.
# El argumento w es de write y a de append.

# data_file = open("./randomFiles/data.txt", "a")

# # Escribiendo en el archivo
# data_file.write("\nHumano - Testing")

# # ** Debemos asegurarnos de siempre cerrar el archivo. **
# data_file.close()


# Tomar en cuenta que w sobreescribe un archivo
# Podemos generar un nuevo archivo cambiando el nombre
data_file = open("./randomFiles/index.html", "w")

# Escribiendo en el archivo
data_file.write("<h1>Hola mundo </h1>")

# ** Debemos asegurarnos de siempre cerrar el archivo. **
data_file.close()