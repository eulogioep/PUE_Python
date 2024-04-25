############ Métodos Mágicos #############

# class Person:
#     def __init__(self, weight, age, salary):
#         self.weight = weight
#         self.age = age
#         self.salary = salary

#     def __add__(self, other): # Método Mágico que Python invoca automáticamente.
#         return self.weight + other.weight


# p1 = Person(30, 40, 50)
# p2 = Person(35, 45, 55)

# print(p1 + p2)

######

# class Person:
#     def __init__(self, weight, age, salary):
#         self.weight = weight
#         self.age = age
#         self.salary = salary

#     def __add__(self, other):

#         # if isinstance(other, int):
#         #     return self.weight + other
        
#         return Person(self.weight + other.weight, -1, -1)

# p1 = Person(30, 40, 50)
# p2 = Person(35, 45, 55)
# p3 = Person(75, 45, 75)

# print((p1 + p2 + p3).weight)

#####

# class Person:
#     def __init__(self, weight, age, salary):
#         self.weight = weight
#         self.age = age
#         self.salary = salary

#     def __add__(self, other):

#         if isinstance(other, int):
#             return self.weight + other
        
#         return self.weight + other.weight

# p1 = Person(30, 40, 50)
# p2 = Person(35, 45, 55)
# p3 = Person(75, 45, 75)

# print(p1 + (p2 + p3))

######################################

# class MagicClass:
#     def __init__(self, valor):
#         self.valor = valor

#     def __repr__(self):
#         return 'Método __repr__() en MagicClass con valor ' + str(self.valor) 

#     def __str__(self):
#         return 'Método __str__ en MagicClass con valor ' + str(self.valor)

#     def __add__(self, otro):
#         print('Método __add__ en MagicClass')
#         return self.valor + otro.valor

#     def __sub__(self, otro):
#         print('Método __sub__ en MagicClass')
#         return self.valor - otro.valor

#     def __mul__(self, otro):
#         print('Método __mul__ en MagicClass')
#         return self.valor * otro.valor

#     def __truediv__(self, otro):
#         print('Método __truediv__ en MagicClass')
#         return self.valor / otro.valor

#     def __floordiv__(self, otro):
#         print('Método __floordiv__ en MagicClass')
#         return self.valor // otro.valor
#     def __mod__(self, otro):
#         print('Método __mod__ en MagicClass')
#         return self.valor % otro.valor

#     def __pow__(self, otro):
#         print('Método __pow__ en MagicClass')
#         return self.valor ** otro.valor

#     def __eq__(self, otro):
#         print('Método __eq__ en MagicClass')
#         return self.valor == otro.valor

#     def __ne__(self, otro):
#         print('Método __ne__ en MagicClass')
#         return self.valor != otro.valor

#     def __lt__(self, otro):
#         print('Método __lt__ en MagicClass')
#         return self.valor < otro.valor

#     def __le__(self, otro):
#         print('Método __le__ en MagicClass')
#         return self.valor <= otro.valor

#     def __gt__(self, otro):
#         print('Método __gt__ en MagicClass')
#         return self.valor > otro.valor

#     def __ge__(self, otro):
#         print('Método __ge__ en MagicClass')
#         return self.valor >= otro.valor

#     def __len__(self):
#         print('Método __len__ en MagicClass')
#         return len(self.valor)
    
#     def __getitem__(self, key):
#         print('Método __getitem__ en MagicClass')
#         return self.valor[key]

#     def __setitem__(self, key, valor):
#         print('Método __setitem__ en MagicClass')
#         self.valor[key] = valor

#     def __delitem__(self, key):
#         print('Método __delitem__ en MagicClass')
#         del self.valor[key]

#     def __iter__(self):
#         print('Método __iter__ en MagicClass')
#         return iter(self.valor)

#     def __contains__(self, item):
#         print('Método __contains__ en MagicClass')
#         return item in self.valor

#     def __call__(self, *args, **kwargs):
#         print('Método __call__ en MagicClass invocado con argumentos args =', args, '- kwargs=', kwargs)

#     def __enter__(self):
#         print('Método __enter__ en MagicClass')
#         return self

#     def __exit__(self, exc_type, exc_valor, traceback):
#         print('Método __exit__ en MagicClass')


# o1 = MagicClass({})

# o1['clave1'] = 'valor'

####################################

# class TimeInterval:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __add_sub(self, other, operation_type):
#         own = self.hours * 3600 + self.minutes * 60 + self.seconds
#         another = other.hours * 3600 + other.minutes * 60 + other.seconds

#         if operation_type == 'subtraction':
#             new_time = own - another
#         elif operation_type == 'addition':
#             new_time = own + another
#         else:
#             raise Exception('Unknown operation')

#         new_hours = new_time // 3600
#         new_minutes = (new_time % 3600) // 60
#         new_seconds = new_time % 60

#         return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

#     def __add__(self, other):
#         if isinstance(other, TimeInterval):
#             return self.__add_sub(other, 'addition')
#         else:
#             raise TypeError('can only add TimeInterval objects')

#     def __sub__(self, other):
#         if isinstance(other, TimeInterval):
#             return self.__add_sub(other, 'subtraction')
#         else:
#             raise TypeError('can only subtract TimeInterval objects')

#     def __mul__(self, other):
#         if isinstance(other, int):
#             new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
#             new_hours = new_time // 3600
#             new_minutes = (new_time % 3600) // 60
#             new_seconds = new_time % 60
#             return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
#         else:
#             raise TypeError('can only multiply TimeInterval objects by integers')

#     def __str__(self):
#         return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
# t1 = TimeInterval(hours=21, minutes=58, seconds=50)
# t2 = TimeInterval(1, 45, 22)

# assert str(t1 + t2) == '23:44:12'
# assert str(t1 - t2) == '20:13:28'
# assert str(t1 * 2) == '43:57:40'

# print('It works like a charm')


# ######

# class TimeInterval:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __add_sub(self, other, operation_type):
#         own = self.hours * 3600 + self.minutes * 60 + self.seconds
#         another = other.hours * 3600 + other.minutes * 60 + other.seconds

#         if operation_type == 'subtraction':
#             new_time = own - another
#         elif operation_type == 'addition':
#             new_time = own + another
#         else:
#             raise Exception('Unknown operation')

#         new_hours = new_time // 3600
#         new_minutes = (new_time % 3600) // 60
#         new_seconds = new_time % 60

#         return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

#     def __add__(self, other):
#         if isinstance(other, TimeInterval):
#             return self.__add_sub(other, 'addition')
#         elif isinstance(other, int):
#             return self.__add_sub(TimeInterval(seconds=other), 'addition')
#         else:
#             raise TypeError('can only add TimeInterval or integer objects')

#     def __sub__(self, other):
#         if isinstance(other, TimeInterval):
#             return self.__add_sub(other, 'subtraction')
#         elif isinstance(other, int):
#             return self.__add_sub(TimeInterval(seconds=other), 'subtraction')
#         else:
#             raise TypeError('can only subtract TimeInterval objects')

#     def __mul__(self, other):
#         if isinstance(other, int):
#             new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
#             new_hours = new_time // 3600
#             new_minutes = (new_time % 3600) // 60
#             new_seconds = new_time % 60
#             return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
#         else:
#             raise TypeError('can only multiply TimeInterval objects by integers')

#     def __str__(self):
#         return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
# t1 = TimeInterval(hours=21, minutes=58, seconds=50)
# t2 = TimeInterval(1, 45, 22)

# assert str(t1 + t2) == '23:44:12'
# assert str(t1 - t2) == '20:13:28'
# assert str(t1 * 2) == '43:57:40'
# assert str(t1 + 62) == '21:59:52'
# assert str(t1 - 62) == '21:57:48'

# print('It works like a charm')


##########################################################

# class A:
#     def info(self):
#         print('Class A')

# class B(A):
#     def info(self):
#         print('Class B')

# class C(A):
#     def info(self):
#         print('Class C')

# class D(B, C):
#     pass

# D().info()


##################################

# class Scanner():
#     def scan(self):
#         print("\tscan() method from Scanner class")

# class Fax():
#     def send(self):
#         print("\tsend() method from Fax class")

#     def print(self):
#         print("\tprint method from Fax class")

# class Printer():
#     def print(self):
#         print("\tprint method from Printer class")

# class MFD_SFP(Scanner, Fax, Printer):
#     pass

# class MFD_SPF(Scanner, Printer, Fax):
#     pass

# print('Creating device following the order: Scanner, Fax, Printer')
# mfd_sfp = MFD_SFP()
# print('Device capabilities:')
# mfd_sfp.scan()
# mfd_sfp.print()
# mfd_sfp.send()

# print()
# print('Creating device following the order: Scanner, Printer, Fax')
# mfd_spf = MFD_SPF()
# print('Device capabilities:')
# mfd_spf.scan()
# mfd_spf.print()
# mfd_spf.send()


############## Polimorfismo ##################

# class Device:
#     def turn_on(self):
#         print('The device was turned on')

# class Radio(Device):
#     pass

# class PortableRadio(Device):
#     def turn_on(self):
#         print('PortableRadio type object was turned on')

# class TvSet(Device):
#     def turn_on(self):
#         print('TvSet type object was turned on')

# device = Device()
# radio = Radio()
# portableRadio = PortableRadio()
# tvset = TvSet()

# for element in (device, radio, portableRadio, tvset):
#     element.turn_on()

#########

# class Wax:
#     def melt(self):
#         print("Wax can be used to form a tool")

# class Cheese:
#     def melt(self):
#         print("Cheese can be eaten")

# class Wood:
#     def fire(self):
#         print("A fire has been started!")

# for element in Wax(), Cheese(), Wood():
#     try:
#         element.melt()
#     except AttributeError:
#         print('No melt() method')
        


##########################

# def combiner(a, b, *args, **kwargs):
#     print(a, type(a))
#     print(b, type(b))
#     print(args, type(args))
#     print(kwargs, type(kwargs))


# combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


####### Decoradores #################

# def simple_hello():
#     print("Hello from simple function!")


# ######

# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function


# ######

# decorated = simple_decorator(simple_hello)
# decorated()

#####

# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function


# @simple_decorator
# def simple_hello():
#     print("Hello from simple function!")


# simple_hello()

#######

# def simple_decorator(own_function):

#     def internal_wrapper(*args, **kwargs):
#         print('"{}" was called with the following arguments'.format(own_function.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         own_function(*args, **kwargs)
#         print('Decorator is still operating')

#     return internal_wrapper


# @simple_decorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)

# combiner('a', 'b', exec='yes')

####################

# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper


# @warehouse_decorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)


# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)


# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)


# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


######

# def big_container(collective_material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             our_function(*args)
#             print('<strong>*</strong> The whole order would be packed with', collective_material)
#             print()
#         return internal_wrapper
#     return wrapper

# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             our_function(*args)
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#         return internal_wrapper
#     return wrapper

# @big_container('plain cardboard')
# @warehouse_decorator('bubble foil')
# def pack_books(*args):
#     print("We'll pack books:", args)

# @big_container('colourful cardboard')
# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# @big_container('strong cardboard')
# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)


# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


######## Laboratorio ############################

# from datetime import datetime

# def time_stamping_machine(own_function):
#     def internal_wrapper(*args, **kwargs):
#         timestamp = datetime.now()
#         string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         print()
#         print(string_timestamp)
#         return own_function(*args, **kwargs)
#     return internal_wrapper

# @time_stamping_machine
# def simple_hello():
#     print("Hello from simple function!")

# @time_stamping_machine
# def add_two_objects(n1, n2):
#     return n1 + n2

# @time_stamping_machine
# def multiply_two_objects(n1, n2):
#     return n1 * n2

# simple_hello()
# print('Result:', add_two_objects('Hello', 'Python'))
# print('Result:', add_two_objects(100, 88))
# print('Result:', multiply_two_objects(100, 88))



####### Decoradores con clases ###################################

# class SimpleDecorator:
#     def __init__(self, own_function):
#         self.func = own_function

#     def __call__(self, *args, **kwargs):
#         print('"{}" was called with the following arguments'.format(self.func.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         self.func(*args, **kwargs)
#         print('Decorator is still operating')


# @SimpleDecorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)


# combiner('a', 'b', exec='yes')


####### Decorador con argumentos #######################################

# class WarehouseDecorator:
#     def __init__(self, material):
#         self.material = material

#     def __call__(self, own_function):
#         def internal_wrapper(*args, **kwargs):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
#             own_function(*args, **kwargs)
#             print()
#         return internal_wrapper


# @WarehouseDecorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)


# @WarehouseDecorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)


# @WarehouseDecorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)


# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


######################################################

# class Parent:

#     estatica = "Parent"

#     @classmethod
#     def class_method(cls):
#         print(cls.estatica)

#     # @staticmethod
#     # def static_method():
#     #     print(Parent.estatica)

# class Child(Parent):
#     estatica = "Child"

# # Accessing the inherited class method from the Child class
# Child.class_method()

############ Laboratorio Clases Abstractas #####################################

# import abc

# class Scanner(abc.ABC):
#     def scan_document(self):
#         return 'Document was scanned'

#     @abc.abstractmethod
#     def get_scanner_status(self):
#         pass

# class Printer(abc.ABC):
#     def print_document(self):
#         return 'Document was printed'

#     @abc.abstractmethod
#     def get_printer_status(self):
#         pass

# class MFD1(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is low, S/N: S001'

#     def get_printer_status(self):
#         return 'Max print resolution is low, S/N: P001'

# class MFD2(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is fine, S/N: S002'

#     def get_printer_status(self):
#         return 'Max print resolution is fine, S/N: P002'

#     def get_history(self):
#         return 'The history is...'

# class MFD3(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is high, S/N: S003'

#     def get_printer_status(self):
#         return 'Max print resolution is high, S/N: P003'

#     def get_history(self):
#         return 'The history is...'

#     def send_fax(self):
#         print('sending fax')

#     def receive_fax(self):
#         print('receiving fax')
# mfd1 = MFD1()
# print(mfd1.print_document())
# print(mfd1.get_printer_status())

# mfd2 = MFD2()
# print(mfd2.print_document())
# print(mfd2.get_printer_status())

# mfd3 = MFD3()
# print(mfd3.print_document())
# print(mfd3.get_printer_status())


###### Laboratorio Decoradores ######################################

# from datetime import datetime

# def time_stamping_machine(own_function):
#     def internal_wrapper(*args, **kwargs):
#         timestamp = datetime.now()
#         string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         print()
#         print(string_timestamp)
#         return own_function(*args, **kwargs)
#     return internal_wrapper

# @time_stamping_machine
# def simple_hello():
#     print("Hello from simple function!")

# @time_stamping_machine
# def add_two_objects(n1, n2):
#     return n1 + n2

# @time_stamping_machine
# def multiply_two_objects(n1, n2):
#     return n1 * n2

# simple_hello()
# print('Result:', add_two_objects('Hello', 'Python'))
# print('Result:', add_two_objects(100, 88))
# print('Result:', multiply_two_objects(100, 88))


#######################################################

# # importando librerías
# import time
# import math
# import random

# # decorador para calcular el tiempo de ejecución de cualquier función
# def calcular_tiempo(func):
#     def medir(*args, **kwargs):
	
#           # calculando el tiempo antes de ejecutar la función
#           inicio = time.time()
          
#           # pausar la ejecución un cierto número de segundos para simular una función más lenta
#           # así podremos ver mejor la diferencia de tiempo
#           time.sleep(random.randint(1,10))
          
#           func(*args, **kwargs)

# 		  # calculando el tiempo después de ejecutar la función
#           final = time.time()
#           print("Tiempo de ejecución de la función", func.__name__,":", round(final - inicio,3), "milisegundos")

#     return medir

# # el decorador puede añadirse a cualquier función,
# # en éste caso para calcular el factorial

# @calcular_tiempo
# def factorial(num):

#  	print(math.factorial(num))

# # llamando a la función
# factorial(1000)

#########################################################################

# class RelojDeLujo:
#     relojes_creados = 0

#     def __init__(self):
#         RelojDeLujo.relojes_creados += 1

#     @classmethod
#     def recuperar_numero_relojes_creados(cls):
#         return cls.relojes_creados

#     @classmethod
#     def con_grabado(cls, texto):
#         if RelojDeLujo.validar_texto(texto):
#             _reloj = cls()
#             _reloj.texto = texto
#             return _reloj
#         else:
#             raise Exception('"' + texto + '" - No cumple con la regla de letras y números')

#     @staticmethod
#     def validar_texto(texto):
#         if len(texto) > 40:
#             return False
#         if not texto.isalpha():
#             return False
#         return True
# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())
# w1 = RelojDeLujo()
# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())
# w2 = RelojDeLujo.con_grabado('Alabama')
# print('Creado reloj con grabado "Alabama", el total ahora es de', RelojDeLujo.recuperar_numero_relojes_creados())

# try:
#     w3 = RelojDeLujo.con_grabado('foo@foo.com')
# except Exception as e:
#     print('El problema es que el texto ', e)

# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())

##################################################

# class RelojDeLujo:
#     __relojes_creados = 0

#     def __init__(self):
#         RelojDeLujo.__relojes_creados += 1

#     @classmethod
#     def recuperar_numero_relojes_creados(cls):
#         return cls.__relojes_creados

#     @classmethod
#     def con_grabado(cls, texto):
#         if cls.validar_texto(texto):
#             _reloj = cls()
#             _reloj.texto = texto
#             return _reloj
#         else:
#             raise Exception('"' + texto + '" - No cumple con la regla de letras y números')

#     @staticmethod
#     def validar_texto(texto):
#         if len(texto) > 40:
#             return False
#         if not texto.isalpha():
#             return False
#         return True
# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())
# w1 = RelojDeLujo()
# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())
# w2 = RelojDeLujo.con_grabado('Alabama')
# print('Creado reloj con grabado "Alabama", el total ahora es de', RelojDeLujo.recuperar_numero_relojes_creados())

# try:
#     w3 = RelojDeLujo.con_grabado('foo@foo.com')
# except Exception as e:
#     print('El problema es que el texto ', e)

# print('Relojes creados hasta ahora:', RelojDeLujo.recuperar_numero_relojes_creados())

#####################################################

# import abc

# class Scanner(abc.ABC):
#     def scan_document(self):
#         return 'Document was scanned'

#     @abc.abstractmethod
#     def get_scanner_status(self):
#         pass

# class Printer(abc.ABC):
#     def print_document(self):
#         return 'Document was printed'

#     @abc.abstractmethod
#     def get_printer_status(self):
#         pass
# class MFD1(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is low, S/N: S001'

#     def get_printer_status(self):
#         return 'Max print resolution is low, S/N: P001'

# class MFD2(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is fine, S/N: S002'

#     def get_printer_status(self):
#         return 'Max print resolution is fine, S/N: P002'

#     def get_history(self):
#         return 'The history is...'

# class MFD3(Scanner, Printer):
#     def get_scanner_status(self):
#         return 'Max scan resolution is high, S/N: S003'

#     def get_printer_status(self):
#         return 'Max print resolution is high, S/N: P003'

#     def get_history(self):
#         return 'The history is...'

#     def send_fax(self):
#         print('sending fax')

#     def receive_fax(self):
#         print('receiving fax')
# mfd1 = MFD1()
# print(mfd1.print_document())
# print(mfd1.get_printer_status())

# mfd2 = MFD2()
# print(mfd2.print_document())
# print(mfd2.get_printer_status())

# mfd3 = MFD3()
# print(mfd3.print_document())
# print(mfd3.get_printer_status())
# class Clase:
#     __numero = 127


# instancia = Clase()

# # print(instancia.__numero)

# # Name Mangling
# print(instancia._Clase__numero)

########################################################

# import random

# class IBANValidationError(Exception):
#     pass

# class IBANDict(dict):
#     def __setitem__(self, _key, _val):
#         if IBANDict.validateIBAN(_key):
#             super().__setitem__(_key, _val)

#     def update(self, *args, **kwargs):
#         for _key, _val in dict(*args, **kwargs).items():
#             self.__setitem__(_key, _val)

#     @staticmethod
#     def validateIBAN(iban):
#         iban = iban.replace(' ', '')

#         if not iban.isalnum():
#             raise IBANValidationError("You have entered invalid characters.")

#         elif len(iban) < 15:
#             raise IBANValidationError("IBAN entered is too short.")
#         elif len(iban) > 31:
#             raise IBANValidationError("IBAN entered is too long.")

#         else:
#             iban = (iban[4:] + iban[0:4]).upper()
#             iban2 = ''
#             for ch in iban:
#                 if ch.isdigit():
#                     iban2 += ch
#                 else:
#                     iban2 += str(10 + ord(ch) - ord('A'))
#             ibann = int(iban2)

#             if ibann % 97 != 1:
#                 raise IBANValidationError("IBAN entered is invalid.")

#             return True
# my_dict = IBANDict()
# keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

# for key in keys:
#     my_dict[key] = random.randint(0, 1000)

# print('The my_dict dictionary contains:')
# for key, value in my_dict.items():
#     print("\t{} -> {}".format(key, value))

# try:
#     my_dict.update({'dummy_account': 100})
# except IBANValidationError:
#     print('IBANDict has protected your dictionary against incorrect data insertion')
    
##########################################

# class RocketNotReadyError(Exception):
#     pass

# def personnel_check():
#     try:
#         print("\tThe captain's name is", crew[0])
#         print("\tThe pilot's name is", crew[1])
#         print("\tThe mechanic's name is", crew[2])
#         print("\tThe navigator's name is", crew[3])

#     except IndexError as alias:
#         raise RocketNotReadyError('Crew is incomplete') from alias

########################################################

# crew = ['John', 'Mary', 'Mike']
# print('Final check procedure')

# try:

#     personnel_check()

# except RocketNotReadyError as e:

#     crew.append("Cesar")
#     personnel_check()


####################################################


