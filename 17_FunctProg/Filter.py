
#Filtra un arreglo de elementos con base en si la condición es
# True ó False.
#Filter recibe una funcion como parametro y el arreglo de elementos
# info: https://www.w3schools.com/python/ref_func_filter.asp

#Ej 1:

def filtrado(variable):
  letters = ['a', 'b', 'e', 'i', 'd', 'o', 'u', 'f']
  if variable in letters: 
    return True
  else:
    return False

sequence = ['d', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', 's']

filtered = filter(filtrado, sequence)
for letter in filtered:
  print(letter)


#Ej 2:
listItems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tempList = list(filter(lambda x:x % 2 == 0, listItems))
print(tempList)
    