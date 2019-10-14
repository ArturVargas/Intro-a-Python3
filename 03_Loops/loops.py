# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print("Continuo")
#         continue
#         #break
#     print(i)

# Con continue se salta el valor de 3
# imprime 1,2,continuo,4,5,6

#con break se detiene el ciclo cuando se cumple la condicion


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# itera sobre las letras de banana
# for x in "banana":
#   print(x)

# For al igual que while tiene la propiedad break y continue y funcionan de la misma forma


# for x in range(6):
#   print(x)

# La funcion "range(numero)" regresa una secuencia de numeros iniciando por defaul en el 0 e incrementamdo 1 por default
# range(index, numero) regresa una secuencia de numeros que inicia desde el index hasta el numero dado sin incluir ese numero
# ej: range(2,6) 2,3,4,5
# range(index, numero, incremento) si agregamos un tercer parametro este corresponde al incremento.


def rotLeft(ar, d):
  a = []
  for i in range(len(ar)):
    a.append(ar[(i+d)% len(ar)])
    print(a)
  return a

rotLeft([1,3,4,5,6], 3)