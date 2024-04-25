################################
# Sección 2.1.1.3
################################

# number = 10
# print(number + 20)

# number = 10
# print(number.__add__(20))

################################
# Sección 2.1.1.4
################################

# class Person:
#     def __init__(self, weight, age, salary):
#         self.weight = weight
#         self.age = age
#         self.salary = salary

#     def __add__(self, other):
#         return self.weight + other.weight


# p1 = Person(30, 40, 50)
# p2 = Person(35, 45, 55)

# print('Peso total para el elevador:', p1 + p2)

################################
# Sección 2.1.1.5
################################

# class Person:
#     def __init__(self, weight, age, salary):
#         self.weight = weight
#         self.age = age
#         self.salary = salary

#     def __add__(self, other):
#         return self.weight + other.weight


# p1 = Person(30, 40, 50)
# p2 = Person(35, 45, 55)

# print('Peso total para el elevador:', p1 + p2)

################################
# Sección 2.1.1.6
################################

# print(dir(10))

# help(10)

################################
# Secciones 2.1.1.7 - 2.2.1.8
################################

##########################
# Comparison methods
##########################

# Function or operator    Magic method	              Implementation meaning or purpose
# --------------------    -------------------         ----------------------------------
#         ==              __eq__(self, other)	      equality operator
#         !=              __ne__(self, other)	      inequality operator
#         <	              __lt__(self, other)	      less-than operator
#         >	              __gt__(self, other)	      greater-than operator
#         <=	              __le__(self, other)	      less-than-or-equal-to operator
#         >=	              __ge__(self, other)	      greater-than-or-equal-to operator


################################
# Numeric methods
############################################
# Unary operators and functions
############################################

# Function or operator	  Magic method	              Implementation meaning or purpose
# --------------------    ------------                --------------------------------------------
#         +	              __pos__(self)               unary positive, like a = +b
#         -	              __neg__(self)	              unary negative, like a = -b
#         abs()	          __abs__(self)	              behavior for abs() function
#         round(a, b)	  __round__(self, b)	          behavior for round() function

############################################
# Common, binary operators and functions
############################################

# Function or operator	  Magic method	              Implementation meaning or purpose
# --------------------    ------------                --------------------------------------------
#         +	              __add__(self, other)	      addition operator
#         -	              __sub__(self, other)	      subtraction operator
#         *	              __mul__(self, other)	      multiplication operator
#         //              __floordiv__(self, other)	  integer division operator
#         /	              __div__(self, other)	      division operator
#         %	              __mod__(self, other)	      modulo operator
#         **	          __pow__(self, other)	      exponential (power) operator

############################################
# Augumented operators and functions
############################################

# By augumented assignment we should understand a sequence of unary operators and assignments like a += 20

# Function or operator	  Magic method	              Implementation meaning or purpose
# --------------------    ------------                --------------------------------------------
#         +=              __iadd__(self, other)	      addition and assignment operator
#         -=	          __isub__(self, other)	      subtraction and assignment operator
#         *=	          __imul__(self, other)	      multiplication and assignment operator
#         //=	          __ifloordiv__(self, other)  integer division and assignment operator
#         /=              __idiv__(self, other)	      division and assignment operator
#         %=	          __imod__(self, other)	      modulo and assignment operator
#         **=	          __ipow__(self, other)	      exponential (power) and assignment operator

############################################
# Type conversion methods
############################################

# Python offers a set of methods responsible for the conversion of built-in data types.

# Function or operator	  Magic method	              Implementation meaning or purpose
# --------------------    ---------------             --------------------------------------------
#         int()	          __int__(self)	              conversion to integer type
#         float()	      __float__(self)	          conversion to float type
#         oct()	          __oct__(self)	              conversion to string, containing an octal representation
#         hex()	          __hex__(self)	              conversion to string, containing a hexadecimal representation

############################################
# Object introspection
############################################

# Python offers a set of methods responsible for representing object details using ordinary strings.

# Function or operator	  Magic method	              Implementation meaning or purpose
# --------------------    ------------                --------------------------------------------
#         str()	          __str__(self)	              responsible for handling str() function calls
#         repr()	          __repr__(self)	              responsible for handling repr() function calls
#         format()	      __format__(self, formatstr) called when new-style string formatting is applied to an object
#         hash()          __hash__(self)	              responsible for handling hash() function calls
#         dir()	          __dir__(self)	              responsible for handling dir() function calls
#         bool()	          __nonzero__(self)	          responsible for handling bool() function calls

############################################
# Object retrospection
############################################

# Following the topic of object introspection, there are methods responsible for object reflection.

# Function or operator	            Magic method	                        Implementation meaning or purpose
# --------------------------        ------------ --------------------   --------------------------------------------
#    isinstance(object, class)	    __instancecheck__(self, object)	    responsible for handling isinstance() function calls
#    issubclass(subclass, class)	__subclasscheck__(self, subclass)	responsible for handling issubclass() function calls

############################################
# Object attribute access
############################################

# Access to object attributes can be controlled via the following magic methods
  
# Expression example	                Magic method                      	 Implementation meaning or purpose
# ---------------------------       -----------------------------------  -----------------------------------------------
#    object.attribute	            __getattr__(self, attribute)	         responsible for handling access to a non-existing attribute
#    object.attribute	            __getattribute__(self, attribute)	 responsible for handling access to an existing attribute
#    object.attribute = value	    __setattr__(self, attribute, value)	 responsible for setting an attribute value
#    del object.attribute	        __delattr__(self, attribute)	         responsible for deleting an attribute

############################################
# Methods allowing access to containers
############################################

# Containers are any object that holds an arbitrary number of other objects; containers provide a way to access the contained objects and to iterate over them. Container examples: list, dictionary, tuple, and set.

# Expression example	                Magic method                      	 Implementation meaning or purpose
# ---------------------------       -----------------------------------  -----------------------------------------------
#    len(container)	                __len__(self)	                     returns the length (number of elements) of the container
#    container[key]	                __getitem__(self, key)	             responsible for accessing (fetching) an element identified by the key argument
#    container[key] = value	        __setitem__(self, key, value)	     responsible for setting a value to an element identified by the key argument
#    del container[key]	            __delitem__(self, key)	             responsible for deleting an element identified by the key argument
#    for element in container	    __iter__(self)	                     returns an iterator for the container
#    item in container	            __contains__(self, item)	         responds to the question: does the container contain the selected item?

# The list of special methods built-in in Python contains more entities. For more information, refer to https://docs.python.org/3/reference/datamodel.html#special-method-names.

##################################

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

##################################
# Laboratorio de Sección 2.1.1.10
##################################

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
#             new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other # multiplicar en segundos
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
# assert str(t1 * 2)  == '43:57:40'

# print('Funciona perfectamente!')

##################################
# class IntervaloTiempo:
#     def __init__(self, horas, minutos, segundos) -> None:
#         self.horas = horas
#         self.minutos = minutos
#         self.segundos = segundos

#     def __formato(self, valor):
#         return '0'+str(valor) if len (str(valor)) ==1 else str(valor)
    
#     def __str__(self) -> str:
#         return self.__formato(self.horas) + ':' + self.__formato(self.minutos) + ':' + self.__formato(self.segundos)
    
#     def tiempo_a_segundos(self) -> int:
#         return self.horas*60*60 + self.minutos*60 + self.segundos
#     def tiempo_a_intervalo(self, t_segundos):
#         horas = t_segundos // (60*60)
#         minutos = (t_segundos - (horas * 60 *60)) // 60
#         segundos = t_segundos - (horas * 60 *60) - minutos*60
#         return IntervaloTiempo(horas, minutos, segundos)
#     def __add__(self, otro):
#         if isinstance(otro, IntervaloTiempo):
#             t1 = self.tiempo_a_segundos()
#             t2 = otro.tiempo_a_segundos()
#             return self.tiempo_a_intervalo(t1 + t2)
#         else:
#             raise ValueError   
#     def __sub__(self,otro):
#         if isinstance(otro, IntervaloTiempo):
#             t1 = self.tiempo_a_segundos()
#             t2 = otro.tiempo_a_segundos()
#             return self.tiempo_a_intervalo(t1 - t2)
#         else:
#              raise ValueError

# t_1 = IntervaloTiempo(2,30,40)
# t_2 = IntervaloTiempo(4,1,40)
# print(t_2 - t_1)


##################################
# Laboratorio de Sección 2.1.1.11
##################################

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
# assert str(t1 * 2)  == '43:57:40'
# assert str(t1 + 62) == '21:59:52'
# assert str(t1 - 62) == '21:57:48'

# print('Funciona perfectamente!')

###################
# Sección 2.2.1.3
###################

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

###################
# Sección 2.2.1.4
###################

# class A:
#     def info(self):
#         print('Class A')

# class B(A):
#     def info(self):
#         print('Class B')

# class C(A):
#     def info(self):
#         print('Class C')

# class D(A, C):
#     pass

# D().info()

###################
# Sección 2.2.1.5
###################

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

# class E(C, B):
#     pass

# D().info()
# E().info()

#################################
# Laboratorio de Sección 2.2.1.6
#################################

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

###################
# Sección 2.2.1.7
###################

# print(dir(1))
# print()
# print(dir('valor'))

# a = 10
# print(a.__add__(20))
# b = 'abc'
# print(b.__add__('def'))

###################
# Sección 2.2.1.8
###################

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

###################
# Sección 2.2.1.9
###################

# class Hierro:
#     def derretir(self):
#         print("El hierro se está fundiendo")

# class Queso:
#     def derretir(self):
#         print("El queso se está fundiendo")

# class Madera:
#     def quemar(self):
#         print("la madera se está quemando!")

# for elemento in Hierro(), Queso(), Madera():
#     try:
#         elemento.derretir()
#     except AttributeError:
#         print('El objeto',type(elemento).__name__,'no contiene un método derretir()')

###################
# Sección 2.3.1.1
###################

# print()
# print(3)
# print(1, 20, 10)
# print('--', '++')

###################

# a_list = list()
# b_list = list(10, 20, 43, 54, 23, 23, 34, 23, 2)

# print(a_list)
# print(b_list)

###################
# Sección 2.3.1.2
###################

# def combinador(a, b, *args, **kwargs):
#     print('Valor recibido:', a, ' - Tipo', type(a))
#     print('Valor recibido:', b, ' - Tipo', type(b))
#     print('Valor recibido en *args:', args, ' - Tipo', type(args))
#     print('Valor recibido en **kwargs:', kwargs, '- Tipo', type(kwargs))

# combinador(10, '20', 40, 60, 30, argumento1=50, argumento2='66')

###################
# Sección 2.3.1.3
###################

# def super_combinador(*my_args, **my_kwargs):
#     print('my_args:', my_args)
#     print('my_kwargs', my_kwargs)
    
# def combinador(a, b, *args, **kwargs):
#     super_combinador(*args, **kwargs)

# combinador(10, '20', 40, 60, 30, argumento1=50, argumento2='66')

###################
# Sección 2.3.1.4
###################

# def combinador(a, b, *args, **kwargs):
#     super_combinador(args, kwargs)  # cuidado con pasar los parámetros sin *!!!!!!!!!!!!!!!!!!

# def super_combinador(*my_args, **my_kwargs):
#     print('my_args:', my_args)
#     print('my_kwargs', my_kwargs)

# combinador(10, '20', 40, 60, 30, argumento1=50, argumento2='66')

###################
# Sección 2.3.1.5
###################

# def combinador(a, b, *args, c=20, **kwargs):
#     super_combinador(c, *args, **kwargs)
    
# def super_combinador(my_c, *my_args, **my_kwargs):
#     print('my_args:', my_args)
#     print('my_c:', my_c)
#     print('my_kwargs', my_kwargs)

# combinador(1, '1', 1, 1, c=2, argumento1=1, argumento2='1')

###################
# Sección 2.4.1.2
###################

# def simple_hello():
#     print("Hello from simple function!")
    
# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function

# ##########

# decorated = simple_decorator(simple_hello)
# decorated()

# ## Equivalente

# simple_decorator(simple_hello)()

###################
# Sección 2.4.1.3
###################

# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function


# @simple_decorator
# def simple_hello():
#     print("Hello from simple function!")


# simple_hello()

###################
# Sección 2.4.1.4
###################

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

###################
# Sección 2.4.1.5
###################

# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('Wrapping items from {} with {}'.format(our_function.__name__, material))
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

###################
# Sección 2.4.1.6
###################

# def big_container(collective_material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print(our_function)
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

# @big_container('plain cardboard')    # invoca a __init() en big_container()       -->  retorna el objeto big_container
#                                      # invoca a __wrapper() en big_container()    -->  retorna la función wrapper()
                                     
# @warehouse_decorator('bubble foil')  # invoca a __init() en warehouse_decorator() -->  retorna el objeto warehouse_decorator
#                                      # invoca a __wrapper() en big_container()    -->  retorna la función wrapper()
                                     
# def pack_books(*args):               # invoca a la función pack_books()           
#                                                 # -->  y ejecuta la función internal_wrapper() de big_container()
#                                                 # -->  con parámetro warehouse_decorator()
#                                                 # -->  que a su vez ejecuta la función internal_wrapper() de warehouse_decorator
#                                                 # -->  que finalmente ejecuta pack_toys()
#     print("We'll pack books:", args)


# pack_books('Alice in Wonderland', 'Winnie the Pooh')

#################################
# Laboratorio de Sección 2.4.1.7
#################################

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

################################################################
# conocer el tiempo de respuesta mediante un decorador
################################################################

# # importando librerías
# import time
# import math
# import random

# # decorador para calcular el tiempo de ejecución de cualquier función
# def calcular_tiempo(func):
 	
#  	# argumentos añadidos a la función 'medir'
#     # *args    --> número variable de argumentos posicionales
#     # **kwargs --> número variable de argumentos de palabras clave

#  	def medir(*args, **kwargs):
#           # calculando el tiempo antes de ejecutar la función
#           inicio = time.time()
          
#           # pausar la ejecución un cierto número de segundos para simular una función más lenta
#           # así podremos ver mejor la diferencia de tiempo
#           time.sleep(random.randint(1,10))
#           func(*args, **kwargs)
         
#           # calculando el tiempo después de ejecutar la función
#           final = time.time()
#           print("Tiempo de ejecución de la función", func.__name__,":", round(final - inicio,3), "milisegundos")

#  	return medir

# # el decorador puede añadirse a cualquier función,
# # en éste caso para calcular el factorial

# @calcular_tiempo
# def factorial(num):

#  	print(math.factorial(num))

# # llamando a la función
# factorial(10)

###################
# Sección 2.4.1.8
###################

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

############################################################
# Comparación entre decoradores como funciones y clases
############################################################
# class WarehouseDecorator:
#     def __init__(self, material):
#         self.material = material

#     def __call__(self, own_function):
#         def internal_wrapper(*args, **kwargs):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
#             own_function(*args, **kwargs)
#             print()
#         return internal_wrapper


# @WarehouseDecorator('kraft')                        # llamada a__init__()       --> retorna el objeto WarehourseDecorator
# def pack_books(*args):                              # llamada a __call__()      --> retorna internal_wrapper
#     print("We'll pack books:", args)

# pack_books('Alice in Wonderland', 'Winnie the Pooh') # invoca a internal_wrapper()    -->   que ejecuta pack_books()

# @WarehouseDecorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# pack_toys('doll', 'car')

# @WarehouseDecorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)

# pack_fruits('plum', 'pear')

##############################################

# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper


# @warehouse_decorator('kraft')                        # invoca a warehouse_decorator() -->   retorna wrapper()
# def pack_books(*args):                               # invoca a wrapper()             -->   retorna internal_wrapper()
#     print("We'll pack books:", args)

# pack_books('Alice in Wonderland', 'Winnie the Pooh') # invoca a internal_wrapper()    -->   que ejecuta pack_books()

# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)

# pack_toys('doll', 'car')

# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)

# pack_fruits('plum', 'pear')

###################
# Sección 2.4.1.9
###################

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

###################
# Sección 2.4.1.10
###################

# def decorador(A):
#     def wrapper():
#         print('Ejecutando decorador de clase')
#         return A
#     return wrapper

# class MiClase:
#     pass

# MiClase = decorador(MiClase())
# objeto = MiClase()

# print(type(objeto))

# ##################################
# def decorador(A):
#     def wrapper():
#         print('Ejecutando decorador de clase')
#         return A
#     return wrapper

# @decorador
# class MiClase:
#     pass

# objeto = MiClase()

# print(type(objeto))

###################
# Sección 2.4.1.11
###################

# class Coche:
#     def __init__(self, codigo_seguridad):
#         self.kilometrake = 0
#         self.codigo_seguridad = codigo_seguridad

# coche = Coche('ABC123')

# print('El kilometraje actual es de', coche.kilometrake, 'km')
# print('El código de seguridad es', coche.codigo_seguridad)

###################
# Sección 2.4.1.12
###################

# def contador_acceso(clase_):
#     clase_.__recuperar_atributo_original = clase_.__getattribute__

#     def nuevo_getattribute(self, nombre):
#         if nombre == 'kilometraje':
#             print('El atributo kilometraje ha sido leído')
#         return clase_.__recuperar_atributo_original(self, nombre)

#     clase_.__getattribute__ = nuevo_getattribute
#     return clase_


# @contador_acceso
# class Coche:
#     def __init__(self, codigo_seguridad):
#         self.kilometraje = 0
#         self.codigo_seguridad = codigo_seguridad

# coche = Coche('ABC123')

# print('El kilometraje actual es de', coche.kilometraje, 'km')
# print('El código de seguridad es', coche.codigo_seguridad)

###################
# Sección 2.5.1.1
###################

# class Example:
#     def __init__(self, value):
#         self.__internal = value

#     def get_internal(self):
#         return self.__internal

# example1 = Example(10)
# example2 = Example(99)
# print(example1.get_internal())
# print(example2.get_internal())

###################
# Sección 2.5.1.3
###################

# class Example:
#     __internal_counter = 0

#     def __init__(self, value):
#         Example.__internal_counter +=1

#     @classmethod
#     def get_internal(cls):
#         return '# of objects created: {}'.format(cls.__internal_counter)

# print(Example.get_internal())

# example1 = Example(10)
# print(Example.get_internal())

# example2 = Example(99)
# print(Example.get_internal())

###################
# Sección 2.5.1.4
###################

# class Example:
#     __internal_counter = 0

#     def __init__(self, value):
#         Example.__internal_counter +=1

#     @classmethod
#     def get_internal(cls):
#         return '# of objects created: {}'.format(cls.__internal_counter)

# print(Example.get_internal())

# example1 = Example(10)
# print(Example.get_internal())

# example2 = Example(99)
# print(Example.get_internal())


###########################################
# # Comparación de métodos
###########################################

# class Clase:
#     __contador_interno = 0

#     def __init__(self, valor):
#         Clase.__contador_interno +=1

#     def metodo_no_instancia():
#         print('metodo_no_instancia() - valor de __contador_interno:', Clase.__contador_interno)
#         return 'metodo_no_instancia() - Puedo acceder a variables de clase como __contador_interno y sólo pueden invocarme a través de la clase'

#     @staticmethod
#     def metodo_estatico():
#         print('metodo_estatico() - valor de __contador_interno:', Clase.__contador_interno)
#         return 'metodo_estatico() - Puedo acceder a variables de clase como __contador_interno y me pueden invocar a través de la clase o de las instancias'

#     @classmethod
#     def metodo_clase(cls):
#         print('metodo_clase() - puedo acceder a variables de clase como __contador_interno a través del parámetro cls:',cls.__contador_interno)
#         return 'metodo_clase() - y me pueden invocar a través de la clase o de las instancias'

# ###############################
# # pruebas metodo_no_instancia()
# ###############################

# # Un método que no sea de instancia ni estático ni de clase sólo puede invocarse a través de la clase
# print(Clase.metodo_no_instancia())

# # Esto falla porque Python lo invoca como si fuera un método de instancia, pasando el parámetro self
# objeto1 = Clase(10)
# print(objeto1.metodo_no_instancia())

# ###############################
# # pruebas metodo_estático()
# ###############################

# # Un método estático se puede invocar a través de la clase o de instancias de la clase
# print(Clase.metodo_estatico())

# # ahora ésto funciona
# objeto1 = Clase(10)
# print(objeto1.metodo_estatico())

# ###############################
# # pruebas metodo_clase()
# ###############################

# # Un método de clase se puede invocar a través de la clase o de instancias de la clase
# # y tiene acceso al contexto de ejecución a través del parámetro cls


# print(Clase.metodo_clase())

# objeto1 = Clase(10)
# print(objeto1.metodo_clase())

# ##################
# Sección 2.5.1.5
# ##################

# class Coche:
#     def __init__(self, codigo_seguridad):
#         print('Llamada a __init__() con código de seguridad', codigo_seguridad)
#         self.codigo_seguridad = codigo_seguridad
#         self.marca = ''

#     @classmethod
#     def crear_coche_incluyendo_marca(cls, codigo_seguridad, marca):
#         print('Llamada al método de clase')
#         _coche = cls(codigo_seguridad) # llamada al constructor de la clase a través de cls
#         _coche.marca = marca
#         return _coche

#     def __str__(self):
#         return 'Código de seguridad: %s - Marca: %s' % (self.codigo_seguridad,self.marca)

# coche1 = Coche('ABCD1234')
# print('Coche1:',coche1)

# print()

# coche2 = Coche.crear_coche_incluyendo_marca('DEF567', 'Volkswagen')
# print('Coche2',coche2)

##########################
# Singleton pattern
##########################

# class Singleton(object):
#     _instancia = None

#     def __init__(self):
#         raise RuntimeError('Solo puedes crear instancias de ésta clase mediante el método get_instancia()')

#     @classmethod
#     def get_instancia(cls):
#         if cls._instancia is None:
            # print('Creando nueva instancia de la clase')
#             cls._instancia = cls.__new__(cls)
#         return cls._instancia

# ###################

# # objeto_singleton1 = Singleton()

# objeto_singleton2 = Singleton.get_instancia()
# objeto_singleton3 = Singleton.get_instancia()
# objeto_singleton4 = Singleton.get_instancia()

# print(id(objeto_singleton2))
# print(id(objeto_singleton3))
# print(id(objeto_singleton4))

###################
# Sección 2.5.1.6
###################

# class CuentaBancaria:
#     def __init__(self, iban):
#         # print('__init__')
#         self.iban = iban
            
#     @staticmethod
#     def validar(iban):
#         if len(iban) == 20:
#             print('Validación correcta')
#         else:
#             print('Validación fallida')


# CuentaBancaria.validar('ES222233334444555566')

# print()

# cuenta1 = CuentaBancaria('ES222233334444555566')

# cuenta1.validar('ES22223333')

###################
# Sección 2.5.1.7
###################

# class CuentaBancaria:
#     def __init__(self, iban):
#         # print('__init__')
#         self.iban = iban
            
#     @staticmethod
#     def validar(iban):
#         if len(iban) == 20:
#             return True
#         else:
#             return False
        
# cuentas_bancarias = ['8' * 20, '7' * 4, '2222']

# for cuenta in cuentas_bancarias:
#     if CuentaBancaria.validar(cuenta):
#         print('Podemos usar el número de cuenta', cuenta, ' para crear una cuenta bancaria')
#     else:
#         print('El número de cuenta bancaria', cuenta, 'es inválido')

##################################
# Laboratorio de Sección 2.5.1.7
##################################

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


###################
# Sección 2.6.1.3
###################

# class BluePrint:
#     def hello(self):
#         print('Nothing is blue unless you need it')


# bp = BluePrint()
# bp.hello()

###################
# Sección 2.6.1.4
###################

# import abc

# class BluePrint(abc.ABC):
#     @abc.abstractmethod
#     def hello(self):
#         pass

# class GreenField(BluePrint):
#     def hello(self):
#         print('Welcome to Green Field!')


# gf = GreenField()
# gf.hello()

###################
# Sección 2.6.1.5
###################

# import abc

# class BluePrint(abc.ABC):
#     @abc.abstractmethod
#     def hello(self):
#         pass

# class GreenField(BluePrint):
#     def hello(self):
#         print('Welcome to Green Field!')


# gf = GreenField()
# gf.hello()

# bp = BluePrint()

###################
# Sección 2.6.1.6
###################

# import abc


# class BluePrint(abc.ABC):
#     @abc.abstractmethod
#     def hello(self):
#         pass


# class GreenField(BluePrint):
#     def hello(self):
#         print('Welcome to Green Field!')


# class RedField(BluePrint):
#     def yellow(self):
#         pass


# gf = GreenField()
# gf.hello()

# rf = RedField()

#################################
# Laboratorio de Sección 2.6.1.8
#################################

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

##################
# Sección 2.7.1.3
##################

# class TankError(Exception):
#     pass


# class Tank:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.__level = 0

#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def level(self, amount):
#         if amount > 0:
#             # fueling
#             if amount <= self.capacity:
#                 self.__level = amount
#             else:
#                 raise TankError('Too much liquid in the tank')
#         elif amount < 0:
#             raise TankError('Not possible to set negative liquid level')

#     @level.deleter
#     def level(self):
#         if self.__level > 0:
#            print('It is good to remember to sanitize the remains from the tank!')
#        self.__level = None

##################
# Sección 2.7.1.4
##################

# class TankError(Exception):
#     pass


# class Tank:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.__level = 0

#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def level(self, amount):
#         if amount > 0:
#             # fueling
#             if amount <= self.capacity:
#                 self.__level = amount
#             else:
#                 raise TankError('Too much liquid in the tank')
#         elif amount < 0:
#             raise TankError('Not possible to set negative liquid level')

#     @level.deleter
#     def level(self):
#         if self.__level > 0:
#             print('It is good to remember to sanitize the remains from the tank!')
#         self.__level = None

# # our_tank object has a capacity of 20 units
# our_tank = Tank(20)

# # our_tank's current liquid level is set to 10 units
# our_tank.level = 10
# print('Current liquid level:', our_tank.level)

# # adding additional 3 units (setting liquid level to 13)
# our_tank.level += 3
# print('Current liquid level:', our_tank.level)

# # let's try to set the current level to 21 units
# # this should be rejected as the tank's capacity is 20 units
# try:
#     our_tank.level = 21
# except TankError as e:
#     print('Trying to set liquid level to 21 units, result:', e)

# # similar example - let's try to add an additional 15 units
# # this should be rejected as the total capacity is 20 units
# try:
#     our_tank.level += 15
# except TankError as e:
#     print('Trying to add an additional 15 units, result:', e)

# # let's try to set the liquid level to a negative amount
# # this should be rejected as it is senseless
# try:
#     our_tank.level = -3
# except TankError as e:
#     print('Trying to set liquid level to -3 units, result:', e)

# print('Current liquid level:', our_tank.level)

# del our_tank.level

#################################
# Laboratorio de Sección 2.7.1.5
#################################

# class ExcepcionCuentaBancaria(Exception):
#     pass

# class CuentaBancaria:
#     def __init__(self, numero_cuenta):
#         self.__saldo = 0
#         self.__numero_cuenta = numero_cuenta
#         pass

#     @property
#     def saldo(self):
#         return self.__saldo

#     @saldo.setter
#     def saldo(self, valor):
#         if valor < 0:
#             raise ExcepcionCuentaBancaria('No es posible asignar un saldo negativo a la cuenta')

#         if abs(self.__saldo - valor) > 100_000:
#             print('Esta operación se está auditando')

#         self.__saldo = valor

#     @saldo.deleter
#     def saldo(self):
#         if self.__saldo > 0:
#             raise ExcepcionCuentaBancaria('No es posible eliminar una cuenta mientras tenga saldo')
#         self.__saldo = None

#     @property
#     def numero_cuenta(self):
#         return self.__numero_cuenta

#     @numero_cuenta.setter
#     def numero_cuenta(self, value):
#         raise ExcepcionCuentaBancaria('Operación inválida')

#     @numero_cuenta.deleter
#     def numero_cuenta(self):
#         raise ExcepcionCuentaBancaria('Operación inválida')

#     def __str__(self):
#         return 'El saldo actual de la cuenta #{} es de {} €'.format(self.__numero_cuenta, self.__saldo)

# cuenta = CuentaBancaria('34-6514-7654-9999-0002')
# cuenta.saldo += 1000
# print(cuenta)

# try:
#     cuenta.saldo = -200
# except ExcepcionCuentaBancaria as e:
#     print('Excepción generada:', e)

# try:
#     cuenta.numero_cuenta = 'Nuevo númerod e cuenta'
# except ExcepcionCuentaBancaria as e:
#     print('Excepción generada:', e)

# try:
#     cuenta.saldo += 1_000_000
# except ExcepcionCuentaBancaria as e:
#     print('Excepción generada:', e)

# try:
#     del cuenta.saldo
# except ExcepcionCuentaBancaria as e:
#     print('Excepción generada:', e)

##################
# Sección 2.8.1.3
##################

# class Car:
#     def __init__(self, engine):
#         self.engine = engine


# class GasEngine:
#     def __init__(self, horse_power):
#         self.hp = horse_power

#     def start(self):
#         print('Starting {}hp gas engine'.format(self.hp))


# class DieselEngine:
#     def __init__(self, horse_power):
#         self.hp = horse_power

#     def start(self):
#         print('Starting {}hp diesel engine'.format(self.hp))


# my_car = Car(GasEngine(4))
# my_car.engine.start()
# my_car.engine = DieselEngine(2)
# my_car.engine.start()

##################
# Sección 2.8.1.5
##################

# class Base_Computer:
#     def __init__(self, serial_number):
#         self.serial_number = serial_number


# class Personal_Computer(Base_Computer):
#     def __init__(self, sn, connection):
#         super().__init__(sn)
#         self.connection = connection
#         print('The computer costs $1000')


# class Connection:
#     def __init__(self, speed):
#         self.speed = speed

#     def download(self):
#         print('Downloading at {}'.format(self.speed))


# class DialUp(Connection):
#     def __init__(self):
#         super().__init__('9600bit/s')

#     def download(self):
#         print('Dialling the access number ... '.ljust(40), end='')
#         super().download()


# class ADSL(Connection):
#     def __init__(self):
#         super().__init__('2Mbit/s')

#     def download(self):
#         print('Waking up modem  ... '.ljust(40), end='')
#         super().download()


# class Ethernet(Connection):
#     def __init__(self):
#         super().__init__('10Mbit/s')

#     def download(self):
#         print('Constantly connected... '.ljust(40), end='')
#         super().download()

# # I started my IT adventure with an old-school dial up connection
# my_computer = Personal_Computer('1995', DialUp())
# my_computer.connection.download()

# # then it came year 1999 with ADSL
# my_computer.connection = ADSL()
# my_computer.connection.download()

# # finally I upgraded to Ethernet
# my_computer.connection = Ethernet()
# my_computer.connection.download()

##################
# Sección 2.8.1.6
##################

# class Base_Computer:
#     def __init__(self, serial_number):
#         self.serial_number = serial_number


# class Personal_Computer(Base_Computer):
#     def __init__(self, sn, connection):
#         super().__init__(sn)
#         self.connection = connection
#         print('The computer costs $1000')


# class Connection:
#     def __init__(self, speed):
#         self.speed = speed

#     def download(self):
#         print('Downloading at {}'.format(self.speed))


# class DialUp(Connection):
#     def __init__(self):
#         super().__init__('9600bit/s')

#     def download(self):
#         print('Dialling the access number ... '.ljust(40), end='')
#         super().download()


# class ADSL(Connection):
#     def __init__(self):
#         super().__init__('2Mbit/s')

#     def download(self):
#         print('Waking up modem  ... '.ljust(40), end='')
#         super().download()


# class Ethernet(Connection):
#     def __init__(self):
#         super().__init__('10Mbit/s')

#     def download(self):
#         print('Constantly connected... '.ljust(40), end='')
#         super().download()

# # I started my IT adventure with an old-school dial up connection
# my_computer = Personal_Computer('1995', DialUp())
# my_computer.connection.download()

# # then in the year 1999 I got ADSL
# my_computer.connection = ADSL()
# my_computer.connection.download()

# # finally I upgraded to Ethernet
# my_computer.connection = Ethernet()
# my_computer.connection.download()

#################################
# Laboratorio de Sección 2.8.1.7
#################################

# class Vehiculo:
#     def __init__(self, codigo_seguridad, motor, ruedas):
#         self.codigo_seguridad = codigo_seguridad
#         self.motor = motor
#         self.ruedas = ruedas

# class Ruedas:
#     def __init__(self, talla):
#         self.talla = talla
#         self.presion = 0

#     def recuperar_presion(self):
#         return self.presion

#     def inflar(self, presion_inflado):
#         self.presion = presion_inflado

# class Motor:
#     def __init__(self, combustible):
#         self.combustible = combustible
#         self.estado = 'apagado'

#     def encender(self):
#         self.estado = 'encendido'

#     def apagar(self):
#         self.estado = 'apagado'

#     def recuperar_estado(self):
#         return self.estado

# ruedas_urbanas = Ruedas(15)
# ruedas_todo_terreno = Ruedas(18)

# motor_electrico = Motor('Eléctrico')
# motor_gasolina = Motor('Gasolina')

# vehiculo_urbano = Vehiculo('111A', motor_electrico, ruedas_urbanas)
# vehiculo_todo_terreno = Vehiculo('888S', motor_gasolina, ruedas_todo_terreno)

# # preparar el vehículo todoterreno para un rally
# print('El motor del vehículo todoterreno', vehiculo_todo_terreno.motor.recuperar_estado())
# vehiculo_todo_terreno.ruedas.inflar(10)
# vehiculo_todo_terreno.motor.encender()
# print('El motor del vehículo todoterreno está', vehiculo_todo_terreno.motor.recuperar_estado())

# # preparar el vehículo urbano para ir de compras
# print('El motor del vehículo urbano', vehiculo_urbano.motor.recuperar_estado())
# vehiculo_urbano.ruedas.inflar(3)
# vehiculo_urbano.motor.encender()
# print('El motor del vehículo urbano', vehiculo_urbano.motor.recuperar_estado())
# vehiculo_urbano.motor.apagar()
# print('El motor del vehículo urbano', vehiculo_urbano.motor.recuperar_estado())

##################
# Sección 2.9.1.2
##################

# class IntegerList(list):

#     @staticmethod
#     def check_value_type(value):
#         if type(value) is not int:
#             raise ValueError('Not an integer type')

#     def __setitem__(self, index, value):
#         IntegerList.check_value_type(value)
#         list.__setitem__(self, index, value)

#     def append(self, value):
#         IntegerList.check_value_type(value)
#         list.append(self, value)

#     def extend(self, iterable):
#         for element in iterable:
#             IntegerList.check_value_type(element)

#         list.extend(self, iterable)


# int_list = IntegerList()

# int_list.append(66)
# int_list.append(22)
# print('Appending int elements succeed:', int_list)

# int_list[0] = 49
# print('Inserting int element succeed:', int_list)

# int_list.extend([2, 3])
# print('Extending with int elements succeed:', int_list)

# try:
#     int_list.append('8-10')
# except ValueError:
#     print('Appending string failed')

# try:
#     int_list[0] = '10/11'
# except ValueError:
#     print('Inserting string failed')

# try:
#     int_list.extend([997, '10/11'])
# except ValueError:
#     print('Extending with ineligible element failed')

# print('Final result:', int_list)

##################
# Sección 2.9.1.3
##################

# from datetime import datetime


# class MonitoredDict(dict):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.log = list()
#         self.log_timestamp('MonitoredDict created')

#     def __getitem__(self, key):
#         val = super().__getitem__(key)
#         self.log_timestamp('value for key [{}] retrieved'.format(key))
#         return val

#     def __setitem__(self, key, val):
#         super().__setitem__(key, val)
#         self.log_timestamp('value for key [{}] set'.format(key))

#     def log_timestamp(self, message):
#         timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
#         self.log.append('{} {}'.format(timestampStr, message))


# kk = MonitoredDict()
# kk[10] = 15
# kk[20] = 5

# print('Element kk[10]:', kk[10])
# print('Whole dictionary:', kk)
# print('Our log book:\n')
# print('\n'.join(kk.log))

##################
# Sección 2.9.1.4
##################

# # IBAN Validator

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')
# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     ibann = int(iban2)
#     if ibann % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")


# # British: GB72 HBZU 7006 7212 1253 00
# # French: FR76 30003 03620 00020216907 50
# # German: DE02100100100152517108

##################
# Sección 2.9.1.5
##################

# class IBANValidationError(Exception):
#     pass


# def validateIBAN(iban):
#     iban = iban.replace(' ', '')

#     if not iban.isalnum():
#         raise IBANValidationError("You have entered invalid characters.")

#     elif len(iban) < 15:
#         raise IBANValidationError("IBAN entered is too short.")

#     elif len(iban) > 31:
#         raise IBANValidationError("IBAN entered is too long.")

#     else:
#         iban = (iban[4:] + iban[0:4]).upper()
#         iban2 = ''
#         for ch in iban:
#             if ch.isdigit():
#                 iban2 += ch
#             else:
#                 iban2 += str(10 + ord(ch) - ord('A'))
#         ibann = int(iban2)

#         if ibann % 97 != 1:
#             raise IBANValidationError("IBAN entered is invalid.")

#         return True


# test_keys = ['GB72 HBZU 7006 7212 1253 01', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108' ]

# for key in test_keys:
#     try:
#         print('Status of "{}" validation: '.format(key))
#         validateIBAN(key)
#     except IBANValidationError as e:
#         print("\t{}".format(e))
#     else:
#         print("\tcorrect")

##################
# Sección 2.9.1.6
##################

# import random


# class IBANValidationError(Exception):
#     pass


# class IBANDict(dict):
#     def __setitem__(self, _key, _val):
#         if validateIBAN(_key):
#             super().__setitem__(_key, _val)

#     def update(self, *args, **kwargs):
#         for _key, _val in dict(*args, **kwargs).items():
#             self.__setitem__(_key, _val)

# ##########

# def validateIBAN(iban):
#     iban = iban.replace(' ', '')

#     if not iban.isalnum():
#         raise IBANValidationError("You have entered invalid characters.")

#     elif len(iban) < 15:
#         raise IBANValidationError("IBAN entered is too short.")

#     elif len(iban) > 31:
#         raise IBANValidationError("IBAN entered is too long.")

#     else:
#         iban = (iban[4:] + iban[0:4]).upper()
#         iban2 = ''
#         for ch in iban:
#             if ch.isdigit():
#                 iban2 += ch
#             else:
#                 iban2 += str(10 + ord(ch) - ord('A'))
#         ibann = int(iban2)

#         if ibann % 97 != 1:
#             raise IBANValidationError("IBAN entered is invalid.")

#         return True


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

