from Chef import Chef
#Este Chef puede hacer lo que el chef generico y otros platillos más
class MexicanChef(Chef):
  #De esta forma heredamos los platillos que puede hacer el otro chef

  def make_taquitos(self):
    print("El chef hizo unos tacos de pastor")

  def make_pozole(self):
    print("El chef hizo un pozole")
  
  # Si queremos que nuestro chef tambien tenga un platillo especial
  # lo sobreescribimos
  def make_special_dish(self):
    print("El chef hizo Tostadas de Pata") 