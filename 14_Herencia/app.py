
from Chef import Chef
from MexicanChef import MexicanChef

myChef = Chef()
myChef.make_chicken()

myMexicanChef = MexicanChef()
# Ahora el chef puede hacer pollo
myMexicanChef.make_chicken()
# y tambien uno de sus platillos
myMexicanChef.make_taquitos()

myChef.make_special_dish()
myMexicanChef.make_special_dish()