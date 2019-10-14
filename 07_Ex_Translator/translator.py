
# Convertir todas las vocales en letra "f"

def traductor(word):
  translation = ""
  for letter in word:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation = translation + "F"
      else:
        translation = translation + "f"
    else:
      translation = translation + letter
  return translation

print(traductor(input("Escribe una frase: ")))
