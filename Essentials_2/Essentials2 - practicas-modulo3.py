######################
# Sección 3.1.1.7
######################

# class TheSimplestClass:
#     pass

# #############################################

# my_first_object = TheSimplestClass()

# print(my_first_object)

# my_second_object = TheSimplestClass()

# print(my_second_object)

# my_third_object = my_second_object

# print(my_third_object)


######################
# Sección 3.2.1.1
######################

# stack = []

# def push(val):
#     stack.append(val)


# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val

# ######################################

# push(3)
# push(2)
# push(1)

# print("Lista:", stack)

# print(pop())
# print(pop())
# print(pop())

# print("Lista:", stack)

######################
# Sección 3.2.1.4
######################

# class Stack:             # Definiendo la clase de la pila.
#     def __init__(self):  # Definiendo la función del constructor.
#         print("¡Ejecutando código en el constructor de la clase Stack!")


# stack_object  = Stack()  # Instanciando el objeto.

# stack_object1 = Stack()  # Instanciando el objeto.

# stack_object2 = Stack()  # Instanciando el objeto.

######################
# Sección 3.2.1.5
######################

# class Stack:
#     def __init__(self):
#         self.lista = []

# ##############################################

# obj1 = Stack()

# print(len(obj1.lista))


######################
# Sección 3.2.1.6
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

# #################################################

# stack_object = Stack()
# print(len(stack_object.__stack_list))

######################
# Sección 3.2.1.7
######################

# class Stack:
#     def __init__(self):
#         self.__pila = []

#     def push(self, valor):
#         self.__pila.append(valor)

#     def pop(self):
#         valor = self.__pila[-1]
#         del self.__pila[-1]
#         return valor

# # ############################################

# stack_object = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())

# print("segunda pila:")

# stack_object2 = Stack()

# stack_object2.push(30)
# stack_object2.push(20)
# stack_object2.push(10)

# print(stack_object2.pop())
# print(stack_object2.pop())
# print(stack_object2.pop())

######################
# Sección 3.2.1.8
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# stack_object_1 = Stack()
# stack_object_2 = Stack()

# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())

# print(stack_object_2.pop())

######################
# Sección 3.2.1.9
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()

# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)
# print(funny_stack.pop())

######################
# Sección 3.2.1.10
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
# ####################################################

# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

######################
# Sección 3.2.1.11
######################

# class Stack:
#     def __init__(self):
#         self.__stackList = []

#     def push(self, val):
#         self.__stackList.append(val)

#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0


# # Ingresa código aquí.

# def push(self, val):
#     self.__sum += val
#     Stack.push(self, val)

######################
# Sección 3.2.1.12
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def get_sum(self):
#         return self.__sum

#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)

#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val


# stack_object = AddingStack()

# for i in range(5):
#     stack_object.push(i)

# print("Suma de elementos en la pila",stack_object.get_sum())

# for i in range(5):
#     print("Retirando elemento de la pila:",stack_object.pop())

######################
#### POLIMORFISMO #### 
######################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#     def __str__(self):
#         cadena = "["
#         for indice in range(len(self.__stack_list) - 1):
#             cadena += str(self.__stack_list[indice]) + ","
#         cadena += str(self.__stack_list[-1]) + "]"
#         return cadena


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def get_sum(self):
#         return self.__sum

#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)

#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#     def __str__(self):
#         return Stack.__str__(self) + " - Suma: " + str(self.__sum)


# stack_object = AddingStack()

# for i in range(5):
#     stack_object.push(i)

# print(stack_object)


# # print("Suma de elementos en la pila",stack_object.get_sum())

# # for i in range(5):
# #     print("Retirando elemento de la pila:",stack_object.pop())

######################
# Sección 3.2.1.13
######################

# # Ejercicio 1

# # Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.

# class Python(Snakes):




# # Ejercicio 2

# # Algo falta en la siguiente declaración, ¿qué es?

# class Snakes
#     def __init__():
#         self.sound = 'Sssssss'


# # El constructor __init__() carece del parámetro obligatorio (deberíamos llamarlo self para cumplir con los estándares).



# # Ejercicio 3

# # Modifica el código para garantizar que la propiedad venomous sea privada.

# class Snakes
#     def __init__(self):
#         self.venomous = True
# 		

# # El código debería verse como sigue:

# # class Snakes
# #     def __init__(self):
# #         self.__venomous = True

###################################
# Sección 3.2.1.14 - Laboratorio
###################################

# class Stack:
#     def __init__(self):
#         self.__stk = []

#     def push(self, val):
#         self.__stk.append(val)

#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val

# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__counter = 0

#     def get_counter(self):
#         return self.__counter

#     def pop(self):
#         self.__counter += 1
#         return Stack.pop(self)

# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

###################################
# Sección 3.2.1.15 - Laboratorio
###################################

# class QueueError(IndexError):
#     pass

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def put(self, elem):
#         self.queue.insert(0, elem)

#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError


# que = Queue()
# que.put(1)
# que.put("perro")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Error de Cola")

###################################
# Sección 3.2.1.16 - Laboratorio
###################################

# class QueueError(IndexError):
#     pass


# class Queue:
#     def __init__(self):
#         self.queue = []
#     def put(self,elem):
#         self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError


# class SuperQueue(Queue):
#     def isempty(self):
#         return len(self.queue) == 0


# que = SuperQueue()
# que.put(1)
# que.put("perro")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Cola vacía")

######################
# Sección 3.3.1.1
######################

# # Diferentes objetos de la misma clase pueden poseer diferentes conjuntos de propiedades.
# # Debe haber una manera de verificar con seguridad si un objeto específico posee la propiedad 
# # que deseas utilizar (a menos que quieras generar una excepción, siempre vale la pena considerarlo).
# # Cada objeto lleva su propio conjunto de propiedades, no interfieren entre sí de ninguna manera.
# # Tales variables (propiedades) se llaman variables de instancia.

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades 
# y métodos predefinidos. 
# Cada objeto los tiene, los quieras o no. 
# Uno de ellos es una variable llamada __dict__ (es un diccionario).

# La variable contiene los nombres y valores de todas las propiedades (variables) 
# que el objeto contiene actualmente. 
# Vamos a usarla para presentar de forma segura el contenido de un objeto.


######################
# Sección 3.3.1.2
######################

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val

#     def set_second(self, val = 2):
#         self.__second = val


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5


# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# print(example_object_1._ExampleClass__first)

######################
# Sección 3.3.1.3
######################

# # Variables de clase
# # Una variable de clase es una propiedad que existe en una sola copia 
# # y se almacena fuera de cualquier objeto.

# # Nota: no existe una variable de instancia si no hay ningún objeto de la clase; 
# # solo existe una variable de clase en una copia, incluso si no hay objetos en la clase.

# # Las variables de clase se crean de manera diferente. El ejemplo te dirá más:

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# Las variables de clase no se muestran en el diccionario de un objeto __dict__ 
# (esto es natural ya que las variables de clase no son partes de un objeto), 
# pero siempre puedes intentar buscar en la variable del mismo nombre, pero a nivel de clase, 
# te mostraremos esto muy pronto.
# Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).

######################
# Sección 3.3.1.4
######################

# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

######################
# Sección 3.3.1.5
######################

# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val


# print(ExampleClass.__dict__)
# example_object = ExampleClass(2)

# print(ExampleClass.__dict__)
# print(example_object.__dict__)

######################
# Sección 3.3.1.6
######################

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1


# example_object = ExampleClass(1)

# print(example_object.a)
# print(example_object.b)

######################
# Sección 3.3.1.7
######################

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1


# example_object = ExampleClass(1)
# print(example_object.a)

# if hasattr(example_object, 'b'):
#     print(example_object.b)

######################
# Sección 3.3.1.8
######################

# class ExampleClass:
#     attr = 1


# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))

#######################################

# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2


# example_object = ExampleClass()

# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))

######################
# Sección 3.3.1.9
######################

# class Sample:
#     gamma = 0 # Class variable.
#     def __init__(self):
#         self.alpha = 1 # Variable de instancia.
#         self.__delta = 3 # Variable de instancia privada.


# obj = Sample()
# obj.beta = 2  # Otra variable de instancia (que existe solo dentro de la instancia "obj").
# print(obj.__dict__)

# #################################3

# # Ejercicio 1

# # ¿Cuáles de las propiedades de la clase Python son variables de instancia y cuáles son variables de clase? ¿Cuáles de ellos son privados? 

# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False


# # population y victims son variables de clase, 
# # mientras que length y __venomous son variables de instancia (esta última también es privada).



# # Ejercicio 2

# # Vas a negar la propiedad __venomous del objeto version_2, 
# # ignorando el hecho de que la propiedad es privada. ¿Cómo vas a hacer esto?

# version_2 = Python()


# # version_2._Python__venomous = not version_2._Python__venomous



# # Ejercicio 3

# # Escribe una expresión que compruebe si el objeto version_2 contiene una propiedad de instancia denominada constrictor (¡si, constrictor!).

# # hasattr(version_2, 'constrictor')

######################
# Sección 3.4.1.1
######################

# class Classy:
#     def method(self):
#         print("método")


# obj = Classy()
# obj.method()


# # Si deseas que el método acepte parámetros distintos a self, debes:

# # Colocarlos después de self en la definición del método.
# # Pasarlos como argumentos durante la invocación sin especificar self.
# # Justo como aqui:

# class Classy:
#     def method(self, par):
#         print("método:", par)


# obj = Classy()
# obj.method(1)
# obj.method(2)
# obj.method(3)

######################
# Sección 3.4.1.2
######################

# # El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.

# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)


# obj = Classy()
# obj.var = 3
# obj.method()


# # El parámetro self también se usa para invocar otros métodos desde dentro de la clase.

# # Justo como aquí:

# class Classy:
#     def other(self):
#         print("otro")

#     def method(self):
#         print("método")
#         self.other()


# obj = Classy()
# obj.method()

######################
# Sección 3.4.1.3
######################

# El constructor:

# Esta obligado a tener el parámetro self (se configura automáticamente).
# Pudiera (pero no necesariamente) tener mas parámetros que solo self; si esto sucede, 
# la forma en que se usa el nombre de la clase para crear el objeto debe tener la definición  __init__.
# Se puede utilizar para configurar el objeto, es decir, 
# inicializa adecuadamente su estado interno, crea variables de instancia, 
# crea instancias de cualquier otro objeto si es necesario, etc.

# Ten en cuenta que el constructor:

# No puede retornar un valor, ya que está diseñado para devolver un objeto recién creado y nada más.
# No se puede invocar directamente desde el objeto o desde dentro de la clase 
# (puedes invocar un constructor desde cualquiera de las superclases del objeto, 
#  pero discutiremos esto más adelante).

# class Classy:
#     def __init__(self, value):
#         self.var = value


# obj_1 = Classy("objeto")

# print(obj_1.var)

######################
# Sección 3.4.1.4
######################

# class Classy:
#     def __init__(self, value = None):
#         self.var = value


# obj_1 = Classy("objeto")
# obj_2 = Classy()

# print(obj_1.var)
# print(obj_2.var)


# ######################################


# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):
#         print("oculto")


# obj = Classy()
# obj.visible()

# try:
#     obj.__hidden()
# except:
#     print("fallido")

# obj._Classy__hidden()

######################
# Sección 3.4.1.5
######################

# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2

#     def method(self):
#         pass

#     def __hidden(self):
#         pass


# obj = Classy()

# print(obj.__dict__)
# print(Classy.__dict__)

######################
# Sección 3.4.1.6
######################

# class Classy:
#     pass


# print(Classy.__name__)
# obj = Classy()
# print(type(obj).__name__)

# print(obj.__name__) # AttributeError

######################
# Sección 3.4.1.7
######################

# class Classy:
#     pass


# print(Classy.__module__)
# obj = Classy()
# print(obj.__module__)

######################
# Sección 3.4.1.8
######################

# class SuperOne:
#     pass


# class SuperTwo:
#     pass


# class Sub(SuperOne, SuperTwo):
#     pass


# def printBases(cls):
#     print('( ', end='')

#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')


# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(Sub)

######################
# Sección 3.4.1.9
######################

# Introspección, que es la capacidad de un programa para examinar el tipo 
# o las propiedades de un objeto en tiempo de ejecución.
# Reflexión, que va un paso más allá, y es la capacidad de un programa 
# para manipular los valores, propiedades y/o funciones de un objeto en tiempo de ejecución.

######################
# Sección 3.4.1.10
######################

# class MyClass:
#     pass


# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5


# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)


# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)

######################
# Sección 3.4.1.11
######################

# class Sample:
#     def __init__(self):
#         self.name = Sample.__name__
#     def myself(self):
#         print("Mi nombre es " + self.name + " y vivo en " + Sample.__module__)


# obj = Sample()
# obj.myself()

##########################################

# # Ejercicio 1

# # La declaración de la clase Snake se muestra a continuación. 
# # Enriquece la clase con un método llamado increment(), el cual incrementa en 1 la propiedad victims.

# class Snake:
#     def __init__(self):
#         self.victims = 0


# # class Snake:
# #     def __init__(self):
# #         self.victims = 0

# #     def increment(self):
# #         self.victims += 1




# # Ejercicio 2

# # Redefine el constructur de la clase Snake para que tenga un parámetro 
# # que inicialice el campo victims con un valor pasado al objeto durante la construcción.


# # class Snake:
# #     def __init__(self, victims):
# #         self.victims = victims	



# # Ejercicio 3

# # ¿Puedes predecir el resultado del siguiente código?

# class Snake:
#     pass


# class Python(Snake):
#     pass


# print(Python.__name__, 'es una', Snake.__name__)
# print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)


# # Python es una Snake
# # Snake puede ser una Python

######################################
# Sección 3.4.1.12 - Laboratorio
######################################

# def two_digits(val):
#     return str(val).zfill(2)

# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds

#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#                two_digits(self.__minutes) + ":" + \
#                two_digits(self.__seconds)

#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0

#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23

##############################

# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)

###############################

# import time, os

# def limpiar_consola():
#     os.system('cls' if os.name == 'nt' else 'clear')

# while True:
#     limpiar_consola()
#     timer.next_second()
#     print(timer)
#     time.sleep(1)

######################################
# Sección 3.4.1.13 - Laboratorio
######################################

# class WeekDayError(Exception):
#     pass

# class Weeker:
#     __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

#     def __init__(self, day):
#         try:
#             self.__current = Weeker.__names.index(day)
#         except ValueError:
#             raise WeekDayError

#     def __str__(self):
#         return Weeker.__names[self.__current]

#     def add_days(self, n):
#         self.__current = (self.__current + n) % 7

#     def subtract_days(self, n):
#         self.__current = (self.__current - n) % 7

# try:
#     weekday = Weeker('Lun')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)

#     weekday = Weeker('XXX')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")

######################################
# Sección 3.4.1.14 - Laboratorio
######################################

# import math

# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def __getx(self):
#         return self.__x

#     def __gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.__getx(), point.__gety())

# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))

######################################
# Sección 3.4.1.15 - Laboratorio
######################################

# import math

# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())

#     def __str__(self) -> str:
#         return '(' + str(self.__x) + ',' + str(self.__y) + ')'

# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         per = 0
#         for i in range(3):
#             print('Calculando distancia entre',self.__vertices[i], 'y', self.__vertices[(i + 1) % 3])
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#         return per

# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())

######################
# Sección 3.5.1.1
######################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)

######################
# Sección 3.5.1.2
######################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' en ' + self.galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)

######################
# Sección 3.5.1.4
######################

# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()

######################
# Sección 3.5.1.5
######################

# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()

######################
# Sección 3.5.1.6
######################

# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print('object_1 is object_2:', object_1 is object_2)
# print('object_1 == object_2:', object_1 == object_2)

# print('object_2 is object_3:', object_2 is object_3)
# print('object_2 == object_3:', object_2 == object_3)

# print('object_3 is object_1:', object_3 is object_1)
# print('object_3 == object_1:', object_3 == object_1)

# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"

# print(string_1 == string_2, string_1 is string_2)

########################################
# sobreescritura del método __eq__
########################################

# class MiClase:
#     def __init__(self, attr1, attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2
        
#     def __eq__(self, otro): 
#         if not isinstance(otro, MiClase):
#             return False
#         return self.attr1 == otro.attr1 and self.attr2 == otro.attr2

# c1 = MiClase(100, 10) 
# c2 = MiClase(100, 10) 
# c3 = c1 

# print('c1 == c2', c1 == c2)
# print('c1 is c2', c1 is c2)
# print('c2 == c3', c2 == c3)
# print('c2 is c3', c2 is c3)
# print('c3 == c1', c3 == c1)
# print('c3 is c1', c3 is c1)

######################
# Sección 3.5.1.7
######################

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name + ". - Super"


# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#     def __str__(self):
#         return "Mi nombre es " + self.name + ". - Sub"

# obj = Sub("Andy")

# print(obj)


######################
# Sección 3.5.1.8
######################

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."


# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)


# obj = Sub("Andy")

# print(obj)

######################
# Sección 3.5.1.9
######################

# # Probando propiedades: variables de clase.
# class Super:
#     supVar = 1


# class Sub(Super):
#     subVar = 2


# obj = Sub()

# print(obj.subVar)
# print(obj.supVar)

######################
# Sección 3.5.1.10
######################

# # Probando propiedades: variables de instancia.
# class Super:
#     def __init__(self):
#         self.supVar = 11


# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12


# obj = Sub()

# print(obj.subVar)
# print(obj.supVar)

######################
# Sección 3.5.1.11
######################

# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101

#     def fun_1(self):
#         return 102


# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
    
#     def fun_2(self):
#         return 202


# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301

#     def fun_3(self):
#         return 302


# obj = Level3()

# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

######################
# Sección 3.5.1.12
######################

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11


# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21


# class Sub(SuperA, SuperB):
#     pass


# obj = Sub()

# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

#############################
# Pruebas herencia múltiple
#############################

# class Super1:
#     def __init__(self, name):
#         self.name = name + 'Super1'
#         print('Constructor de Super1')

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."

# class Super2:
#     def __init__(self, name):
#         self.name = name + 'Super2'
#         print('Constructor de Super2')

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."

# class Sub(Super1, Super2):
#     def __init__(self, name):
#         super().__init__(name)
        
#         # Super1.__init__(self, name)
#         # Super2.__init__(self, name)


# obj = Sub("Andy")

# print(obj)
# print(obj.__dict__)


######################
# Sección 3.5.1.13
######################

# class Level1:
#     var = 100
#     def fun(self):
#         return 101


# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201


# class Level3(Level2):
#     pass


# obj = Level3()

# print(obj.var, obj.fun())

# class Sub(SuperA, SuperB):
#     pass


# obj = Sub()

# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

######################
# Sección 3.5.1.14
######################

# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"


# class Right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"


# class Sub(Left, Right):
#     pass


# obj = Sub()

# print(obj.var, obj.var_left, obj.var_right, obj.fun())

######################
# Sección 3.5.1.15
######################

# class One:
#     def do_it(self):
#         print("do_it de One")

#     def doanything(self):
#         self.do_it()


# class Two(One):
#     def do_it(self):
#         print("do_it de Two")


# one = One()
# two = Two()

# one.doanything()
# two.doanything()

######################
# Sección 3.5.1.16
######################

# ¿Puedes detectar el error del código?

# Los métodos turn()son muy similares como para dejarlos en esta forma.

# Vamos a reconstruir el código: vamos a presentar una superclase para reunir 
# todos los aspectos similares de los vehículos, trasladando todos los detalles a las subclases.


# import time

# class TrackedVehicle:
#     def control_track(left, stop):
#         pass # no implementado!!

#     def turn(left):
#         control_track(left, True)
#         time.sleep(0.25)
#         control_track(left, False)


# class WheeledVehicle:
#     def turn_front_wheels(left, on):
#         pass # no implementado!

#     def turn(left):
#         turn_front_wheels(left, True)
#         time.sleep(0.25)
#         turn_front_wheels(left, False)

######################
# Sección 3.5.1.17
######################

# import time

# class Vehicle:
#     def change_direction(left, on):
#         pass

#     def turn(left):
#         change_direction(left, True)
#         time.sleep(0.25)
#         change_direction(left, False)


# class TrackedVehicle(Vehicle):
#     def control_track(left, stop):
#         pass

#     def change_direction(left, on):
#         control_track(left, on)


# class WheeledVehicle(Vehicle):
#     def turn_front_wheels(left, on):
#         pass

#     def change_direction(left, on):
#         turn_front_wheels(left, on)


#############################################
# Pruebas @staticmethod - @classmethod
#############################################

# class Super:
#     var_clase = 'Valor de la variable de Clase'
    
#     def __init__(self):
#         var_instancia = 'Valor de la variable de instancia'
    
#     @staticmethod
#     def metodo_estatico(): 
#         Super.var_clase  = 333
#         # Super.metodo_clase()
#         print('Accediendo a var_clase desde metodo_estatico()', Super.var_clase) 
        
#     @classmethod
#     def metodo_clase(cls): 
#         # cls.metodo_estatico()  
#         Super.var_clase  = 444
#         print('Accediendo a var_clase desde metodo_clase()', cls.var_clase)

# #########################################################

# # Super.metodo_estatico()
# Super.metodo_clase()


######################
# Sección 3.5.1.18
######################

# import time

# class Tracks:
#     def change_direction(self, left, on):
#         print("pistas: ", left, on)


# class Wheels:
#     def change_direction(self, left, on):
#         print("ruedas: ", left, on)


# class Vehicle:
#     def __init__(self, controller):
#         self.controller = controller

#     def turn(self, left):
#         self.controller.change_direction(left, True)
#         time.sleep(0.25)
#         self.controller.change_direction(left, False)


# wheeled = Vehicle(Wheels())
# tracked = Vehicle(Tracks())

# wheeled.turn(True)
# tracked.turn(False)

######################
# Sección 3.5.1.20
######################

# class Top:
#     def m_top(self):
#         print("top")


# class Middle(Top):
#     def m_middle(self):
#         print("middle")


# class Bottom(Middle):
#     def m_bottom(self):
#         print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

############################################

# # Sin sorpresas hasta ahora.
# # Hagamos un pequeño cambio en este código. Echa un vistazo:

# class Top:
#     def m_top(self):
#         print("top")


# class Middle(Top):
#     def m_middle(self):
#         print("middle")


# class Bottom(Middle, Top):
#     def m_bottom(self):
#         print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()


# # ¿Puedes ver la diferencia? 
# # Está escondida en esta línea:

# # class Bottom(Middle, Top):

######################
# Sección 3.5.1.21
######################

# class A:
#     pass


# class B(A):
#     pass


# class C(A):
#     pass


# class D(B, C):
#     pass


# d = D()

#################################

# class Top:
#     def m_top(self):
#         print("top")


# class Middle_Left(Top):
#     def m_middle(self):
#         print("middle_left")


# class Middle_Right(Top):
#     def m_middle(self):
#         print("middle_right")


# class Bottom(Middle_Left, Middle_Right):
#     def m_bottom(self):
#         print("bottom")

# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

######################
# Sección 3.5.1.22
######################

# # 1. Un método llamado __str__() es responsable de convertir el contenido 
# # de un objeto en una cadena (más o menos) legible. 
# # Puedes redefinirlo si deseas que tu objeto pueda presentarse de una forma más elegante. 
# # Por ejemplo:

# class Mouse:
#     def __init__(self, name):
#         self.my_name = name


#     def __str__(self):
#         return self.my_name


# the_mouse = Mouse('mickey')
# print(the_mouse)  # Imprime "mickey". 


# # 2. Una función llamada issubclass(Class_1, Class_2) es capaz 
# # de determinar si Class_1 es una subclase de Class_2. Por ejemplo:

# class Mouse:
#     pass


# class LabMouse(Mouse):
#     pass


# print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Imprime "False True"


# # 3. Una función llamada isinstance(Object, Class) 
# # comprueba si un objeto proviene de una clase indicada. 
# # Por ejemplo:

# class Mouse:
#     pass


# class LabMouse(Mouse):
#     pass


# mickey = Mouse()
# print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Imprime "True False".


# # 4. Un operador llamado is comprueba si dos variables hacen referencia al mismo objeto. 
# # Por ejemplo:

# class Mouse:
#     pass


# mickey = Mouse()
# minnie = Mouse()
# cloned_mickey = mickey
# print(mickey is minnie, mickey is cloned_mickey)  # Imprime "False True".

# # 5. Una función sin parámetros llamada super() retorna l
# # a referencia a la superclase más cercana de la clase. 
# # Por ejemplo:

# class Mouse:
#     def __str__(self):
#         return "Mouse"


# class LabMouse(Mouse):
#     def __str__(self):
#         return "Laboratory " + super().__str__()


# doctor_mouse = LabMouse();
# print(doctor_mouse)  # Imprime "Laboratory Mouse".


# # 6. Los métodos, así como las variables de instancia y de clase 
# # definidas en una superclase son heredados automáticamente por sus subclases. 
# # Por ejemplo:

# class Mouse:
#     Population = 0
#     def __init__(self, name):
#         Mouse.Population += 1
#         self.name = name

#     def __str__(self):
#         return "Hola, mi nombre es " + self.name

# class LabMouse(Mouse):
#     pass

# professor_mouse = LabMouse("Profesor Mouse")
# print(professor_mouse, Mouse.Population)  # Imprime "Hola, mi nombre es Profesor Mouse 1"


# # 7. Para encontrar cualquier propiedad de objeto/clase, Python la busca dentro:

#     # Del objeto mismo.
#     # Todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
#     # Si existe más de una clase en una ruta de herencia en particular, Python las escanea de izquierda a derecha.
#     # Si lo mencionado anteriormente falla, la excepción AttributeError es generada.

# # 8. Si alguna de las subclases define un método, variable de clase o variable de instancia 
# # del mismo nombre que existe en la superclase, 
# # el nuevo nombre anula cualquiera de las instancias anteriores del nombre. Por ejemplo:

# class Mouse:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name

# class AncientMouse(Mouse):
#     def __str__(self):
#         return "Meum nomen est " + self.name

# mus = AncientMouse("Caesar")  # Imprime "Meum nomen est Caesar"
# print(mus)

######################
# Sección 3.5.1.23
######################

# # El siguiente fragmento de código se ha ejecutado con éxito:

# class Dog:
#     kennel = 0
#     def __init__(self, breed):
#         self.breed = breed
#         Dog.kennel += 1
#     def __str__(self):
#         return self.breed + " dice: ¡Guau!"


# class SheepDog(Dog):
#     def __str__(self):
#         return super().__str__() + " ¡No huyas, corderito!"


# class GuardDog(Dog):
#     def __str__(self):
#         return super().__str__() + " ¡Quédese donde está, intruso!"


# rocky = SheepDog("Collie")
# luna = GuardDog("Dobermann")


# # Ejercicio 1

# # ¿Cuál es el resultado esperado del siguiente código?

# print(rocky)
# print(luna)


# # Collie dice: ¡Guau! ¡No huyas, corderito!
# # Dobermann dice: ¡Guau! ¡Quédese donde está, intruso!



# # Ejercicio 2

# # ¿Cuál es el resultado esperado del siguiente código?

# print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
# print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))


# # True False
# # False True



# # Ejercicio 3

# # ¿Cuál es el resultado esperado del siguiente código?

# print(luna is luna, rocky is luna)
# print(rocky.kennel)


# # True False
# # 2



# # Ejercicio 4

# # Define una subclase de SheepDog llamada LowlandDog, y equipala con un método __str__() que anule un método heredado del mismo nombre. El nuevo método __str__() debe retornar la cadena "¡Guau! ¡No me gustan las montañas!".

# # class LowlandDog(SheepDog):
# # 	def __str__(self):
# # 		return Dog.__str__(self) + " ¡No me gustan las montañas"

######################
# Sección 3.6.1.1
######################

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         return None
#     else:
#         print("Todo salió bien")
#         return n

# print(reciprocal(2))
# print(reciprocal(0))

######################
# Sección 3.6.1.2
######################

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         n = None
#     else:
#         print("Todo salió bien")
#     finally:
#         print("Es momento de decir adiós")
#         return n


# print(reciprocal(2))
# print(reciprocal(0))

######################
# Sección 3.6.1.3
######################

# try:
#     i = int("¡Hola!")
# except Exception as e:
#     print(e)
#     print(e.__str__())
#     print(type(e).__name__)    
######################
# Sección 3.6.1.4
######################

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)


# print_exception_tree(BaseException)

######################
# Sección 3.6.1.5
######################

# def print_args(args):
#     lng = len(args)
#     if lng == 0:
#         print("")
#     elif lng == 1:
#         print(args[0])
#     else:
#         print(str(args))


# try:
#     raise Exception
# except Exception as e:
#     print(e, e.__str__(), sep=' : ' ,end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

# try:
#     raise Exception("mi", "excepción")
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

######################
# Sección 3.6.1.6
######################

# class MyZeroDivisionError(ZeroDivisionError):	
#     pass


# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("peores noticias")
#     else:		
#         raise ZeroDivisionError("malas noticias")


# for mode in [False, True]:
#     try:
#         do_the_division(mode)
#     except ZeroDivisionError:
#         print('División entre cero')

# for mode in [False, True]:
#     try:
#         do_the_division(mode)
#     except MyZeroDivisionError:
#         print('Mi división entre cero')
#     except ZeroDivisionError:
#         print('División entre cero original')

######################
# Sección 3.6.1.7
######################

# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         Exception.__init__(self, message)
#         self.pizza = pizza


# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         PizzaError._init__(self, pizza, message)
#         self.cheese = cheese

######################
# Sección 3.6.1.8
######################

# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         Exception.__init__(self, message)
#         self.pizza = pizza


# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         PizzaError.__init__(self, pizza, message)
#         self.cheese = cheese


# def make_pizza(pizza, cheese):
#     if pizza not in ['margherita', 'capricciosa', 'calzone']:
#         raise PizzaError(pizza, "no hay tal pizza en el menú")
#     if cheese > 100:
#         raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
#     print("¡Pizza lista!")

# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
#     try:
#         make_pizza(pz, ch)
#     except TooMuchCheeseError as tmce:
#         print(tmce, ':', tmce.cheese)
#     except PizzaError as pe:
#         print(pe, ':', pe.pizza)

######################
# Sección 3.6.1.9
######################

# 1. El bloque else: de la sentencia try se ejecuta 
# cuando no ha habido ninguna excepción durante la ejecución del try:.


# 2. El bloque finally: de la sentencia try es siempre executado.


# 3. La sintaxis except Exception_Name as exception_object: 
# te permite interceptar un objeto que contiene información 
# sobre una excepción pendiente. 
# La propiedad del objeto llamada args (una tupla) almacena 
# todos los argumentos pasados al constructor del objeto.


# 4. Las clases de excepciones pueden extenderse para enriquecerlas 
# con nuevas capacidades o para adoptar sus características a excepciones recién definidas.

# Por ejemplo:

# try:
#     assert __name__ == "__main__"
# except:
#     print("fallido", end=' ')
# else:
#     print("éxito", end=' ')
# finally:
#     print("terminado")

#########################################

# # El código da como salida: éxito terminado.

# # Ejercicio 1

# # ¿Cuál es el resultado esperado del siguiente código?

# import math

# try:
#     print(math.sqrt(9))
# except ValueError:
#     print("inf")
# else:
#     print("ok")


# # 3.0
# # ok



# # Ejercicio 2

# # ¿Cuál es el resultado esperado del siguiente código?

# import math

# try:
#     print(math.sqrt(-9))
# except ValueError:
#     print("inf")
# else:
#     print("ok")
# finally:
#     print("fin")


# # inf
# # fin



# # Ejercicio 3

# # ¿Cuál es el resultado esperado del siguiente código?

# import math

# class NewValueError(ValueError):
#     def __init__(self, name, color, state):
#         self.data = (name, color, state)

# try:
#     raise NewValueError("Advertencia enemiga", "Alerta roja", "Alta disponibilidad")
# except NewValueError as nve:
#     for arg in nve.args:
#         print(arg, end='! ')


# # Advertencia enemiga! Alerta roja! Alta disponibilidad! 

######################
# Sección 3.6.1.9
######################
