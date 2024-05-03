# # Conectarse a un servidor http

# import socket

# #server_addr = input("What server do you want to connect to? ")
# server_addr = 'example.com'
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# # Solicitud de un documento al server
# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)

# # Cierra la conexión con el server.
# sock.shutdown(socket.SHUT_RDWR)
# sock.close()

# # Imprimir la respuesta
# print(repr(reply))

###########################################################

# Conexión y parseo de la respuesta a un server http.

# import socket

# def parse_response(response):
#     headers, _, body = response.partition('\r\n\r\n')
#     status_line, * headers_lines = headers.split('\r\n')
#     status_code = int(status_line.split()[1])

#     return status_code, headers_lines, body

# server_addr = 'example.com'
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# print("\nGET / HTTP/1.1\r\n" + 
#       "Host: " + server_addr +
#       "\r\nConnection: close\r\n\r\n")

# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")

# response = sock.recv(10000)
# status_code, headers, body = parse_response(response.decode())

# print(f"Status Code: {status_code}")
# print("\nHeaders:")
# for header in headers:
#     print(header)
# print("\nBody:")
# print(body)

###### Procesar información JSON ##############################################

#################################################
# Python Data                      JSON element  #
#------------------------------------------------#
# dict                              object
# list o tuple                      array
# string                            string
# int o float                       number
# True o False                      true o false
# None                              null

###################################################

# Pasando números a Json

# import json

# electron = 1.602176620898E10-19
# print(json.dumps(electron))

###################

# Pasando String a Json

# import json

# comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
# print(json.dumps(comics))

##########

# Pasando List a Json

# import json

# my_list = [1, 2.34, True, "False", None, ['a', 0]]
# print(json.dumps(my_list))

###########

# Pasando Diccionario a Json

# import json

# my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
# print(json.dumps(my_dict))

##########

# Json no reconoce otros tipos así que hay que informarle cómo hacer la traducción.

###

# Como Función

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


# some_man = Who('John Doe', 42)
# print(json.dumps(some_man, default=encode_who))


###

# Como Clase

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class MyEncoder(json.JSONEncoder):
#     def default(self, w):
#         if isinstance(w, Who):
#             return w.__dict__
#         else:
#             return super().default(self, z)


# some_man = Who('John Doe', 42)
# print(json.dumps(some_man, cls=MyEncoder))

##### Convertir de JSON a Python

## Números

# import json

# jstr = '16021766189.98'
# electron = json.loads(jstr)
# print(type(electron))
# print(electron)

### Strings

# import json

# jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
# comics = json.loads(jstr)
# print(type(comics))
# print(comics)

### Lists

# import json

# jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
# my_list = json.loads(jstr)
# print(type(my_list))
# print(my_list)

### Dicionario

# import json

# json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
# my_dict = json.loads(json_str)
# print(type(my_dict))
# print(my_dict)

### Serializar y deserializar: OBJETOS <-> JSON

### Como Función

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + 'is not JSON serializable')


# def decode_who(w):
#     return Who(w['name'], w['age'])


# old_man = Who("Jane Doe", 23)
# json_str = json.dumps(old_man, default=encode_who)
# new_man = json.loads(json_str, object_hook=decode_who)
# print(type(new_man))
# print(new_man.__dict__)

### Como Clase

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class MyEncoder(json.JSONEncoder):
#     def default(self, w):
#         if isinstance(w, Who):
#             return w.__dict__
#         else:
#             return super().default(self, z)


# class MyDecoder(json.JSONDecoder):
#     def __init__(self):
#         json.JSONDecoder.__init__(self, object_hook=self.decode_who)

#     def decode_who(self, d):
#         return Who(**d)


# some_man = Who('Jane Doe', 23)
# json_str = json.dumps(some_man, cls=MyEncoder)
# new_man = json.loads(json_str, cls=MyDecoder)

# print(type(new_man))
# print(new_man.__dict__)


############# Trabajando con XML #########################

# import xml.etree.ElementTree

# cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
# print(cars_for_sale.tag)
# for car in cars_for_sale.findall('car'):
#     print('\t', car.tag)
#     for prop in car:
#         print('\t\t', prop.tag, end='')
#         if prop.tag == 'price':
#             print(prop.attrib, end='')
#     print(' =', prop.text)

##############

# import xml.etree.ElementTree

# tree = xml.etree.ElementTree.parse('cars.xml')
# cars_for_sale = tree.getroot()
# for car in cars_for_sale.findall('car'):
#     if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
#         cars_for_sale.remove(car)
#         break
# new_car = xml.etree.ElementTree.Element('car')
# xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
# xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
# xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
# xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
# xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
# cars_for_sale.append(new_car)
# tree.write('newcars.xml', method='')


########## Pruebas con Node.js ########################

### Montar un mini server con un archivo json para pruebas

# En la consola: npm install -g json-server

# Levantar el Servidor en consola: json-server --watch cars.json

### Probar con 'request'

# import requests

# reply = requests.get('http://localhost:3000')
# print(reply.status_code)

# Respuesta: 200 si encuentra el recurso.

### Ver el diccionario de respuestas de 'requests'

# import requests

# print(requests.codes.__dict__)

### Ver el encabezado respondido (Headers)

# import requests

# reply = requests.get('http://localhost:3000')
# #print(reply.headers)
# #print(reply.headers['X-Powered-By'])

### Ver el Body de la respuesta del server

# import requests

# reply = requests.get('http://localhost:3000')
# print(reply.text)

### 







