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

#######################################################################



