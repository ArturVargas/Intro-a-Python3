
gridList = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

print(gridList[0][0])
print(gridList[1][1])

for row in gridList:
  print(f"Fila: {row}")
  for col in row:
    print(f"Elementos: {col}")