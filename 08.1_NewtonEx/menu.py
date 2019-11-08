import math

text = ''' Welcome to Newton's cradle!
(1)What's the domain name of my email addres?
(2)Calculate permiter and area for a circle
(3)Clean given text 
(4)Encrypt given text
'''
print(text)

def optionOne(email):
  character = email.find('@')
  if character > 0:
    res = (email[character:email.find('.com')])
  else:
    res = ("Please type a valid email address")
  return res

def optionTwo():
  PI = math.pi
  try:
    rad = float(input("Please insert radius: "))
    if rad > 0:
      perimeter = (2 * PI * rad)
      area = PI * (math.pow(rad, 2))
      res = (f"Perimetro: {perimeter}, Area: {area}")
    else:
      res = "Please insert a positive number"
  except ValueError:
    res = "Please insert a number"
  return res


try:
  option = int(input("Please select an option: "))
except ValueError:
  print("Please insert a number")

if option == 1:
  email = input("Please insert email addres: ")
  print(optionOne(email))
elif option == 2:
  print(optionTwo())
elif option == 3:
  text = input("Please insert a dirty string: ")
  print(" ".join(text.split()))
elif option == 4:
  toEncrypt = input("Please insert the string to encrypt: ")
  print("#".join(toEncrypt.split())[::-1])
else:
  print("Please insert a number from 1 to 4")
  

