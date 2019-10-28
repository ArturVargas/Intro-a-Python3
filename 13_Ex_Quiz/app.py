# Ejercicio de Clases:
#Crear un Quiz en el cual las respuestas coincidan con las enviadas
# como parametro en questions[] y que regrese el valor de cuantas
#respuestas fueron correctas
from Question import Question

questions_list = [
  "Que lenguaje de programación es tu favorito?\n(a)JavaScript \n(b)Python \n(c)Go \n(d)Otro\n",
  "Que nivel de conocimientos tienes en ese lenguaje de programación? \n(a)Basico \n(b)Intermedio \n(c)Avanzado\n",
  "Que fuentes de información usas para aprender?\n(a)Documentación \n(b)Youtube \n(c)Udemy \n(d)Otro\n"
]

questions = [
  Question(questions_list[0], "a"),
  Question(questions_list[1], "b"),
  Question(questions_list[2], "b")
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.res:
      score += 1
  print(f"Tienes {score} correctas de {len(questions)}")

run_test(questions)