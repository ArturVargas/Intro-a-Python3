import requests

urlBase = 'https://jsonplaceholder.typicode.com'

#GET
usersUrl = urlBase + '/users'
data = requests.get(usersUrl)
print(f"Arreglo de Usuarios {data.json()}")
print(f"Status: {data.status_code}")
print(f"Como Texto {data.text}")

#POST
postUrl = urlBase + '/posts'
body = {
    'title': 'newUser',
    'body': 'Nuevo Usuario desde Post',
    'userId': 1
}

send = requests.post(postUrl, data=body)
print(send.text)
print(f"Status: {send.status_code}")
# Si la respuesta es un Id: 101 esta correcto

#DELETE
# deleteUrl = urlBase + 'posts/1'
# deleted = requests.delete(deleteUrl)
# print(deleted.text)
# print(f"Status: {deleted.status_code}")

#PUT
# putUrl = urlBase + 'posts/1'
# bod = {
#     'id':1,
#     'title':'Actualizado',
#     'body':'Usuario Actualizado',
#     'userId':1
# }
# headers = {
#   "Content-type":"application/json"  
# }

#update = requests.put(putUrl, data=bod, headers=headers)
#print(f"Status: {update.status_code}")
#print(update.text)

