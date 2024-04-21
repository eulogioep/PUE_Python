####### POO ###########

# # Ejemplo de clase

# class Persona:
#     pass     

# #############

# persona1 = Persona()

# persona2 = Persona()

# print(type(persona1))

#persona1 = persona2 # Como son objetos, funcionan como dos mandos que apuntan al mismo objeto

#####################################

# Pila con enfoque procedimental

# pila = []


# def push(elemento):
#     pila.append(elemento)


# def pop():
#     valor = pila[-1]
#     del pila[-1]
#     return valor


# push(3)
# push(2)
# push(1)

# print(pop())
# print(pop())
# print(pop())

# Introduce en orden, el 3,2,1 y despues expulsa en orden inverso. Como una pila

##########

# Pila con enfoque Orientado a Objetos

# class Stack: # Definiendo la clase de la pila.
#     def __init__(self): # Definiendo la función del constructor.
#         self.stack_list = []


# stack_object = Stack() # Instanciando el objeto. Cada objeto instanciado es único y tiene un id propio.
# print(len(stack_object.stack_list))

# Encapsulación. Si un atributo tiene __<nombre>, crea un atributo aparentemente privado
# class Stack:
#     def __init__(self):
#         self.__stack_list = []


# stack_object = Stack()
# print(len(stack_object.__stack_list))

# Pero si me quiero saltar la privacidad, utilizo el Name Mangling (Renombrar)
# print(stack_object1._Stack__stack_list)

######

# Paso 2

# class Stack:
#     def __init__(self):
#         self.__stack_list = []


#     def push(self, val):
#         self.__stack_list.append(val)


#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# ### clase ###

# stack_object = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())


#######
# Podemos crear todas las pilas que queramos

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


##################################################

# Nueva clase para manejar pilas

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


#### Ejemplo terminado ##############

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
# print(stack_object.get_sum())

# for i in range(5):
#     print(stack_object.pop())


########## Laboratorios ###########################################

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

#####################################

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
    

# ##################

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


############## Variables de instancia ################################

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

#------------------------------------#
# {'first': 1}
# {'first': 2, 'second': 3}
# {'first': 4, 'third': 5}
#------------------------------------#

############## Variables de clase (Estáticos en Java) #########################

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

#-------------------------------#
# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3
#-------------------------------#

################## Ejemplo con método interno #############################################

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


########### La vida interna de clases y objetos ##############################

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

########## Herencia Múltiple ####################################################

# class SuperOne:
#     pass


# class SuperTwo:
#     pass


# class Sub(SuperOne, SuperTwo):
#     pass


# def printBases(clase):
#     print('( ', end='')

#     for x in clase.__bases__:
#         print(x.__name__, end=' ')
#     print(')')


# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(Sub)


########### Método __str__ #################################################

# class Timer:
    
#     def __str__(self):
#         return "Esta es la representacion del objeto"
    
# print(Timer())

####################### Crear un temporizador ######################################

   
###################################################

# import os, time

# def limpiar_consola():

#     os.system('cls' if os.name == 'nt' else 'clear')


# class Timer:
#     def __init__(self, hora = 0, min = 0, seg = 0):
        
#         self.__horas = hora
#         self.__minutos = min
#         self.__segundos = seg

#     def two_digits(val):
#         return f'{val:02}'


#     def next_second(self):
        
#         self.__segundos += 1
#         if self.__segundos > 59:
#             self.__segundos = 0
#             self.__minutos += 1
#             if self.__minutos > 59:
#                 self.__minutos = 0
#                 self.__horas += 1
#                 if self.__horas > 23:
#                     self.__horas = 0
        

#     def prev_second(self):
        
#         self.__segundos -= 1
#         if self.__segundos < 0:
#             self.__segundos = 59
#             self.__minutos -= 1
#             if self.__minutos < 0:
#                 self.__minutos = 59
#                 self.__horas -= 1
#                 if self.__horas < 0:
#                     self.__horas = 23


    
#     def __str__(self):
        
#         return Timer.two_digits(self.__horas) + ":" + \
#                Timer.two_digits(self.__minutos) + ":" + \
#                Timer.two_digits(self.__segundos)

        # Otra alternativa
        # return str(self.__horas).zfill(2) + ":" + \
        #                 str(self.__minutos).zfill(2) + ":" + \
        #                 str(self.__segundos).zfill(2)


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)

# ##### Temporizador #####

# timer = Timer(23, 59, 59)

# while True:
#     limpiar_consola()
#     timer.next_second()
#     print(timer)
#     time.sleep(1)
    
############################# Manipulador de dias de la semana ###################################

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
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")


    
########################## Distancia entre dos puntos ######################################################

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


# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))


################################ Triangulo ####################################

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


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         per = 0
#         for i in range(3):
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#         return per


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())


##################### Herencia #########################################################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)


#################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' en ' + self.galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)

########### issubclass() ###################

# En Python, una clase, siempre será considerada una subclase de si misma.

# class S1:
#     pass
# class S2(S1):
#     pass
# class S3(S2):
#     pass


# for cls1 in [S1, S2, S3]:
#     for cls2 in [S1, S2, S3]:
#         print("\n¿La clase", cls1.__name__, "es una subclase de", cls2.__name__, "? ", end ='')
#         print(issubclass(cls1, cls2), end="\t")
#     print()

########## isinstance() ####################

# class S1:
#     def __str__(self) -> str:
#         return "o1"
# class S2(S1):
#     def __str__(self) -> str:
#         return "o2"
# class S3(S2):
#     def __str__(self) -> str:
#         return "o3"

# o1 = S1()
# o2 = S2()
# o3 = S3()

# for obj in [o1,o2,o3]:
#     for cls in [S1,S2,S3]:
#         print("\n¿El objeto", obj, "es una instancia de", cls.__name__, "? ", end ='')
#         print(isinstance(obj, cls), end="\t")

#     print()

########## Operador is ##################

# El operador is verifica si dos variables, en este caso (object_one y object_two) se refieren al mismo objeto.

# No olvides que las variables no almacenan los objetos en sí, sino solo los identificadores que 
# apuntan a la memoria interna de Python.


# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"

# print(string_1 == string_2, string_1 is string_2)

    
#### Cómo Python encuentra propiedades y métodos ############

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."


# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)


# obj = Sub("Andy")

# print(obj)

####### Herencia Múltiple ##########
# En la herencia múltiple, tiene prioridad la primera clase indicada si tiene métodos con el mismo nombre.
# Python soporta la Herencia múltiple pero se recomienda no utilizarla.

# La herencia múltiple viola el principio de responsabilidad única (mas detalles aquí: 
#     https://en.wikipedia.org/wiki/Single_responsibility_principle) 
# ya que forma una nueva clase de dos (o más) clases que no saben nada una de la otra.

# Sugerimos encarecidamente la herencia múltiple como la última de todas las posibles soluciones: 
#     si realmente necesitas las diferentes funcionalidades que ofrecen las diferentes clases, 
#     la composición puede ser una mejor alternativa.

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

###############

# class SuperA:
#     var_a = "Valor de var_a en SuperA"
#     def fun_a(self):
#         return "Ejecutando fun_a() en SuperA"


# class SuperB:
#     var_a = "Valor de var_a en SuperB"
#     def fun_a(self):
#         return "Ejecutando fun_a() en SuperB"

# class Sub(SuperB, SuperA): #En la herencia múltiple, tiene prioridad la primera clase indicada si tiene métodos con el mismo nombre.
#     pass

# ####################
# obj = Sub()

# print(obj.var_a, " - ",  obj.fun_a())


##################

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

###############

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


# class Sub(Left, Right):  #En la herencia múltiple, tiene prioridad la primera clase indicada si tiene métodos con el mismo nombre.
#     pass


# obj = Sub()

# print(obj.var, obj.var_left, obj.var_right, obj.fun())


####### Jerarquia de clases ############

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

#################

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

########

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

############## Herencia del diamante ####################

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

######################## Más información sbre excepciones ##########################################

######### En excepciones también se puede utilizar -else- #################

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


###########

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         n = None
#     else:
#         print("Todo salió bien")
#     finally: # Siempre se ejecuta
#         print("Es momento de decir adiós")
#         return n


# print(reciprocal(2))
# print(reciprocal(0))

############# Las excepciones son clasese que dan lugar a Objetos en tiempo de ejecución ########

# try:
#     i = int("¡Hola!")
# except Exception as e:
#     print(e)
#     print(e.__str__())

############### Función recursiva que recorre toda la clase excepciones ########

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)


# print_exception_tree(BaseException)

########### Anatomia detallada de las excepciones ##########

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

############## Crear mi propia excepción ##########

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



#################################################################################################



