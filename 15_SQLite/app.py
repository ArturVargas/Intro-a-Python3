
import sqlite3

#De esta forma le decimos a sqlite que cree una nueva bd
#en este caso con el nombre "miBD"
db = sqlite3.connect("miBD.db")

# Creamos nuestra primera tabla en sqlite:
def CrateTable():
  #Con esta instruccion le decimos que la data que leeremos esta
  #en fomato de columnas, asi podemos leerla
  db.row_factory=sqlite3.Row

  # Aqui creamos nuestra tabla User con las propiedadades de ID, name, email y password
  # Con el atributo unique le diremos que no puede haber emails repetidos
  db.execute("create table if not exists User(ID integer primary key autoincrement, Name text, email text unique, password text)")

  # Con db.commit se confirma la transaccion echa, osea que todos los cambios en la bd son guardados 
  db.commit()

#Agregaremos Datos a la tabla
def AddData(Name, email, password):
  db.row_factory=sqlite3.Row
 #Insertaremos informacion en la bd.
 #Enviaremos la data como parametros.
  db.execute("insert into User(Name,email,password) values(?,?,?)",
              (Name,email,password))
  db.commit()
  print("Usuario Creado Exitosamente!!")

#Para enlistar los datos de nuestra db
def UserList():
  cursor = db.execute("select * from User")
  for row in cursor:
    print("ID: {}, Name: {}, Email: {}, Password: {}".format(row["ID"], row["Name"],row["email"],row["password"]))

def DeleteRow(ID):
  db.row_factory= sqlite3.Row
  db.execute("delete from User where ID={}".format(ID))
  db.commit()
  print(f"El usuario {ID} fue borrado exitosamente!!")

def UpdateEmail(ID, email):
  db.row_factory= sqlite3.Row
  db.execute("update User set email=? where ID=?",(email,ID))
  db.commit()
  print(f"Email de {ID} fue actualizado!!")

# Creamos la funcion main que nos permitira llamar las otras funciones.
def main():
  CrateTable()
  while 1:
    operation = int(input("Que operación deseas hacer: \n 1.Crear Usuario " +
                  "\n 2.Listar Usuarios \n 3.Borrar Usuario " + 
                  "\n 4.Actualizar email \n 0.Salir \n"))
    if operation == 0:
      break
    elif operation == 1:    
      name = input("Da el nombre: ")
      email = input("Da un correo valido: ")
      password = input("Contraseña: ")
      AddData(name, email, password)
    elif operation == 2:
      UserList()
    elif operation == 3:
      idx = int(input("ID del usuario que desea borrar: "))
      DeleteRow(idx)
    elif operation == 4:  
      idx = int(input("ID Usuario: "))
      email = input("Nuevo email: ")
      UpdateEmail(idx, email)
 


if __name__ == '__main__':main()