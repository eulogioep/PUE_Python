################################
# Sección 5.1.1.3
################################

# class Dog:
#     pass


# age = 10
# codes = [33, 92]
# dog = Dog()

# print(type(age))
# print(type(codes))
# print(type(dog))
# print(type(Dog))

##############

# for t in (int, list, type):
#     print(type(t))

################################
# Sección 5.1.1.4
################################

# class Dog:
#     pass

# dog = Dog()
# print('"dog" is an object of class named:', Dog.__name__)
# print()
# print('class "Dog" is an instance of:', Dog.__class__)
# print('instance "dog" is an instance of:', dog.__class__)
# print()
# print('class "Dog" is  ', Dog.__bases__)
# print()
# print('class "Dog" attributes:', Dog.__dict__)
# print('object "dog" attributes:', dog.__dict__)

################################
# Sección 5.1.1.5
################################

# for element in (1, 'a', True):
#     print(element, 'is', element.__class__, type(element))

################################
# Sección 5.1.1.6
################################

# Dog = type('Dog', (), {})

# print('The class name is:', Dog.__name__)
# print('The class is an instance of:', Dog.__class__)
# print('The class is based on:', Dog.__bases__)
# print('The class attributes are:', Dog.__dict__)

################################
# Sección 5.1.1.7
################################

# def funcion(self):
#     print('Guau Guau!!!')

# class Animal:
#     def comer(self):
#         print('A comeeer!')

# Perro = type('Perro', (Animal, ), {'edad':3, 'ladrar':funcion})

# print('El nombre de la clase es:', Perro.__name__)
# print('La clase es una instancia de:', Perro.__class__)
# print('Laq clase está basada en:', Perro.__bases__)
# print('Los atributos de la clase son:', Perro.__dict__)

# perrito = Perro()
# perrito.comer()
# perrito.ladrar()
# print(perrito.edad, 'años')

################################
# Sección 5.1.1.8
################################

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         obj = super().__new__(mcs, name, bases, dictionary)
#         obj.custom_attribute = 'Added by My_Meta'
#         return obj

# class My_Object(metaclass=My_Meta):
#     pass

# print(My_Object.__dict__)


################################
# Sección 5.1.1.9
################################

# def greetings(self):
#     print('Just a greeting function, but it could be something more serious like a check sum')

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if 'greetings' not in dictionary:
#             dictionary['greetings'] = greetings
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     def greetings(self):
#         print('We are ready to greet you!')

# myobj1 = My_Class1()
# myobj1.greetings()
# myobj2 = My_Class2()
# myobj2.greetings()


##################################
# Laboratorio de Sección 5.1.1.10
##################################


# import time

# def get_class_instantiation_time(self):
#     return self.class_instantiation_time

# class CleanCodeGuard(type):
#     classes_created = []

#     def __new__(mcs, name, bases, dictionary):
#         if 'get_class_instantiation_time' not in dictionary:
#             dictionary['get_class_instantiation_time'] = get_class_instantiation_time
#         obj = super().__new__(mcs, name, bases, dictionary)

#         obj.class_instantiation_time = time.time()
#         CleanCodeGuard.classes_created.append(name)
#         time.sleep(1)
#         return obj

# class My_Class1(metaclass=CleanCodeGuard):
#     pass

# class My_Class2(metaclass=CleanCodeGuard):
#     pass

# my_object1 = My_Class1()
# print(my_object1.get_class_instantiation_time())

# my_object2 = My_Class2()
# print(my_object2.get_class_instantiation_time())

# print(CleanCodeGuard.classes_created)
