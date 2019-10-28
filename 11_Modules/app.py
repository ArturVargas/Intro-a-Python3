
import modules_tools
## Podemos crear un alias para nuestro modulo.
## Ej: import modules_tools as tools y usarlo como tools
# print(f"{tools.farenheit_to_celcius(68)} ºC")

print(f"{modules_tools.farenheit_to_celcius(68)} ºC")

result = modules_tools.Hex_to_Bin("a23")
print(result)

# Para encontrar los diferentes modulos que tiene Python 3
# https://docs.python.org/3/py-modindex.html
# Para instalar modulos
# https://docs.python.org/3/installing/index.html