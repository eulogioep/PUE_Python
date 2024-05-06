###################
# Sección 1.2.1.3
###################

# import socket

# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

###################
# Sección 1.2.1.5
###################

# import socket

# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))
# sock.send(b"GET / HTTP/1.1\r\n Host: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")

###################
# Sección 1.2.1.6
###################

# import socket

# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))
# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)

###################
# Sección 1.2.1.7
###################

# import socket

# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# print("\nGET / HTTP/1.1\r\n" + 
#       "Host: " + server_addr +
#       "\r\nConnection: close\r\n\r\n")

# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)
# print()
# print(reply)
# try:
#     sock.shutdown(socket.SHUT_RDWR)
# except OSError as e:
#     print(e)

# sock.close()
#############################
# Formatear la respuesta

# import socket

# def parse_response(response):
#     headers, _, body = response.partition('\r\n\r\n')
#     status_line, * headers_lines = headers.split('\r\n')
#     status_code = int(status_line.split()[1])

#     return status_code, headers_lines, body

# server_addr = 'decathlon.com'
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# print("\nGET / HTTP/1.1\r\n" + 
#       "Host: " + server_addr +
#       "\r\nConnection: close\r\n\r\n")

# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")

# response = sock.recv(10000)

# print(response)
# status_code, headers, body = parse_response(response.decode())

# print(f"Status Code: {status_code}")
# print("\nHeaders:")
# for header in headers:
#     print(header)
# print("\nBody:")
# print(body)

#############################
## 301 
#############################
# import socket

# def get_request(host, path):
#     request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, 80))
#         s.sendall(request.encode())

#         response = b""
#         while True:
#             data = s.recv(1024)
#             if not data:
#                 break
#             response += data

#     return response.decode()

# def parse_response(response):
#     headers, _, body = response.partition('\r\n\r\n')
#     status_line, *headers_lines = headers.split('\r\n')
#     status_code = int(status_line.split()[1])

#     return status_code, headers_lines, body

# def handle_redirect(host, path):
#     response = get_request(host, path)
#     status_code, headers, body = parse_response(response)

#     if status_code == 301:
#         for header in headers:
#             if header.startswith('Location:'):
#                 new_location = header.split(':', 1)[1].strip()
#                 new_host, new_path = new_location.split('/', 3)[2:]

#                 return handle_redirect(new_host, '/' + new_path)

#     return status_code, headers, body

# host = 'example.com'
# path = '/'
# status_code, headers, body = handle_redirect(host, path)
# print(f"Status Code: {status_code}")
# print("Headers:")
# for header in headers:
#     print(header)
# print("Body:")
# print(body)

###################
# Sección 1.2.1.8
###################

# import socket

# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))
# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)
# sock.shutdown(socket.SHUT_RDWR)
# sock.close()

# print(repr(reply))

######################################
## Procesar y formatear la respuesta
######################################

# import socket
# from bs4 import BeautifulSoup

# def parse_http_response(reply):
#     try:
#         # intentar decodificar la respuesta usando UTF-8
#         reply_str = reply.decode("utf-8")
#     except UnicodeDecodeError:
#         # Si falla, intentar decodificar la respuesta con ISO-8859-1
#         reply_str = reply.decode("iso-8859-1")
    
#     try:
#         # Dividir la respuesta en status, headers y body
#         status_line, _, rest = reply_str.partition('\r\n')
#         status_code = int(status_line.split()[1])

#         headers_str, _, body = rest.partition('\r\n\r\n')
        
#         # Guardar headers en un diccionario
#         headers = {}
#         for line in headers_str.split('\r\n'):
#             header, value = line.split(': ', 1)
#             headers[header] = value

#         return status_code, headers, body
#     except Exception as e:
#         print("Error parsing HTTP response:", e)
#         return None, None, None

# #############
# server_addr = input("What server do you want to connect to? ")
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))
# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)
# sock.shutdown(socket.SHUT_RDWR)
# sock.close()

# # Parsear la respuesta HTTP
# status_code, headers, body = parse_http_response(reply)

# # Imprimir código de estado HTTP
# print("\nStatus Code:", status_code)

# # Imprimir encabezados de la respuesta
# print("\nHeaders:", '\n')
# for header, value in headers.items():
#     print(header + ": " + value)

# # Imprimir el body formateado en HTML
# try:
#     soup = BeautifulSoup(body, 'html.parser')
    
#     print("\nBody (HTML):\n")
#     print(soup.prettify())
# except Exception as e:
#     print("Error printing HTML body:", e)

###################
# Sección 1.4.1.1
###################

# # The first of our samples takes a number and outputs a number – we don't expect anything more:

# import json

# electron = 1.602176620898E10-19
# print(json.dumps(electron))

# #####################################
# # Now’s a good moment to introduce a list. What do you think about this example?

# import json

# my_list = [1, 2.34, True, "False", None, ['a', 0]]
# print(json.dumps(my_list))

# #######################################
# # Let’s check a dictionary. Here’s a simple test:

# import json

# my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
# print(json.dumps(my_dict))

###################
# Sección 1.4.1.2
###################

# import json

# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# some_man = Who('John Doe', 42)
# print(json.dumps(some_man))

#####################

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

###################
# Sección 1.4.1.3
###################

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

##################

# import json

# jstr = '16021766189.98'
# electron = json.loads(jstr)
# print(type(electron))
# print(electron)

# ###################

# import json

# jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
# comics = json.loads(jstr)
# print(type(comics))
# print(comics)

###################
# Sección 1.4.1.4
###################

# import json

# jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
# my_list = json.loads(jstr)
# print(type(my_list))
# print(my_list)

####################

# import json

# json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
# my_dict = json.loads(json_str)
# print(type(my_dict))
# print(my_dict)

####################

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

###################
# Sección 1.4.1.5
###################

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
#             return super().default(self, w)

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

#################################################################
## Serialización y deserialización de objetos complejos con json
#################################################################

# import json

# class Order:
#     def __init__(self, order_id, product_name, quantity, price):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.quantity = quantity
#         self.price = price

# class Customer:
#     def __init__(self, customer_id, name, orders):
#         self.customer_id = customer_id
#         self.name = name
#         self.orders = orders

# class CustomEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Order):
#             return {
#                 "order_id": obj.order_id,
#                 "product_name": obj.product_name,
#                 "quantity": obj.quantity,
#                 "price": obj.price
#             }
#         elif isinstance(obj, Customer):
#             return {
#                 "customer_id": obj.customer_id,
#                 "name": obj.name,
#                 "orders": obj.orders
#             }
#         return json.JSONEncoder.default(self, obj)

# class CustomDecoder(json.JSONDecoder):
#     def decode(self, json_string):
#         decoded = super().decode(json_string)
#         if "customer_id" in decoded:
#             orders = []
#             for order_data in decoded["orders"]:
#                 order = Order(
#                     order_data["order_id"],
#                     order_data["product_name"],
#                     order_data["quantity"],
#                     order_data["price"]
#                 )
#                 orders.append(order)
#             return Customer(decoded["customer_id"], decoded["name"], orders)
#         return decoded
    
# #######################################

# order1 = Order(1, "Laptop", 2, 1200)
# order2 = Order(2, "Phone", 1, 800)
# customer = Customer(101, "John Doe", [order1, order2])

# serialized_customer = json.dumps(customer, cls=CustomEncoder)
# print("\nSerialized:\n", serialized_customer)

# deserialized_customer = json.loads(serialized_customer, cls=CustomDecoder)
# print("\nDeserialized:\n")
# print("Customer ID:", deserialized_customer.customer_id)
# print("Name:", deserialized_customer.name)
# print("Orders:")
# for order in deserialized_customer.orders:
#     print("- Order ID:", order.order_id)
#     print("  Product:", order.product_name)
#     print("  Quantity:", order.quantity)
#     print("  Price:", order.price)

###################
# Sección 1.5.1.7
###################

# import xml.etree.ElementTree

# cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
# print(cars_for_sale.tag)
# for car in cars_for_sale.findall('car'):
#     print('\t', car.tag)
#     for prop in car:
#         print('\t\t', prop.tag, (prop.attrib if prop.tag == 'price' else ''), '=', prop.text, end='\n')

###################
# Sección 1.5.1.8
###################

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

#################################################################
## Serialización y deserialización de objetos complejos con xml
#################################################################

# import xml.etree.ElementTree as ET

# class Order:
#     def __init__(self, order_id, product_name, quantity, price):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.quantity = quantity
#         self.price = price

# class Customer:
#     def __init__(self, customer_id, name, orders):
#         self.customer_id = customer_id
#         self.name = name
#         self.orders = orders

# def serialize_customer_to_xml(customer):
#     root = ET.Element("Customer")
#     customer_id_element = ET.SubElement(root, "CustomerID")
#     customer_id_element.text = str(customer.customer_id)
#     name_element = ET.SubElement(root, "Name")
#     name_element.text = customer.name
#     orders_element = ET.SubElement(root, "Orders")
#     for order in customer.orders:
#         order_element = ET.SubElement(orders_element, "Order")
#         order_id_element = ET.SubElement(order_element, "OrderID")
#         order_id_element.text = str(order.order_id)
#         product_name_element = ET.SubElement(order_element, "ProductName")
#         product_name_element.text = order.product_name
#         quantity_element = ET.SubElement(order_element, "Quantity")
#         quantity_element.text = str(order.quantity)
#         price_element = ET.SubElement(order_element, "Price")
#         price_element.text = str(order.price)
#     return ET.tostring(root)

# def deserialize_customer_from_xml(xml_string):
#     root = ET.fromstring(xml_string)
#     customer_id = int(root.find("CustomerID").text)
#     name = root.find("Name").text
#     orders = []
#     for order_element in root.find("Orders").findall("Order"):
#         order_id = int(order_element.find("OrderID").text)
#         product_name = order_element.find("ProductName").text
#         quantity = int(order_element.find("Quantity").text)
#         price = float(order_element.find("Price").text)
#         orders.append(Order(order_id, product_name, quantity, price))
#     return Customer(customer_id, name, orders)

# order1 = Order(1, "Laptop", 2, 1200)
# order2 = Order(2, "Phone", 1, 800)
# customer = Customer(101, "John Doe", [order1, order2])

# serialized_customer_xml = serialize_customer_to_xml(customer)
# print("Serialized XML:")
# print(serialized_customer_xml.decode())

# deserialized_customer = deserialize_customer_from_xml(serialized_customer_xml)
# print("\nDeserialized:")
# print("Customer ID:", deserialized_customer.customer_id)
# print("Name:", deserialized_customer.name)
# print("Orders:")
# for order in deserialized_customer.orders:
#     print("- Order ID:", order.order_id)
#     print("  Product:", order.product_name)
#     print("  Quantity:", order.quantity)
#     print("  Price:", order.price)

###################
# Sección 1.6.1.5
###################

# import requests

# reply = requests.get('http://localhost:3000')
# print(reply.status_code)

########################

# import requests

# print(requests.codes.__dict__)

########################

# if reply.status_code == requests.codes.ok:

########################

# import requests

# reply = requests.get('http://localhost:3000')
# if reply.status_code == requests.codes.ok:
#     print("Solicitud correcta!")

########################

# import requests

# reply = requests.get('http://localhost:3000')

# for header in reply.headers:
#     print(header, ': ', reply.headers[header], sep='')

###################
# Sección 1.6.1.6
###################

# import requests

# reply = requests.get('http://localhost:3000')
# print(reply.text)

###################
# Sección 1.6.1.9
###################

# import requests

# try:
#     reply = requests.get('http://localhost:3000', timeout=1)
# except requests.exceptions.Timeout:
#     print('Sorry, Mr. Impatient, you didn\'t get your data')
# else:
#     print('Here is your data, my Master!')

##########################

# import requests

# try:
#     reply = requests.get('http://localhost:3001', timeout=1)
# except requests.exceptions.ConnectionError:
#     print('Nobody\'s home, sorry!')
# else:
#     print('Everything fine!')

###################
# Sección 1.6.1.10
###################

# import requests

# try:
#     reply = requests.get('http:////////////')
# except requests.exceptions.InvalidURL:
#     print('Recipient unknown!')
# else:
#     print('Everything fine!')

###################
# Sección 1.7.1.2
###################

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

###################
# Sección 1.7.1.3
###################

# import requests

# try:
#     reply = requests.get("http://localhost:3000/cars")
# except:
#     print("Communication error")
# else:
#     if reply.status_code == requests.codes.ok:
#        if reply.headers['Content-Type'] == 'application/json':
#             print(reply.json())
#     else:
#         print("Server error")

###################
# Sección 1.7.1.4
###################
        
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

###################
# Sección 1.7.1.5
###################

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
#     reply = requests.get('http://localhost:3000/cars/2')
# except requests.RequestException:
#     print('Communication error')
# else:
#     if reply.status_code == requests.codes.ok:
#         show(reply.json())
#     elif reply.status_code == requests.codes.not_found:
#         print("Resource not found")
#     else:
#         print('Server error')

###################
# Sección 1.7.1.6
###################

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

###################
# Sección 1.7.1.7
###################
        
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


###################
# Sección 1.7.1.8
###################

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

###################
# Sección 1.7.1.9
###################

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
#     reply = requests.delete('http://localhost:3000/cars/1')
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

###################
# Sección 1.7.1.10
###################
        
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
# new_car = {'id': 8,
#            'brand': 'Porsche',
#            'model': '911',
#            'production_year': 1963,
#            'convertible': False}
# print(json.dumps(new_car))
# try:
#     reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
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

###################
# Sección 1.7.1.11
###################
        
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
#        'production_year': 1967,
#        'convertible': True}
# try:
#     reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
#     print("res=" + str(reply.status_code))
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

##################################
# Laboratorio de Sección 2.1.1.1
##################################

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

##################################
# Laboratorio de Sección 2.1.1.2
##################################
        
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

################################
## alternativa a decoder
################################
## class MyDecoder(json.JSONDecoder):
##      def decode(self, json_string):
##          decoded = super().decode(json_string)

##          if "registration_number" in decoded:
##             new_vehicle = Vehicle() 
##             new_vehicle.registration_number = decoded["registration_number"]
##             new_vehicle.year_of_production = decoded["year_of_production"]
##             new_vehicle.passenger = decoded["passenger"]
##             new_vehicle.mass = decoded["mass"]
##             return new_vehicle

##          return decoded
##################################

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

##################################
# Laboratorio de Sección 2.1.1.3
##################################

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

##################################
# Laboratorio de Sección 2.1.1.4
##################################

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

##################################
# Laboratorio de Sección 2.1.1.5
##################################

# import requests
# import json


# Service_URI = 'http://localhost:3000/cars/'
# h_close = {'Connection': 'Close'}
# h_content = {'Content-Type': 'application/json'}
# column_headers = ["id", "brand", "model", "production_year", "convertible"]
# column_witdhs = [10, 15, 10, 20, 15]


# def check_server(cid=None):
#     # returns True or False;
#     # when invoked without arguments simply checks if server responds;
#     # invoked with car ID checks if the ID is present in the database;
#     uri = Service_URI
#     if cid:
#         uri += str(cid)
#         print(uri)
#     try:
#         res = requests.head(uri, headers=h_close)
#     except requests.exceptions.RequestException:
#         return False
#     return res.status_code == requests.codes.ok


# def print_menu():
#     # prints user menu - nothing else happens here;
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
#     # reads user choice and checks if it's valid;
#     # returns '0', '1', '2', '3' or '4' 
#     ok = False
#     while not ok:
#         answer = input("Enter your choice (0..4): ")
#         ok = answer in ['0', '1', '2', '3', '4']
#         if ok:
#             return answer
#         print("Bad choice!")


# def print_header():
#     # prints elegant cars table header;
#     for (head, width) in zip(column_headers, column_witdhs):
#         print(head.ljust(width), end='| ')
#     print()


# def print_car(car):
#     # prints one car's data in a way that fits the header;
#     for (name, width) in zip(column_headers, column_witdhs):
#         print(str(car[name]).ljust(width), end='| ')
#     print()


# def list_cars():
#     # gets all cars' data from server and prints it;
#     # if the database is empty prints diagnostic message instead;
#     try:
#         res = requests.get(Service_URI)
#     except requests.exceptions.Requ1estException:
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
#     # checks if name (brand or model) is valid;
#     # valid name is non-empty string containing
#     # digits, letters and spaces;
#     # returns True or False;
#     for char in name:
#         if not (char.isspace() or char.isdigit() or char.isalpha()):
#             return False
#     return True


# def enter_id():
#     # allows user to enter car's ID and checks if it's valid;
#     # valid ID consists of digits only;
#     # returns int or None (if user enters an empty line);
#     while True:
#         id = input("Car ID (empty string to exit): ")
#         if not id or id.isspace():
#             return None
#         if not id.isdigit():
#             print("Invalid ID - re-enter.")
#             continue
#         return id


# def enter_production_year():
#     # allows user to enter car's production year and checks if it's valid;
#     # valid production year is an int from range 1900..2000;
#     # returns int or None  (if user enters an empty line);
#     while True:
#         prod_year = input("Car production year (empty string to exit): ")
#         if not prod_year or prod_year.isspace():
#             return None
#         if not prod_year.isdigit() or not (1900 <= int(prod_year) <= 2000):
#             print("Invalid production year - re-enter.")
#             continue
#         return int(prod_year)


# def enter_name(what):
#     # allows user to enter car's name (brand or model) and checks if it's valid;
#     # uses name_is_valid() to check the entered name;
#     # returns string or None  (if user enters an empty line);
#     # argument describes which of two names is entered currently ('brand' or 'model');
#     while True:
#         name = input("Car " + what + " (empty string to exit): ")
#         if name == '' or name.isspace():
#             return None
#         if not name_is_valid(name):
#             print(what.title() + ' contains illegal characters - re-enter.')
#             continue
#         return name.title()


# def enter_convertible():
#     # allows user to enter Yes/No answer determining if the car is convertible;
#     # returns True, False or None  (if user enters an empty line);
#     while True:
#         conv = input("Is this car convertible? [y/n] (empty string to exit): ")
#         if conv == '':
#             return None
#         if conv.upper() not in ['Y', 'N']:
#             print("Invalid input - re-enter.")
#             continue
#         return conv in ['y', 'Y']


# def delete_car():
#     # asks user for car's ID and tries to delete it from database;
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
#     # lets user enter car data;
#     # argument determines if the car's ID is entered (True) or not (False);
#     # returns None if user cancels the operation or a dictionary of the following structure:
#     # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
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
#     # invokes input_car_data(True) to gather car's info and adds it to the database;
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
#     # invokes enter_id() to get car's ID if the ID is present in the database;
#     # invokes input_car_data(False) to gather new car's info and updates the database;
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
