import requests
import json

#ejercicio 1, obtener la informacion de los usuarios
#usamos el metodo GET para obtener la info
#utilizamos la lib json para almacenar la infor
url = "https://reqres.in/api/users?page=2"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
usesr_data = json.loads(response.text)
print(response)
print(usesr_data)


#ejercicio 2, ingresar un usuario llamado Ignacio y trabajo profesor
#utilizamos el metodo post para ingresarlo
url = "https://reqres.in/api/users"
payload="""{'Nombre': 'Ignacio',
         'Trabajo': 'Profesor'}"""
headers = {}
response = requests.request("POST", url, headers=headers, data=payload)
created_user = json.loads(response.text)
print(response)
print(created_user)

#ejercicio 3, actualizar un usuario llamado 'morpheus'
#utilizaremos el metodo put

#ejercicio 3, actualizar un usuario llamado 'morpheus'
#utilizaremos el metodo put

url = "https://reqres.in/api/users/2"
payload="""{
        "name": "morpheus",
        "residence':'zion'"
            }"""
headers = {}
response = requests.request("PUT", url, headers=headers, data=payload)
updated_user = json.loads(response.text)
print(response)
print(updated_user)

#ejercicio 4, eliminaremos un usuario llamado 'Tracey'
#utilizaremos el metodo DELETE

url = "https://reqres.in/api/users/6"
payload=""
headers = {}
response = requests.request("DELETE", url, headers=headers, data=payload)
print(response)
