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

### Ver el diccionario de respuestas de 'requests'o código de respuesta

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

### Los 3 datos en un sólo programa.

# import requests

# reply = requests.get('http://localhost:3000')

# print(reply.status_code)

# print(reply.headers)

# print(reply.text)

################################

# POST (No Idempotente) y PUT (Idempotente)
# POST: Crear recurso y PUT: Actualizar recurso.
# DELETE: Eliminar recurso.


########## Excepción del tiempo de respuesta. #########

# import requests

# try:
#     reply = requests.get('http://localhost:3000', timeout=1) # Para probar, se cambia el timeout a 0.00000000000001
# except requests.exceptions.Timeout:
#     print('Sorry, Mr. Impatient, you didn\'t get your data')
# else:
#     print('Here is your data, my Master!')


######## Error de conexión #########

# import requests

# try:
#     reply = requests.get('http://localhost:3001', timeout=1)
# except requests.exceptions.ConnectionError:
#     print('Nobody\'s home, sorry!')
# else:
#     print('Everything fine!')


##### Error de URL #########################

# import requests

# try:
#     reply = requests.get('http:////////////')
# except requests.exceptions.InvalidURL:
#     print('Recipient unknown!')
# else:
#     print('Everything fine!')

####### CRUD ################
# CREATE
# READ
# UPDATE
# DELETE

### READ ###

# import requests

# try:
#     reply = requests.get("http://localhost:3000/cars")
# except requests.RequestException:
#     print("Communication error")
# else:
#     if reply.status_code == requests.codes.ok:
#         print(reply.text)
#     else:
#         print("Server error")


### Si la lectura es correcta, muestra la cabecera ###

# import requests

# try:
#     reply = requests.get("http://localhost:3000/cars")
# except:
#     print("Communication error")
# else:
#     if reply.status_code == requests.codes.ok:
#         if reply.headers['Content-Type'] == 'application/json':
#             print(reply.json())
#     else:
#         print("Server error")


### Misma información pero formateado para mejor visión ###

# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     for car in json:
#         show_car(car)


# try:
#     reply = requests.get('http://localhost:3000/cars')
# except requests.RequestException:
#     print('Communication error')
# else:
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     else:
#         print('Server error')



###### Recuperar un sólo recurso ###

# Según el id
# http://server:port/resource/id

# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# try:
#     reply = requests.get('http://localhost:3000/cars/2') # Se indica el id
# except requests.RequestException:
#     print('Communication error')
# else:
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

######## Ordenar los datos recibidos ###


# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# try:
#     reply = requests.get('http://localhost:3000/cars?_sort=production_year')
# except requests.RequestException:
#     print('Communication error')
# else:
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

######## Este ejemplo funciona con Node en versiones más antiguas

# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# try:
#     reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
# except requests.RequestException:
#     print('Communication error')
# else:
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

####### Ejemplo con keep-alive. Mantiene la sesión viva.

# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# try:
#     reply = requests.get('http://localhost:3000/cars')
# except requests.RequestException:
#     print('Communication error')
# else:
#     print('Connection=' + reply.headers['Connection'])
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')


###### DELETE  Operaciones de eliminación ###########

# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# headers = {'Connection': 'Close'}
# try:
#     reply = requests.delete('http://localhost:3000/cars/2')
#     print("res=" + str(reply.status_code))
#     reply = requests.get('http://localhost:3000/cars/', headers=headers)
# except requests.RequestException:
#     print('Communication error')
# else:
#     print('Connection=' + reply.headers['Connection'])
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

### CREATE Agrega nueva información ###
# POST: Agrega la misma información con nuevos registros


# import json
# import requests

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# h_close = {'Connection': 'Close'}
# h_content = {'Content-Type': 'application/json'}
# new_car = {'id': 7,
#            'brand': 'Porsche',
#            'model': '911',
#            'production_year': 1963,
#            'convertible': False}
# print(json.dumps(new_car))
# try:
#     reply = requests.put('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
#     print("reply=" + str(reply.status_code))
#     reply = requests.get('http://localhost:3000/cars/', headers=h_close)
# except requests.RequestException:
#     print('Communication error')
# else:
#     print('Connection=' + reply.headers['Connection'])
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

###
# PUT: Actualiza el registro creado.

# import requests, json

# key_names = ["id", "brand", "model", "production_year", "convertible"]
# key_widths = [10, 15, 10, 20, 15]


# def show_head():
#     for (n, w) in zip(key_names, key_widths):
#         print(n.ljust(w), end='| ')
#     print()


# def show_empty():
#     for w in key_widths:
#         print(' '.ljust(w), end='| ')
#     print()


# def show_car(car):
#     for (n, w) in zip(key_names, key_widths):
#         print(str(car[n]).ljust(w), end='| ')
#     print()


# def show(json):
#     show_head()
#     if type(json) is list:
#         for car in json:
#             show_car(car)
#     elif type(json) is dict:
#         if json:
#             show_car(json)
#         else:
#             show_empty()


# h_close = {'Connection': 'Close'}
# h_content = {'Content-Type': 'application/json'}
# car = {'id': 6,
#        'brand': 'Mercedes Benz',
#        'model': '300SL',
#        'production_year': 2000,
#        'convertible': True}
# try:
#     reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
#     print("res=" + str(reply.headers))
#     print(reply.text)
#     reply = requests.get('http://localhost:3000/cars/', headers=h_close)
# except requests.RequestException:
#     print('Communication error')
# else:
#     print('Connection=' + reply.headers['Connection'])
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

################## Laboratorios ########################

# Uso del módulo socket y sus funciones básicas.

# import sys
# import socket

# if len(sys.argv) not in [2, 3]:
#     print("Improper number of arguments: at least one is required" +
#           "and not more than two are allowed:")
#     print("- http server's address (required)")
#     print("- port number (defaults to 80 if not specified)")
#     exit(1)

# addr = sys.argv[1]
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) == 3:
#     try:
#         port = int(sys.argv[2])
#         if not (1 <= port <= 65535):
#             raise ValueError
#     except ValueError:
#         print("Port number is invalid - exiting.")
#         exit(2)
# else:
#     port = 80

# try:
#     sock.connect((addr, port))
# except socket.timeout:
#     print("The server" + addr + "seems to be dead - sorry.")
#     exit(3)
# except socket.gaierror:
#     print("Server address" + addr + "is invalid or malformed - sorry.")
#     exit(4)

# request = b"HEAD / HTTP/1.0\r\nHost: " + \
#           bytes(addr, "utf8") + \
#           b"\r\nConnection:close\r\n\r\n"

# sock.send(request)
# answer = sock.recv(100).decode("utf8")
# sock.shutdown(socket.SHUT_RDWR)
# sock.close()
# print(answer[:answer.find('\r')])

##########

# Uso del módulo JSON y sus funciones básicas.

# import json


# class Vehicle:
#     def __init__(self, registration_number, year_of_production, passenger, mass):
#         self.registration_number = registration_number
#         self.year_of_production = year_of_production
#         self.passenger = passenger
#         self.mass = mass


# class MyEncoder(json.JSONEncoder):
#     def default(self, veh):
#         if isinstance(veh, Vehicle):
#             return veh.__dict__
#         else:
#             return super().default(self, veh)


# class MyDecoder(json.JSONDecoder):
#     def __init__(self):
#         json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

#     def decode_vehicle(self, veh):
#         return Vehicle(**veh)


# print("What can I do for you?")
# print("1 - produce a JSON string describing a vehicle")
# print("2 - decode a JSON string into vehicle data")
# answer = ''
# while answer not in ['1', '2']:
#     answer = input("Your choice: ")
# if answer == '1':
#     rn = input("Registration number: ")
#     yop = int(input("Year of production: "))
#     psg = input("Passenger [y/n]: ").upper() == 'Y'
#     mss = float(input("Vehicle mass: "))
#     vehicle = Vehicle(rn, yop, psg, mss)
#     print("Resulting JSON string is:")
#     print(json.dumps(vehicle, cls=MyEncoder))
# else:
#     json_str = input("Enter vehicle JSON string: ")
#     try:
#         new_car = json.loads(json_str, cls=MyDecoder)
#         print(new_car.__dict__)
#     except TypeError:
#         print("The JSON string doesn't describe a valid vehicle")
# print("Done")

###########

# Lectura de XML y parseo del mismo.

# import xml.etree.ElementTree

# try:
#     NYSE = xml.etree.ElementTree.parse('nyse.xml')
# except FileNotFoundError:
#     print("Stock data file not found")
#     exit(1)
# except xml.etree.ElementTree.ParseError:
#     print("Stock data file contains invalid data")
#     exit(2)
# quotes = NYSE.getroot()
# print('COMPANY'.ljust(40), end='')
# print('LAST'.ljust(10), end='')
# print('CHANGE'.ljust(10), end='')
# print('MIN'.ljust(10), end='')
# print('MAX'.ljust(10), end='')
# print()
# print('-' * 80)
# for quote in quotes.findall('quote'):
#     print(quote.text.ljust(40), end='')
#     print(quote.attrib['last'].ljust(10), end='')
#     print(quote.attrib['change'].ljust(10), end='')
#     print(quote.attrib['min'].ljust(10), end='')
#     print(quote.attrib['max'].ljust(10), end='')
#     print()

################

# Uso del módulo 'requests'

# import sys
# import requests

# if len(sys.argv) not in [2, 3]:
#     print("Improper number of arguments: at least one is required " +
#           "and not more than two are allowed:")
#     print("- http server's address (required)")
#     print("- port number (defaults to 80 if not specified)")
#     exit(1)

# addr = sys.argv[1]
# URI = 'http://' + sys.argv[1]
# if len(sys.argv) == 3:
#     try:
#         port = int(sys.argv[2])
#         if not (1 <= port <= 65535):
#             raise ValueError
#     except ValueError:
#         print("Port number is invalid - exiting.")
#         exit(2)
#     URI += ':' + str(port)
# URI += '/'

# try:
#     response = requests.head(URI)
# except requests.exceptions.InvalidURL:
#     print("The given URL '" + sys.argv[1] + "' is invalid.")
#     exit(3)
# except requests.exceptions.ConnectionError:
#     print("Cannot connect to '" + addr + "'.")
#     exit(4)
# except requests.exceptions.RequestException:
#     print("Some problems appeared - sorry.")
#     exit(5)

# print(response.status_code,  response.reason)


##############

# Requests y uso de REST con una DB

# import requests
# import json


# Service_URI = 'http://localhost:3000/cars/'
# h_close = {'Connection': 'Close'}
# h_content = {'Content-Type': 'application/json'}
# column_headers = ["id", "brand", "model", "production_year", "convertible"]
# column_witdhs = [10, 15, 10, 20, 15]


# def check_server(cid=None):
#     uri = Service_URI
#     if cid:
#         uri += str(cid)
#     try:
#         res = requests.head(uri, headers=h_close)
#     except requests.exceptions.RequestException:
#         return False
#     return res.status_code == requests.codes.ok


# def print_menu():
#     print("+-----------------------------------+")
#     print("|       Vintage Cars Database       |")
#     print("+-----------------------------------+")
#     print("M E N U")
#     print("=======")
#     print("1. List cars")
#     print("2. Add new car")
#     print("3. Delete car")
#     print("4. Update car")
#     print("0. Exit")


# def read_user_choice():
#     ok = False
#     while not ok:
#         answer = input("Enter your choice (0..4): ")
#         ok = answer in ['0', '1', '2', '3', '4']
#         if ok:
#             return answer
#         print("Bad choice!")


# def print_header():
#     for (head, width) in zip(column_headers, column_witdhs):
#         print(head.ljust(width), end='| ')
#     print()


# def print_car(car):
#     for (name, width) in zip(column_headers, column_witdhs):
#         print(str(car[name]).ljust(width), end='| ')
#     print()


# def list_cars():
#     try:
#         res = requests.get(Service_URI)
#     except requests.exceptions.RequestException:
#         print("Communication error :(")
#         return
#     cars = res.json()
#     if len(cars) == 0:
#         print("*** Database is empty ***")
#         return
#     print_header()
#     for car in cars:
#         print_car((car))
#     print()


# def name_is_valid(name):
#     for char in name:
#         if not (char.isspace() or char.isdigit() or char.isalpha()):
#             return False
#     return True


# def enter_id():
#     while True:
#         id = input("Car ID (empty string to exit): ")
#         if not id or id.isspace():
#             return None
#         if not id.isdigit():
#             print("Invalid ID - re-enter.")
#             continue
#         return int(id)


# def enter_production_year():
#     while True:
#         prod_year = input("Car production year (empty string to exit): ")
#         if not prod_year or prod_year.isspace():
#             return None
#         if not prod_year.isdigit() or not (1900 <= int(prod_year) <= 2000):
#             print("Invalid production year - re-enter.")
#             continue
#         return int(prod_year)


# def enter_name(what):
#     while True:
#         name = input("Car " + what + " (empty string to exit): ")
#         if name == '' or name.isspace():
#             return None
#         if not name_is_valid(name):
#             print(what.title() + ' contains illegal characters - re-enter.')
#             continue
#         return name.title()


# def enter_convertible():
#     while True:
#         conv = input("Is this car convertible? [y/n] (empty string to exit): ")
#         if conv == '':
#             return None
#         if conv.upper() not in ['Y', 'N']:
#             print("Invalid input - re-enter.")
#             continue
#         return conv in ['y', 'Y']


# def delete_car():
#     while True:
#         id = enter_id()
#         if not id:
#             return
#         try:
#             res = requests.delete(Service_URI + str(id))
#         except requests.exceptions.RequestException:
#             print('Communication error - delete failed.')
#             return
#         if res.status_code == requests.codes.not_found:
#             print("Unknown ID - nothing has been deleted")
#             continue
#         print("Success!")


# def input_car_data(with_id):
#     if with_id:
#         car_id = enter_id()
#         if car_id is None:
#             return {}
#     else:
#         car_id = 0
#     brand = enter_name('brand')
#     if brand is None:
#         return {}
#     model = enter_name('model')
#     if model is None:
#         return {}
#     prod_year = enter_production_year()
#     if prod_year is None:
#         return {}
#     conv = enter_convertible()
#     if conv is None:
#         return {}
#     return {'id': car_id, 'brand': brand, 'model': model, 'production_year': prod_year, 'convertible': conv}


# def add_car():
#     new_car = input_car_data(True)
#     if not new_car:
#         return
#     try:
#         res = requests.post(Service_URI, headers=h_content, data=json.dumps(new_car))
#     except requests.exceptions.RequestException:
#         print('Communication error - adding new car failed')
#         return
#     if res.status_code != 201:
#         print("Duplicated car ID - adding new car failed")


# def update_car():
#     while True:
#         car_id = enter_id()
#         if not car_id:
#             return
#         if not check_server(car_id):
#             print("Car ID not found in the database.")
#         else:
#             break
#     car = input_car_data(False)
#     if not car:
#         return

#     car["id"] = car_id
#     try:
#         res = requests.put(Service_URI + str(car_id), headers=h_content, data=json.dumps(car))
#     except requests.exceptions.RequestException:
#         print('Communication error - updating car data failed')
#         return
#     if res.status_code != requests.codes.ok:
#         print("Duplicated car ID - adding new car failed")


# while True:
#     if not check_server():
#         print("Server is not responding - quitting!")
#         exit(1)
#     print_menu()
#     choice = read_user_choice()
#     if choice == '0':
#         print("Bye!")
#         exit(0)
#     elif choice == '1':
#         list_cars()
#     elif choice == '2':
#         add_car()
#     elif choice == '3':
#         delete_car()
#     elif choice == '4':
#         update_car()




