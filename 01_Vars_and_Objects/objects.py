
car = {
    "brand": "Ford",
    "model": "Mustag GT",
    "year": 1964
}

print(car)

#Cambiando el Valor de year del objeto car.
car["year"] = 2019
print(car)

#Añadiendo Valores al objeto.
car["color"] = "purple"
print(car)

#Quitando Valores
car.pop('model')
print(car)

#Limpiando el Diccionario
car.clear()
print(car)