################################
# Sección 4.1.1.3
################################

# a_string = '10 days to departure'
# b_string = '20 days to departure'

# print('a_string identity:', id(a_string))
# print('b_string identity:', id(b_string))

################################
# Sección 4.1.1.4
################################

# a_string = '10 days to departure'
# b_string = a_string

# print('a_string identity:', id(a_string))
# print('b_string identity:', id(b_string))

################################
# Sección 4.1.1.5
################################

# a_string = ['10', 'days', 'to', 'departure']
# b_string = a_string

# print('a_string identity:', id(a_string))
# print('b_string identity:', id(b_string))
# print('The result of the value comparison:', a_string == b_string)
# print('The result of the identity comparison:', a_string is b_string)

# print()

# a_string = ['10', 'days', 'to', 'departure']
# b_string = ['10', 'days', 'to', 'departure']

# print('a_string identity:', id(a_string))
# print('b_string identity:', id(b_string))
# print('The result of the value comparison:', a_string == b_string)
# print('The result of the identity comparison:', a_string is b_string)

################################
# Sección 4.1.1.6
################################

# print("Part 1")
# print("Let's make a copy")
# a_list = [10, "banana", [997, 123]]
# b_list = a_list[:]
# print("a_list contents:", a_list)
# print("b_list contents:", b_list)
# print("Is it the same object?", a_list is b_list)

# print()
# print("Part 2")
# print("Let's modify b_list[2]")
# b_list[2][0] = 112
# print("a_list contents:", a_list)
# print("b_list contents:", b_list)
# print("Is it the same object?", a_list is b_list)

################################
# Sección 4.1.1.8
################################

# import copy

# print("Let's make a deep copy")
# a_list = [10, "banana", [997, 123]]
# b_list = copy.deepcopy(a_list)
# print("a_list contents:", a_list)
# print("b_list contents:", b_list)
# print("Is it the same object?", a_list is b_list)

# print()
# print("Let's modify b_list[2]")
# b_list[2][0] = 112
# print("a_list contents:", a_list)
# print("b_list contents:", b_list)
# print("Is it the same object?", a_list is b_list)

# ######

# print('Id a_list',id(a_list))
# for elemento in a_list:
#     print('\tId de elemento:',id(elemento))

# print('Id b_list',id(b_list))
# for elemento in b_list:
#     print('\tId de elemento:',id(elemento))

################################
# Sección 4.1.1.9
################################

# import copy
# import time

# a_list = [(1,2,3) for x in range(1_000_000)]

# print('Single reference copy')
# time_start = time.time()
# b_list = a_list
# print('Execution time:', round(time.time() - time_start, 3))
# print('Memory chunks:', id(a_list), id(b_list))
# print('Same memory chunk?', a_list is b_list)

# print()

# print('Shallow copy')
# time_start = time.time()
# b_list = a_list[:]
# print('Execution time:', round(time.time() - time_start, 3))
# print('Memory chunks:', id(a_list), id(b_list))
# print('Same memory chunk?', a_list is b_list)

# print()

# print('Deep copy')
# time_start = time.time()
# b_list = copy.deepcopy(a_list)
# print('Execution time:', round(time.time() - time_start, 3))
# print('Memory chunks:', id(a_list), id(b_list))
# print('Same memory chunk?', a_list is b_list)

################################
# Sección 4.1.1.10
################################

# import copy

# a_dict = {
#     'first name': 'James',
#     'last name': 'Bond',
#     'movies': ['Goldfinger (1964)', 'You Only Live Twice']
#     }
# b_dict = copy.deepcopy(a_dict)
# print('Memory chunks:', id(a_dict), id(b_dict))
# print('Same memory chunk?', a_dict is b_dict)
# print("Let's modify the movies list")
# a_dict['movies'].append('Diamonds Are Forever (1971)')
# print('a_dict movies:', a_dict['movies'])
# print('b_dict movies:', b_dict['movies'])

################################
# Sección 4.1.1.11
################################

# # El constructor solo se invoca una vez!!!

# import copy

# class Example:
#     def __init__(self):
#         self.properties = ["112", "997"]
#         print("Hello from __init__()")

# a_example = Example()
# b_example = copy.deepcopy(a_example)
# print("Memory chunks:", id(a_example), id(b_example))
# print("Same memory chunk?", a_example is b_example)
# print()
# print("Let's modify the movies list")
# b_example.properties.append("911")
# print('a_example.properties:', a_example.properties)
# print('b_example.properties:', b_example.properties)

###################################
# Laboratorio de Sección 4.1.1.12
###################################

# import copy

# warehouse = list()
# warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
# warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
# warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
# warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
# warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

# new_warehouse = copy.deepcopy(warehouse)
# for item in new_warehouse:
#     if item['weight'] > 300:
#         item['price'] *= 0.8

# print('*'*20)
# print('Source list of candies')
# for item in warehouse:
#     print(item)

# print('*'*20)
# print('Price proposal')
# for item in new_warehouse:
#     print(item)

###################################
# Laboratorio de Sección 4.1.1.13
###################################

# import copy


# class Delicacy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

#     def __str__(self):
#         return 'item:{}, price:{}, total weight: {}'.format(
#             self.name, self.price, self.weight
#             )

# warehouse = list()

# warehouse.append(Delicacy('Lolly Pop', 0.4, 133))
# warehouse.append(Delicacy('Licorice', 0.1, 251))
# warehouse.append(Delicacy('Chocolate', 1, 601))
# warehouse.append(Delicacy('Sours', 0.01, 513))
# warehouse.append(Delicacy('Hard candies', 0.3, 433))

# new_warehouse = copy.deepcopy(warehouse)
# for item in new_warehouse:
#     if item.weight > 300:
#         item.price *= 0.8

# print('*' * 20)
# print('Source list of candies')
# for item in warehouse:
#     print(item)

# print('*' * 20)
# print('Price proposal')
# for item in new_warehouse:
#     print(item)

# # Check that the line:
# # new_warehouse = copy.deepcopy(warehouse)
# # is exchanged with the following line:
# # new_warehouse = copy.copy(warehouse)

################################
# Sección 4.2.1.2
################################

## Serialización

# import pickle

# a_dict = dict()
# a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
# a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
# a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
# a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

# a_list = ['a', 123, [10, 100, 1000]]

# with open('multidata.pckl', 'wb') as file_out:
#     pickle.dump(a_dict, file_out)
#     pickle.dump(a_list, file_out)

################################
# Sección 4.2.1.3
################################

## Deserialización

# import pickle

# with open('multidata.pckl', 'rb') as file_in:
#     data1 = pickle.load(file_in)
#     data2 = pickle.load(file_in)

# print(type(data1))
# print(data1)
# print(type(data2))
# print(data2)

################################
# Sección 4.2.1.4
################################

# import pickle

# a_list = ['a', 123, [10, 100, 1000]]
# bytes = pickle.dumps(a_list)
# print('Intermediate object type, used to preserve data:', type(bytes))

# # now pass 'bytes' to appropriate driver

# # therefore when you receive a bytes object from an appropriate driver you can deserialize it
# b_list = pickle.loads(bytes)
# print('A type of deserialized object:', type(b_list))
# print('Contents:', b_list)

# Serialización sin ficheros

# import pickle

# object = 'Hola buenos días'
# serialized_object = pickle.dumps(object)                    # serialización

# print(serialized_object)

# deserialized_object = pickle.loads(serialized_object)       # deserialización

# print(deserialized_object)

################################
# Sección 4.2.1.6
################################

# import pickle

# def f1():
#     print('Hello from the jar!')

# with open('function.pckl', 'wb') as file_out:
#     pickle.dump(f1, file_out)

# import pickle

# with open('function.pckl', 'rb') as file_in:
#     data = pickle.load(file_in)

# print(type(data))
# print(data)
# data()

###########################
# import pickle

# def mi_funcion(mensaje):
#     print('Mensaje recibido en mi_funcion:',mensaje)
# ########################
# class MiClase:
#     def __init__(self,mensaje):
#         self.__mensaje = mensaje
#     def get_mensaje(self):
#         return self.__mensaje
# ########################

# # Solo se serializa la referencia a la función
# with open('function.pckl', 'wb') as fichero_salida:
#     pickle.dump(mi_funcion, fichero_salida)    

# with open('function.pckl', 'rb') as fichero_entrada:
#     data = pickle.load(fichero_entrada)

# print(type(data))
# print(data)
# data('Buenos días')

# ########################

# # Solo se serializa la referencia a la clase
# with open('function.pckl', 'wb') as fichero_salida:
#     pickle.dump(MiClase, fichero_salida)    

# with open('function.pckl', 'rb') as fichero_entrada:
#     clase = pickle.load(fichero_entrada)

# print(type(clase))
# print(clase)
# objeto = clase('Buenos días')
# print(objeto.get_mensaje())

################################
# Sección 4.2.1.7
################################

# import pickle

# class Cucumber:
#     def __init__(self):
#         self.size = 'small'

#     def get_size(self):
#         return self.size

# cucu = Cucumber()

# with open('cucumber.pckl', 'wb') as file_out:
#     pickle.dump(cucu, file_out)

# import pickle

# with open('cucumber.pckl', 'rb') as file_in:
#     data = pickle.load(file_in)

# print(type(data))
# print(data)
# print(data.size)
# print(data.get_size())

################################
## Serialización sin ficheros

# import pickle

# object = 'Hola buenos días'
# serialized_object = pickle.dumps(object)                    # serialización

# print(serialized_object)

# deserialized_object = pickle.loads(serialized_object)       # deserialización

# print(deserialized_object)

################################
# Sección 4.3.1.2
################################

# import shelve

# shelve_name = 'first_shelve.shlv'

# my_shelve = shelve.open(shelve_name, flag='c')
# my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
# my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
# my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
# my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
# my_shelve.close()

# new_shelve = shelve.open(shelve_name)
# print(new_shelve['USD'])
# new_shelve.close()

#################################3

## Laboratorio adicional

# import pickle

# class Cliente:
#     contador = 100
#     def __init__(self, nombre):
#         Cliente.contador += 1
#         self.id = Cliente.contador
#         self.nombre = nombre
#         self.lista_pedidos = []
        
#     def add_pedido(self, pedido):
#         self.lista_pedidos.append(pedido)
        
#     def __str__(self):
#         resultado = '\nCliente ' + str(self.id) + ' - ' + self.nombre + ':\n' + 'Lista de pedidos: \n' 
#         for elemento in self.lista_pedidos:
#             resultado += '\n\t' + elemento.__str__()
            
#         return resultado 


# class Pedido:
#     contador = 1000
#     def __init__(self, producto, cantidad, precio_unitario):
#         Pedido.contador += 1 
#         self.id = Pedido.contador
#         self.producto = producto
#         self.cantidad = cantidad
#         self.precio_unitario = precio_unitario
        
#     def __str__(self):
#         return 'Id pedido: ' + str(self.id) + ' - Producto: ' + self.producto + ' - Cantidad: ' + str(self.cantidad)  + ' - Precio unitario: ' + str(self.precio_unitario) + ' €'


#################

# cliente1 = Cliente('César Martín')
# cliente1.add_pedido(Pedido('Smart TV', 3, 599))
# cliente1.add_pedido(Pedido('Smart Phone', 1, 1200))
# cliente1.add_pedido(Pedido('Auriculares', 2, 45))

# print(cliente1)

###########################
## Serializando con pickle
###########################


# print('serializando con pickle:\n')

# with open('clientes.pckl', 'wb') as fichero:
#     pickle.dump(cliente1, fichero)

# print('deserializando con pickle:\n')

# with open('clientes.pckl', 'rb') as fichero:
#     nuevo_objeto_cliente = pickle.load(fichero)

# print(type(nuevo_objeto_cliente))
# print(nuevo_objeto_cliente)

###########################
## Serializando con shelve
###########################

# print('\nPruebas con shelve:\n')
# ## Creando un segundo cliente

# cliente2 = Cliente('Marta Gómez')
# cliente2.add_pedido(Pedido('Altavoces', 1, 299))
# cliente2.add_pedido(Pedido('Cámara de video', 1, 1755))
# cliente2.add_pedido(Pedido('Memoria USB', 2, 25))

# print(cliente2)

# import shelve

# nombre_shelve = 'clientes.shlv'

# mi_shelve = shelve.open(nombre_shelve, flag='c')
# mi_shelve['CESAR_MARTIN'] = cliente1
# mi_shelve['MARTA_GOMEZ'] = cliente2
# mi_shelve.close()

# nuevo_shelve = shelve.open(nombre_shelve)
# print(nuevo_shelve['CESAR_MARTIN'])
# print(nuevo_shelve['MARTA_GOMEZ'])
# nuevo_shelve.close()