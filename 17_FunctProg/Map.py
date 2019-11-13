
#Info: https://www.w3schools.com/python/ref_func_map.asp

X = [1, 2, 3, 4, 5]
def square(num):
  return num * num

print(list(map(square, X)))