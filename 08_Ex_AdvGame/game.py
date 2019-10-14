import random

secretWords = {
  "It is something that you can do with your dog": "game",
  "It is something that you have in your office": "computer",
  "It is the best friend to man": "dog",
  "It is something round with cheesse and meat": "pizza"
}
wordKey = random.choice(list(secretWords))
print("Pista: " + wordKey)
secretWord = secretWords.get(wordKey)
guess = ""
guessCount = 0
limit = 3
limit_guesses = False

while guess != secretWord and not(limit_guesses):
  if guessCount < limit:
    guess = input("Intenta Adivinar tienes " + str(limit-guessCount)+ " intentos: ")
    guessCount += 1
  else:
    limit_guesses = True

if limit_guesses:
  print("Perdiste Chavo!!")
else:
  print("Ganaste Champ!!") 