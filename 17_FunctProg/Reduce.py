#En este ejercicio nececitamos importar el paquete functools
# ver más: https://www.geeksforgeeks.org/reduce-in-python/

from functools import reduce

listItems = [1,2,3,4,5,6,7,8,9,10]
print(listItems)

#Sin reduce.
sum = 0
for item in listItems:
  sum= sum+item
print(sum)

#Usaremos reduce para sumar los elementos del arreglo
total = reduce(lambda x,y: x+y, listItems)
print(total)