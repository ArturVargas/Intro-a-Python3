
#Info: https://www.w3schools.com/python/ref_func_map.asp

#Ej 1

X = [1, 2, 3, 4, 5]
def square(num):
  return num * num

print(list(map(square, X)))

#Ej 2

listItems = [1,2,3,4,5,6,7]
print(listItems)
tempList = list(map(lambda x: x*2, listItems))
print(tempList)

