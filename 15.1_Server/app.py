
"""
En esta practica crearemos un servidor web
"""
import http.server
import socketserver

PORT = 8000

#Se crea un controlador que maneje las peticiones del server.
controller = http.server.SimpleHTTPRequestHandler

#Se abre el puerto, en este caso el 8000 que es el que estara
#recibiendo las peticiones.

with socketserver.TCPServer(("", PORT), controller) as http:
  print("Server Corriendo en http://localhost:{}".format(PORT))
  http.serve_forever()

#Por default python renderiza el archivo index.html