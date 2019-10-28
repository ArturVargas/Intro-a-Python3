
# En este archivo pondremos algunas funciones utiles que nos
# serviran más adelante como un modulo de Python.
# Los modulos son librerias de codigo, esto nos ayuda a no tener que
# reescribir las funciones o metodos.

import random

hex_to_bin = {
  '0':'000',
  '1':'0001',
  '2':'0010',
  '3':'0011',
  '4':'0100',
  '5':'0101',
  '6':'0110',
  '7':'0111',
  '8':'1000',
  '9':'1001',
  'A':'1010',
  'B':'1011',
  'C':'1100',
  'D':'1101',
  'E':'1110',
  'F':'1111'
}

def farenheit_to_celcius(gradosFarenheit):
   celcius_result = (gradosFarenheit - 32)/(1.8000)
   return celcius_result

def Hex_to_Bin(hexadecimal):
  result = " "
  for letter in hexadecimal.upper():
    if letter in hex_to_bin:
     print(f"El Valor de {letter} a binario es: {hex_to_bin.get(letter)}")
     result = result + hex_to_bin.get(letter)
    else:
     return (f"No se encontro un valor para {letter}")
  return result



