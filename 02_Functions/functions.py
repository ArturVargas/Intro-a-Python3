
# variables Globales
age = 26

#Se define una funcion
def my_function():
    print(f'Mi funcion {age}')
 
# Se llama a la funcion
my_function()

def second_func(firs, sec):
    print(f'Parametros {age}, {sec}')
    return firs + sec

# second_func(1, 6)
print(second_func(1, 6))


#Las Funciones Lambda
# Son pequeñas funciones anonimas que pueden tener cualquier numero de argumentos
# pero tener una sola expresion
# Sintaxis: lambda arguments: expresion

x = lambda a,b,c,d: a+b*c-d
print(x(2,5,7,1))

def display(name):
    print(f"Hola {name} welcome to Phyton3")

def main(param, fun):
    fun(param)

main('Artur', display)