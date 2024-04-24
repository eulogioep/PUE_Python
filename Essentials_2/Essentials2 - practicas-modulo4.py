######################
# Sección 4.1.1.1
######################

# for i in range(5):
#     print(i)

######################
# Sección 4.1.1.2
######################

# class Fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("__iter__")
#         return self

#     def __next__(self):
#         print("__next__")		
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret


# for i in Fib(10):
#     print(i)


########################
# Ejemplo generador
########################

# class Generador:
#     def __init__(self, limite):
        
#         print("__init__")
        
#         self.__limite = limite
#         self.__valor_actual = 0

#     def __iter__(self):
        
#         print("__iter__")
        
#         return self

#     def __next__(self):
        
#         print("__next__")		
        
#         self.__valor_actual += 1
        
#         if self.__valor_actual > self.__limite:
#             raise StopIteration
            
#         return self.__valor_actual


# for numero in Generador(10):
#     print(numero)

######################
# Sección 4.1.1.3
######################

# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("Fib iter")
#         return self

#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret


# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)

#     def __iter__(self):
#         print("Class iter")
#         return self.__iter


# object = Class(8)

# for i in object:
#     print(i)

##########################################

# class Generador:
#     def __init__(self, limite):
        
#         print("__init__")
        
#         self.__limite = limite
#         self.__valor_actual = 0

#     def __iter__(self):
        
#         print("__iter__ en Generador")
        
#         return self

#     def __next__(self):
        
#         print("__next__")		
        
#         self.__valor_actual += 1
        
#         if self.__valor_actual > self.__limite:
#             raise StopIteration
            
#         return self.__valor_actual


# class Clase1:
#     def __init__(self, limite):
#         print('constructor')
#         self.__x = Generador(limite)
        
#     def __iter__(self):
#         print("__iter__ en Clase1")
#         return self.__x

# #######################

# objeto = Clase1(8)      # se invoca a __init__()

# for i in Clase1(8)._Clase1__x:
#     print(i)

# for i in objeto:     # __iter__() solo se invoca si lo uso aquí
#     print(i)

######################
# Sección 4.1.1.4
######################

# def fun(n):
#     for i in range(n):
#         return i
    
# print(fun(10))

######################

# def fun(n):
#     for i in range(n):
#         yield i
        
# for i in fun(10):
#     print(i)

######################
# Sección 4.1.1.5
######################

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# generador = powers_of_2(10)

# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())
# print(generador.__next__())

# for v in powers_of_2(8):
#     print(v)

##################################
# Listas por comprensión
##################################

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
        
# t = [x for x in powers_of_2(5)]
# print(t)

##################################
# Función list()
##################################

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
        
# t = list(powers_of_2(3))
# print(t)

##################################
# Operador in
##################################

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# for i in range(20):
#     if i in powers_of_2(4):
#         print(i)

###################################
# Generador Fibonacci
###################################

# def fibonacci(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n

# fibs = list(fibonacci(10))
# print(fibs)


#####################################################
# Ejemplos yield para retirar elementos de una lista
#####################################################

# Ramón

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def quitar_pares_yield(lista):    
#     for n in lista:
#         if n  % 2 != 0:
            
#             yield n

# for x in quitar_pares_yield(lista):
#     print(x)

# Jose Antonio

# pila = [1,2,3,4,5]

# def extraer_elemento(lista_pila:list):
#     for n in range(len(lista_pila)):
#         yield lista_pila[len(pila) -n -1]

# for elemento in extraer_elemento(pila):
#     print(elemento)

# Jennyfer

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)
#         print(f"Elemento '{item}' agregado a la pila: {self.items}")

#     def __iter__(self):
#         # Imprimir la lista completa antes de empezar a retirar elementos
#         print("Lista completa antes de retirar elementos:", self.items)
#         # Utilizar yield para devolver los elementos uno por uno
#         while self.items:
#             yield self.items.pop()
#             print(f"Elemento '{item}' retirado de la pila: {self.items}")

# # Ejemplo de uso:
# stack = Stack()

# for i in range(1,10):
#     stack.push(i)

# # Utilizar un bucle for para retirar los elementos de la pila e imprimirlos
# print("\nElementos retirados de la pila:")
# for item in stack:
#     print(item)


######################
# Sección 4.1.1.6
######################

# list_1 = []

# for ex in range(6):
#     list_1.append(10 ** ex)
    

# list_2 = [10 ** ex for ex in range(6)]

# print(list_1)
# print(list_2)

######################
# Sección 4.1.1.7
######################

# the_list = []

# for x in range(10):
#     the_list.append(1 if x % 2 == 0 else 0)

# print(the_list)

######################
# Sección 4.1.1.8
######################

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

# print(the_list)

################################
# Listas frente a generadores
################################

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

# print(the_list)

# for v in the_list:
#     print(v, end=" ")
# print()

# print(the_generator.__next__())

# for v in the_generator:
#     print(v, end=" ")
# print()

######################
# Sección 4.1.1.9
######################

# dos      = lambda: 2
# cuadrado = lambda x: x * x
# potencia = lambda x, y: x ** y

# for numero in range(10):
#     print('Cuadrado de',numero,'=' , cuadrado(numero), end=" ")
#     print('Potencia de',numero, 'elevado a',numero,  '=', potencia(numero, numero))

######################
# Sección 4.1.1.10
######################

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')

# # polinomio
# # f(x) = 2x2 - 4x + 2

# def poly(x):
#     return 2 * x**2 - 4 * x + 2


# print_function([x for x in range(-2, 3)], poly)

###########################

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')

# print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

######################
# Sección 4.1.1.11
######################

# La función map() aplica la función pasada por su primer argumento 
# a todos los elementos de su segundo argumento y devuelve un iterador 
# que entrega todos los resultados de funciones subsequentes.

# list_1 = [x for x in range(5)]

# # podemos convertir el resultado en una lista
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)


# # pero también podemos utilizarlo directamente en un bucle for
# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()

######################
# Sección 4.1.1.12
######################

# filter()

# Espera el mismo tipo de argumentos que map(), pero hace algo diferente: 
# filtra su segundo argumento mientras es guiado por direcciones 
# que fluyen desde la función especificada en el primer argumento 
# (la función se invoca para cada elemento de la lista, al igual que en map())

# # Los elementos que devuelven True de la función pasan el filtro, los otros son rechazados.

# from random import seed, randint

# seed()
# data = [randint(-10,10) for x in range(5)]

# # filtar pares y mayores que cero

# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# print(data)
# print(filtered)

######################
# Sección 4.1.1.13
######################

# def outer(par):
#     loc = par

#     print('Ejecutando función outer que devuelve inner()')

#     def inner():
#         print('Ejecutando función inner')
#         return loc
    
#     return inner

# var = 1
# fun = outer(var)
# print('Resultado:', fun())

######################
# Sección 4.1.1.14
######################

# Un cierre se debe invocar exactamente de la misma manera en que se ha declarado.

# def ejemplo_cierre(parametro):
#     numero = parametro

#     def potencia(p):
#         return p ** numero
#     return potencia


# cuadrado = ejemplo_cierre(2)
# cubo = ejemplo_cierre(3)

# for numero in range(5):
#     print(numero, cuadrado(numero), cubo(numero))

###########################
# Fábrica de funciones
###########################

# def fabrica_funciones(potencia, limite):
#     __potencia = potencia
#     __limite = limite

#     def fun_lista_potencias():
#         return [numero ** __potencia for numero in range(__limite)]

#     def fun_generador_potencias():
#         return (numero ** __potencia for numero in range(__limite))

#     return fun_lista_potencias if __limite < 100 else fun_generador_potencias


# cuadrados = fabrica_funciones(potencia=2, limite=10)

# lista_cuadrados = cuadrados()

# print(lista_cuadrados)    

# cubos = fabrica_funciones(potencia=3, limite=10)    

# lista_cubos = cubos()

# print(lista_cubos)    

# ########################################################
# cuadrados = fabrica_funciones(potencia=2, limite=100)

# for valor in cuadrados():
#     print(valor, end =' ')

# cubos = fabrica_funciones(potencia=3, limite=100)    
# for valor in cubos():
#     print(valor, end =' ')

##############################
# Resumen de Sección 4.1.1.15
##############################

# # 1. Un iterator es un objeto de una clase que proporciona al menos dos métodos (sin contar el constructor):
# # __iter__() se invoca una vez cuando se crea el iterador y devuelve el propio objeto del iterador.
# # __next__() se invoca para proporcionar el valor de la siguiente iteración y genera la excepción StopIteration 
# # cuando la iteración llega a su fin.

# # 2. La sentencia yield solo puede ser utilizada dentro de funciones. 
# # La sentencia yield suspende la ejecución de la función y hace que la función 
# # devuelva el argumento de yield como resultado. 
# # Esta función no puede invocarse de forma regular, su único propósito es ser utilizada como un generador 
# # (es decir, en un contexto que requiera una serie de valores, como un bucle for).


# # 3. Una expresión condicional es una expresión construida usando el operador if-else. 
# # Por ejemplo:

# print(True if 0 >= 0 else False)


# # Da como salida: True.


# # 4. Una lista por comprensión se convierte en un generador cuando se emplea dentro de paréntesis 
# # (usado entre corchetes, produce una lista regular). 
# # Por ejemplo:

# for x in (el * 2 for el in range(5)):
#     print(x)

# # Da como salida: 02468.


# # 4. Una función lambda es una herramienta para crear funciones anónimas. 
# # Por ejemplo:

# def foo(x, f):
#     return f(x)

# print(foo(9, lambda x: x ** 0.5))


# # Da como salida: 3.0.


# # 5. La función map(fun, list) crea una copia del argumento list, 
# # y aplica la función fun a todos sus elementos, retornando un generador 
# # que proporciona el nuevo contenido de la lista elemento por elemento. 
# # Por ejemplo:

# short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
# new_list = list(map(lambda s: s.title(), short_list))
# print(new_list)


# # Da como salida: ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].


# # 6. La función filter(fun, list) crea una copia de aquellos elementos de list, 
# # lo cual hace que la función fun retorne True. 
# # El resultado de la función es un generador proporcionando el nuevo contenido de la lista elemento por elemento. 
# # Por ejemplo:

# short_list = [1, "Python", -1, "Monty"]
# new_list = list(filter(lambda s: isinstance(s, str), short_list))
# print(new_list)


# # Da como salida: ['Python', 'Monty'].


# # 7. Un cierre es una técnica que permite almacenar valores a pesar de que el contexto 
# # en el que han sido creados no existe más. 
# # Por ejemplo:

# def tag(tg):
#     tg2 = tg
#     tg2 = tg[0] + '/' + tg[1:]

#     def inner(str):
#         return tg + str + tg2
#     return inner


# b_tag = tag('<b>')
# print(b_tag('Monty Python'))


# # Da como salida: <b>Monty Python</b>


# # Ejercicio 1

# # ¿Cuál es el resultado esperado del siguiente código?

# class Vowels:
#     def __init__(self):
#         self.vow = "aeiouy "  # Sí, sabemos que y no siempre se considera una vocal.
#         self.pos = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.pos == len(self.vow):
#             raise StopIteration
#         self.pos += 1
#         return self.vow[self.pos - 1]


# vowels = Vowels()
# for v in vowels:
#     print(v, end=' ')
    
# # a e i o u y



# # Ejercicio 2

# # Escribe una función lambda, estableciendo a 1 su argumento entero, y aplícalo a la función map() para producir la cadena 1 3 3 5 en la consola.

# # any_list = [1, 2, 3, 4]
# # even_list = # Completar las líneas aquí.
# # print(even_list)

# any_list = [1, 2, 3, 4]
# even_list = list(map(lambda n: n | 1, any_list))
# print(even_list)


# # Ejercicio 3

# # ¿Cuál es el resultado esperado del siguiente código?

# def replace_spaces(replacement='*'):
#     def new_replacement(text):
#         return text.replace(' ', replacement)
#     return new_replacement


# stars = replace_spaces()
# print(stars("And Now for Something Completely Different"))

# # And*Now*for*Something*Completely*Different

##############################
# Sección 4.2.1.9
##############################

# try:
#     stream = open("./quijote-reducido.txt", "rt")
#     # El procesamiento va aquí.
#     stream.close()
# except Exception as exc:
#     print("No se puede abrir el archivo:", exc)

##############################
# Sección 4.2.1.11
##############################

## Símbolos estándar del sistema errno
## https://docs.python.org/es/3/library/errno.html

# import errno

# try:
#     s = open("./quijote-reducido.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("El archivo no existe.")
#     elif exc.errno == errno.EMFILE:
#         print("Demasiados archivos abiertos.")
#     else:
#         print("El numero del error es:", exc.errno)



# from os import strerror

# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     print("El archivo no pudo ser abierto:", strerror(exc.errno))

##############################
# Resumen de Sección 4.2.1.12
##############################

# # Ejercicio 1

# # ¿Cómo se codifica el valor del argumento modo de la función open() si se va a crear un nuevo archivo de texto?

# # "wt" o "w"

# # Ejercicio 2

# # ¿Cuál es el significado del valor representado por errno.EACESS?

# # Permiso denegado: no se permite acceder al contenido del archivo.

# # Ejercicio 3

# # ¿Cuál es la salida esperada del siguiente código, asumiendo que el archivo llamado file no existe?

# import errno

# try:
#     stream = open("file", "rb")
#     print("existe")
#     stream.close()
# except IOError as error:
#     if error.errno == errno.ENOENT:
#         print("ausente")
#     else:
#         print("desconocido")

# ausente

##############################
# Sección 4.3.1.1
##############################

# # Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
# stream = open("tzop.txt", "rt", encoding = "utf-8")

# # Se imprime el contenido del archivo:
# print(stream.read()) 

##############################
# Sección 4.3.1.2
##############################

##############################
# Tamaño del archivo en bytes
##############################

# import os
# print(os.path.getsize("text.txt"), 'bytes')

##############################

# from os import strerror

# try:
#     counter = 0
#     stream = open('text.txt', "rt")
#     char = stream.read(1)
#     while char != '':
#         print(char, end='')
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.3
##############################

# from os import strerror

# try:
#     counter = 0
#     stream = open('text.txt', "rt")
#     content = stream.read() # cargar el fichero completo en memoria
#     for char in content:
#         print(char, end='')
#         counter += 1
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

###############################
# Rama else y bloque finally
###############################

# from os import strerror

# try:
#     counter = 0
#     stream = open('text.txt', "rt")
    
# except Exception as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
# else:
#     content = stream.read() # cargar el fichero completo en memoria
#     for char in content:
#         print(char, end='')
#         counter += 1
# finally:
#     if stream in locals(): # Si la variable stream existe
#         stream.close()
#         print("\n\nCaracteres en el archivo:", counter)

##############################
# Sección 4.3.1.4
##############################

# from os import strerror

# try:
#     character_counter = line_counter = 0
#     stream = open('text.txt', 'rt')
#     line = stream.readline()
#     while line != '':
#         line_counter += 1
#         for char in line:
#             print(char, end='')
#             character_counter += 1
#         line = stream.readline()
#     stream.close()
#     print("\n\nCaracteres en el archivo:", character_counter)
#     print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.5
##############################

# from os import strerror

# try:
#     character_counter = line_counter = 0
#     stream = open('text.txt', 'rt')
#     lines = stream.readlines(20)
#     while len(lines) != 0:
#         for line in lines:
#             line_counter += 1
#             for char in line:
#                 print(char, end='')
#                 character_counter += 1
#         lines = stream.readlines(10)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", character_counter)
#     print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.6
##############################

# from os import strerror

# try:
# 	character_counter = line_counter = 0
    
# 	for line in open('text.txt', 'rt'): # iterable!!
# 		line_counter += 1
# 		for char in line:
# 			print(char, end='')
# 			character_counter += 1
# 	print("\n\nCaracteres en el archivo: ", character_counter)
# 	print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))


##############################
# Sección 4.3.1.7
##############################

# from os import strerror

# try:
# 	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
# 	for i in range(10):
# 		s = "línea #" + str(i+1) + "\n"
# 		for char in s:
# 			file.write(char)
# 	file.close()
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.8
##############################

# import sys

# from os import strerror

# try:
#     file = open('newtext.txt', 'wt')
#     for i in range(10):
#         file.write("línea #" + str(i+1) + "\n")
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
#     # sys.stderr.write("Mensaje de Error:" + e.__str__())

##############################
# Sección 4.3.1.9
##############################

# data = bytearray(10)
# print(data)

##############################
# Sección 4.3.1.10
##############################

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 100 - i

# # print(data)

# for b in data:
#     print('binario:', bin(b), end = ' - ')
#     print('hexadecimal:', hex(b), end = ' - ')
#     print('octal:', oct(b), end = ' - ')
#     print('decimal:', int(b))

##############################
# Sección 4.3.1.11
##############################

# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
    
# ##################

# from os import strerror

# data = bytearray(10)

# try:
#     binary_file = open('file.bin', 'rb')
#     binary_file.readinto(data)
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.12
##############################

# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# #########################################

# from os import strerror

# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read())
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.13
##############################

# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
    
# ################################

# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read(5))
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

##############################
# Sección 4.3.1.14
##############################

# from os import strerror

# source_file_name = input("Ingresa el nombre del archivo fuente: ")
# try:
#     source_file = open(source_file_name, 'rb')
# except IOError as e:
#     print("No se puede abrir archivo fuente: ", strerror(e.errno))
#     exit(e.errno)	

# destination_file_name = input("Ingresa el nombre del archivo destino: ")

# try:
#     destination_file = open(destination_file_name, 'wb')
# except Exception as e:
#     print("No se puede crear el archivo de destino:", strerror(e.errno))
#     source_file.close()
#     exit(e.errno)	

# buffer = bytearray(65536)
# total  = 0
# try:
#     readin = source_file.readinto(buffer)
#     while readin > 0:
#         written = destination_file.write(buffer[:readin])
#         total += written
#         readin = source_file.readinto(buffer)
# except IOError as e:
#     print("No se puede crear el archivo de destino: ", strerror(e.errno))
#     exit(e.errno)	
    
# print(total,'byte(s) escritos con éxito')
# source_file.close()
# destination_file.close()

###############################
# Laboratorio Sección 4.3.1.15
###############################

# from os import strerror

# # Inicializa 26 contadores para cada letra latina.
# # Nota: hemos usado una comprensión para esto.
# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# print(counters)

# file_name = input("Ingresa el nombre del archivo a analizar: ")
# try:
#     file = open(file_name, "rt")
#     for line in file:
#         for char in line:
#             # Si es una letra...
#             if char.isalpha():
#                 # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
#                 counters[char.lower()] += 1
#     file.close()
#     # Demos salida a los contadores.
#     for char in counters.keys():
#         c = counters[char]
#         if c > 0:
#             print(char, '->', c)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))

###############################
# Laboratorio Sección 4.3.1.16
###############################

# from os import strerror

# counters = {chr(punto_codigo): 0 for punto_codigo in range(ord('a'), ord('z') + 1)}
# file_name = input("Ingresa el nombre del archivo a analizar: ")
# try:
#     file = open(file_name, "rt")
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 counters[char.lower()] += 1
#     file.close()
#     file = open(file_name + '.hist', 'wt')
#     # Nota: hemos utilizado una lambda para acceder a los elementos del directorio 
#     # y se ha establecido reverse a True para obtener un orden válido.
#     for clave, valor in sorted(counters.items(), key=lambda tupla: tupla[1], reverse=True):
#         if valor > 0:
#             file.write(clave + ' -> ' + str(valor) + '\n')
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))


# alternativa con mayusculas y minusculas diferenciadas y con funcion generadora

# def mi_generador():
#     for i in range(65,123):
#         if i > 90 and i < 97:
#             continue
#         else:
#             yield chr(i)

# def llenar_abecedario():

#     abecedario = {caracter: 0 for caracter in mi_generador()}

#     # abecedario = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
#     # mayusculas = {chr(ch): 0 for ch in range(ord('A'), ord('Z') + 1)}

#     # abecedario.update(mayusculas)

#     # for ch in range(97, 123): # Rango correcto para minúsculas
#     #     abecedario[chr(ch)] = 0
#     # for i in range(65, 91):  # Rango correcto para mayúsculas
#     #     abecedario[chr(i)] = 0
#     return abecedario

# # Llenar el diccionario con el abecedario y contador asociado a cero
# abecedario = llenar_abecedario()

# print(abecedario)

# archivo = input("Introduce el nombre del archivo: ")

# try:
#     stream = open(archivo, "rt")
#     line = stream.readline() 
#     while line != '':
#         contador = 0
#         for char in line:
#             if char in abecedario:
#                 contador +=1
#                 abecedario[char] = contador
#         line = stream.readline()
#     stream.close()

# except Exception as exc:
#     print("no se puede leer el archivo: ", exc)

# for clave, valor in sorted(abecedario.items(), key=lambda item: item[1],reverse=True):
#     if valor != 0:
#         print('{:<5} {}'.format(clave, valor))
###############################
# Laboratorio Sección 4.3.1.17
###############################

# # Una clase de la excepción base para nuestro código:
# class StudentsDataException(Exception):
#     pass


# # Una excepción para líneas erróneas:
# class WrongLine(StudentsDataException):
#     def __init__(self, line_number, line_string):
#         super().__init__(self)
#         self.line_number = line_number
#         self.line_string = line_string


# # Una excepción para un archivo vacío.
# class FileEmpty(StudentsDataException):
#     def __init__(self):
#         super().__init__(self)


# from os import strerror

# # Un diccionario para los datos de los estudiantes:
# data = { }

# file_name = input("Ingresa el nombre del archivo de datos del estudiante: ")
# line_number = 1
# try:
#     f = open(file_name, "rt")
#     # Leer el archivo completo en la lista.
#     lines = f.readlines()
#     f.close()
#     # ¿El archivo está vacío?
#     if len(lines) == 0:
#         raise FileEmpty()
#     # Escanee el archivo línea por línea.
#     for i in range(len(lines)):
#         # Obtener la línea n.
#         line = lines[i]
#         # Divídirlo en columnas.
#         columns = line.split()
#         # Debe haber 3 columnas, ¿están ahí?
#         if len(columns) != 3:
#             raise WrongLine(i + 1, line)
#         # Construye una clave a partir del nombre y apellido del estudiante.
#         student = columns[0] + ' ' + columns[1]
#         # Obtener puntos.
#         try:
#             points = float(columns[2])
#         except ValueError:
#             raise WrongLine(i + 1, line)
#         # Actualizar diccionario.
#         try:
#             data[student] += points
#         except KeyError:
#             data[student] = points
#     # Imprimir resultados.
#     for student in sorted(data.keys()):
#         print(student,'\t', data[student])

# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))
# except WrongLine as e:
#     print("Línea incorrecta #" + str(e.line_number) + " en el archivo fuente:" + e.line_string)
# except FileEmpty:
#     print("Archivo fuente vacío")

###############################
# Resumen de Sección 4.3.1.18
###############################

# 1.Para leer el contenido de un archivo, se pueden utilizar los siguientes métodos:

# read(number): 
#     lee el número de carácteres/bytes del archivo y los retorna como una cadena, es capaz de leer todo el archivo a la vez.
# readline(): 
#     lee una sola línea del archivo de texto.
# readlines(number): 
#     lee el número de líneas del archivo de texto; es capaz de leer todas las líneas a la vez.
# readinto(bytearray): 
#     lee los bytes del archivo y llena el bytearray con ellos.

# 2. Para escribir contenido nuevo en un archivo, se pueden utilizar los siguientes métodos:

# write(string): 
#     escribe una cadena a un archivo de texto.
# write(bytearray): 
#     escribe todos los bytes de un bytearray a un archivo.

# 3. El método open() devuelve un objeto iterable que se puede usar para recorrer todas las líneas 
# del archivo dentro de un bucle for. 
# Por ejemplo:

# for line in open("file", "rt"):
#     print(line, end='')


# El código copia el contenido del archivo a la consola, línea por línea. 
# Nota: el stream se cierra automáticamente cuando llega al final del archivo.

# Ejercicio 1

# ¿Qué se espera del método readlines() cuando el stream está asociado con un archivo vacío?

# Una lista vacía (una lista de longitud cero).


# Ejercicio 2

# ¿Qué se pretende hacer con el siguiente código?

# for line in open("file", "rt"):
#     for char in line:
#         if char.lower() not in "aeiouy ":
#             print(char, end='')

# Copia el contenido del archivo file hacia la consola, ignorando las vocales.

# Ejercicio 3

# Vas a procesar un mapa de bits almacenado en un archivo llamado image.png y 
# quieres leer su contenido como un todo en una variable bytearray llamada image. 
# Agrega una línea al siguiente código para lograr este objetivo.

# try:
#     stream = open("image.png", "rb")
#     # Inserta una línea aquí.
#     image = bytearray(stream.read())
#     stream.close()
# except IOError:
#     print("fallido")
# else:
#     print("exitoso")

##################
# Sección 4.4.1.2
##################

# import os
# print(os.uname())

# for (clave, valor) in os.uname():
#     print(valor)

# import os
# print('name:', os.name)

## convertir uname en diccionario

# attributes = ['name', 'nodename', 'release', 'version', 'root']
# d = {attr : value for attr,value in zip(attributes, os.uname())}
# print(d)


##################
# Sección 4.4.1.3
##################

# import os

# os.mkdir("my_first_directory")
# print(os.listdir())

##################
# Sección 4.4.1.4
##################

# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.listdir())

##################
# Sección 4.4.1.5
##################

# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())

##################
# Sección 4.4.1.6
##################

# import os

# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())


# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())

# for elem in os.listdir():
#     print(elem)


###########################

# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())

##################
# Sección 4.4.1.7
##################

# import os

# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)

##############################
# Laboratorio Sección 4.4.1.8
##############################

# import os

# class BuscadorDirectorios:
#     def buscar(self, ruta, directorio_a_buscar):
#         try:
#             # cambiar el directorio de trabajo actual
#             os.chdir(ruta)
#         except OSError:
#             # No procesa un archivo que no es un directorio.
#             return

#         # Saber en qué directorio estamos actualmente
#         directorio_actual = os.getcwd()
        
#         # recorrer el directorio actual
#         for entrada_actual in os.listdir(directorio_actual):

#             # si encontramos una coincidencia, imprimirla
#             if entrada_actual == directorio_a_buscar:
#                 print(directorio_actual + "/" + directorio_a_buscar)
                
#             # Llamada recursiva a find() para buscar en subdirectorios
#             self.buscar(directorio_actual + "/" + entrada_actual, directorio_a_buscar)

# buscador_directorios = BuscadorDirectorios()
# buscador_directorios.buscar("./tree", "python")

###############################################

# import os

# def find(path, directory):
#     for root, dirs, files in os.walk(path):
#         if directory in dirs:
#             print(os.path.join(root, directory))

# path = "./tree"
# directory = "python"
# find(path, directory)

###############################################

# import os

# class DirectorySearcher:
#     def find(self, path, dir):
#         try:
#             os.chdir(path)
#         except OSError:
#             # No procesa un archivo que no es un directorio.
#             return

#         current_dir = os.getcwd()
#         for entry in os.listdir("."):
#             if entry == dir:
#                 print(os.getcwd() + "/" + dir)
#             self.find(current_dir + "/" + entry, dir)


# directory_searcher = DirectorySearcher()
# directory_searcher.find("./tree", "python")

##############################
# Sección 4.5.1.2
##############################

# from datetime import date

# today = date.today()

# print("Hoy:", today)
# print("Año:", today.year)
# print("Mes:", today.month)
# print("Día:", today.day)

# from datetime import date

# my_date = date(2019, 11, 4)
# print(my_date)

##############################
# Sección 4.5.1.3
##############################

# from datetime import date
# import time

# timestamp = time.time()
# print("Marca de tiempo (timestamp) :", timestamp)

# d = date.fromtimestamp(timestamp)
# print("Fecha:", d)

##############################
# Sección 4.5.1.4
##############################

# from datetime import date

# d = date.fromisoformat('2019-11-04')
# print(d)

##############################
# Sección 4.5.1.5
##############################

# from datetime import date

# d = date(1991, 2, 5)
# print(d)

# d = d.replace(year=1992, month=1, day=16)
# print(d)

##############################
# Sección 4.5.1.6
##############################

# from datetime import date

# d = date(2019, 11, 4)
# print(d.weekday())

# from datetime import date

# d = date(2019, 11, 4)
# print(d.isoweekday())

##############################
# Franjas horarias
# import pytz as tz
# import datetime as dt

# berlin = tz.timezone("Europe/Berlin")
# fecha1 = dt.datetime(2017, 8, 9, 10, 10, 10)
# fecha2 = dt.datetime(2017, 8, 9, 10, 10, 10, tzinfo=berlin)
# fecha3 = dt.datetime(2017, 8, 9, 10, 10, 10).replace(tzinfo=berlin)
# fecha4 = dt.datetime(2017, 8, 9, 10, 10, 10, tzinfo=tz.UTC)

# print(fecha1)
# print(fecha2)
# print(fecha3)
# print(fecha4)
##############################
# Sección 4.5.1.7
##############################

# from datetime import time

# t = time(14, 53, 20, 1)

# print("Tiempo:", t)
# print("Hora:", t.hour)
# print("Minuto:", t.minute)
# print("Segundo:", t.second)
# print("Microsegundo:", t.microsecond)

##############################
# Sección 4.5.1.8
##############################

# import time

# class Student:
#     def take_nap(self, seconds):
#         print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
#         time.sleep(seconds)
#         print("¡Dormí bien! ¡Me siento genial!")

# student = Student()
# student.take_nap(5)

##############################
# Sección 4.5.1.9
##############################

# import time

# timestamp = 1572879180
# print(time.ctime(timestamp))

# import time
# print(time.ctime())

##############################
# Sección 4.5.1.10
##############################

# # time.struct_time:
# #     tm_year   # Especifica el año.
# #     tm_mon    # Especifica el mes (valor de 1 a 12)
# #     tm_mday   # Especifica el día del mes (valor de 1 a 31)
# #     tm_hour   # Especifica la hora (valor de 0 a 23)
# #     tm_min    # Especifica el minuto (valor de 0 a 59)
# #     tm_sec    # Especifica el segundo (valor de 0 a 61)
# #     tm_wday   # Especifica el día de la semana (valor de 0 a 6)
# #     tm_yday   # Especifica el día del año (valor de 1 a 366)
# #     tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
# #     tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
# #     tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)

# import time

# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))

##############################
# Sección 4.5.1.11
##############################

# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

##############################
# Sección 4.5.1.12
##############################

# from datetime import datetime

# dt = datetime(2019, 11, 4, 14, 53)

# print("Fecha y Hora:", dt)
# print("Fecha:", dt.date())
# print("Hora:", dt.time())

##############################
# Sección 4.5.1.13
##############################

# from datetime import datetime

# print("hoy:", datetime.today())
# print("ahora:", datetime.now())
# print("utc_ahora:", datetime.utcnow())

##############################
# Sección 4.5.1.14
##############################

# from datetime import datetime

# dt = datetime(2020, 10, 4, 14, 55)
# print("Marca de tiempo:", dt.timestamp())

##############################
# Sección 4.5.1.15
##############################

# %Y: devuelve el año con el siglo como número decimal. En nuestro ejemplo, esto es 2020.
# %m: devuelve el mes como un número decimal con relleno de ceros. En nuestro ejemplo, es 01.
# %d: devuelve el día como un número decimal con relleno de ceros. En nuestro ejemplo, es 04.

# from datetime import date

# d = date(2020, 1, 4)
# print(d.strftime('%Y/%m/%d'))

##############################
# Sección 4.5.1.16
##############################

# from datetime import time
# from datetime import datetime

# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))

# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S"))

##############################
# Sección 4.5.1.17
##############################

# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

##############################
# Sección 4.5.1.18
##############################

# from datetime import datetime
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

##############################
# Sección 4.5.1.19
##############################

# from datetime import date
# from datetime import datetime

# d1 = date(2020, 11, 4)
# d2 = date(2019, 11, 4)

# print(d1 - d2)

# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)

# print(dt1 - dt2)

##############################
# Sección 4.5.1.20
##############################

# from datetime import timedelta

# delta = timedelta(weeks=2, days=2, hours=3)
# print(delta)

## timedelta solo almacena días, segundos y microsegundos internamente

# from datetime import timedelta

# delta = timedelta(weeks=2, days=2, hours=3)
# print("Días:", delta.days)
# print("Segundos:", delta.seconds)
# print("Microsegundos:", delta.microseconds)

##############################
# Sección 4.5.1.21
##############################

# from datetime import timedelta
# from datetime import date
# from datetime import datetime

# delta = timedelta(weeks=2, days=2, hours=2)
# print(delta)

# delta2 = delta * 2
# print(delta2)

# d = date(2019, 10, 4) + delta2
# print(d)

# dt = datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)

###############################
# Laboratorio Sección 4.5.1.22
###############################

# from datetime import datetime

# my_date = datetime(2020, 11, 4, 14, 53)

# print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
# print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
# print(my_date.strftime("%a, %Y %b %d"))
# print(my_date.strftime("%A, %Y %B %d"))
# print(my_date.strftime("Día de la semana: %w"))
# print(my_date.strftime("Día del año: %j"))
# print(my_date.strftime("Número de semana en el año: %W"))

######################################

# Solicitar la fecha al usuario
# Ejemplo de formato de entrada:
# 2024-23-04 14:53:00

# from datetime import datetime

# string_fecha = input('Introduce una fecha con el formato yyyy-dd-mm h:mm:ss: ') 

# mi_fecha = datetime.strptime(string_fecha, "%Y-%d-%m %H:%M:%S")

# print(mi_fecha.strftime("%Y/%m/%d %H:%M:%S"))
# print(mi_fecha.strftime("%y/%B/%d %H:%M:%S %p"))
# print(mi_fecha.strftime("%a, %Y %b %d"))
# print(mi_fecha.strftime("%A, %Y %B %d"))
# print(mi_fecha.strftime("Día de la semana: %w"))
# print(mi_fecha.strftime("Día del año: %j"))
# print(mi_fecha.strftime("Número de semana en el año: %W"))

###############################
# Laboratorio extra
###############################

# from datetime import date, timedelta

# def siguiente_dia(fecha, dia):
#     dias_hasta_nuevo_dia = dia - fecha.weekday()
#     if dias_hasta_nuevo_dia <= 0: # El día ya ha transcurrido en ésta semana
#         dias_hasta_nuevo_dia += 7
#     return fecha + timedelta(dias_hasta_nuevo_dia)

# seis_semanas = timedelta(weeks=6)

# fecha_actual = date.today()
# siguiente_lunes = siguiente_dia(fecha_actual + seis_semanas, 0) # 0 = Lunes, 1=Martes, 2=Miércoles...
# print('El próximo Lunes 6 semanas después de la fecha actual es el día', siguiente_lunes)

#######################################
# José Antonio
#######################################

# from datetime import datetime, timedelta

# ahora = datetime.now()
# intervalo = timedelta(weeks=6)
# vencimiento = ahora + intervalo

# dia_semana_vencimiento = int(vencimiento.strftime('%w'))
# if dia_semana_vencimiento == 1:
#     print(vencimiento.strftime('%Y/%m/%d día semana: %a'))
# else:
#     vencimiento = vencimiento + timedelta(days= 8 - dia_semana_vencimiento)
#     print(vencimiento.strftime('%Y/%m/%d día semana: %a'))

########################################
# Francisco
########################################

# from datetime import datetime, timedelta

# # Fecha determinada (un lunes)
# fecha_actual = datetime(2024, 2, 26)  

# # Sumar 6 meses a la fecha determinada
# fecha_despues = fecha_actual + timedelta(days=30*6)

# # Encontrar el lunes más cercano después del tiempo
# while fecha_despues.weekday() != 0:  # 0 es el código para el lunes
#     fecha_despues += timedelta(days=1)

# print("Fecha del lunes después del tiempo:", fecha_despues.strftime("%Y-%m-%d"))

########################################
# Miguel Angel
########################################

# from datetime import *

# fecha_actual = date.today()
# seis_meses_despues  = fecha_actual + timedelta(365/2)

# dia_semana = seis_meses_despues.weekday()

# if dia_semana != 0 :
#     seis_meses_despues += timedelta(7-dia_semana)
# print(seis_meses_despues.strftime("Seis meses despues estamos a: %A"))
# print(seis_meses_despues)


###############################
# Resumen de Sección 4.5.1.23
###############################

# # 1. Para crear un objeto date, debes pasar los argumentos de año, mes y día de la siguiente manera:

# from datetime import date

# my_date = date(2020, 9, 29)
# print("Año:", my_date.year) # Año: 2020
# print("Mes:", my_date.month) # Mes: 9
# print("Día:", my_date.day) # Día: 29


# # El objeto date tiene tres atributos (de solo lectura): año, mes y día.


# # 2. El método today devuelve un objeto de fecha que representa la fecha local actual:

# from datetime import date
# print("Hoy:", date.today()) # Muestra: Hoy: 2020-09-29



# # 3. En Unix, la marca de tiempo expresa el número de segundos desde el 1 de Enero de 1970 a las 00:00:00 (UTC). 
# # Esta fecha se llama la "época de Unix", porque ahí comenzó el conteo del tiempo en los sistemas Unix. 
# # La marca de tiempo es en realidad la diferencia entre una fecha en particular (incluida la hora) 
# # y el 1 de Enero de 1970, 00:00:00 (UTC), expresada en segundos. 
# # Para crear un objeto de fecha a partir de una marca de tiempo, 
# # debemos pasar una marca de tiempo Unix al método fromtimestamp:

# from datetime import date
# import time

# timestamp = time.time()
# d = date.fromtimestamp(timestamp)


# # Nota: La función time devuelve el número de segundos desde el 1 de Enero de 1970 
# # hasta el momento actual en forma de número punto flotante.


# # 4. El constructor de la clase time acepta seís argumentos (hour, minute, second, microsecond, tzinfo, y fold). 
# # Cada uno de estos argumentos es opcional.

# from datetime import time

# t = time(13, 22, 20)

# print("Hora:", t.hour) # Hora: 13
# print("Minuto:", t.minute) # Minuto: 22
# print("Segundo:", t.second) # Segundo: 20



# # 5. El módulo time contiene la función sleep, que suspende la ejecución del programa 
# # durante un número determinado de segundos, por ejemplo:

# import time

# time.sleep(10)
# print("¡Hola mundo!") # Este texto se mostrará después de 10 segundos.



# # 6. En el módulo datetime, la fecha y la hora se pueden representar como objetos separados o como un solo objeto. 
# # La clase que combina fecha y hora se llama datetime. 
# # Todos los argumentos pasados al constructor van a atributos de clase de solo lectura. 
# # Son year, month, day, hour, minute, second, microsecond, tzinfo, y fold:

# from datetime import datetime

# dt = datetime(2020, 9, 29, 13, 51)
# print("Fecha y Hora:", dt) # Muestra: Fecha y Hora: 2020-09-29 13:51:00



# # 7. El método strftime toma solo un argumento en forma de cadena que especifica un formato 
# # que puede constar de directivas. Una directiva es una cadena que consta del carácter % (porcentaje) 
# # y una letra minúscula o mayúscula. 
# # A continuación se muestran algunas directivas útiles:

# # %Y: devuelve el año con el siglo como número decimal.
# # %m: devuelve el mes como un número decimal con relleno de ceros.
# # %d: devuelve el día como un número decimal con relleno de ceros.
# # %H: devuelve la hora como un número decimal con relleno de ceros.
# # %M: devuelve el minuto como un número decimal con relleno de ceros.
# # %S: devuelve el segundo como un número decimal con relleno de ceros.
# # Ejemplo:

# from datetime import date

# d = date(2020, 9, 29)
# print(d.strftime('%Y/%m/%d')) # Muestra: 2020/09/29



# # 8. Es posible realizar cálculos en los objetos date y datetime, por ejemplo:

# from datetime import date

# d1 = date(2020, 11, 4)
# d2 = date(2019, 11, 4)

# d = d1 - d2
# print(d) # Muestra: 366 days, 0:00:00.
# print(d * 2) # Muestra: 732 days, 0:00:00.


# # El resultado de la resta se devuelve como un objeto timedelta que expresa 
# # la diferencia en días entre las dos fechas en el ejemplo anterior.

# # Toma en cuenta que también se muestra la diferencia en horas, minutos y segundos. 
# # El objeto timedelta se puede utilizar para realizar más cálculos (por ejemplo, puedes multiplicarlo por 2).


# # Ejercicio 1

# # ¿Cuál es el resultado del siguiente fragmento de código?

# from datetime import time

# t = time(14, 39)
# print(t.strftime("%H:%M:%S"))


# # 14:39:00


# # Ejercicio 2

# # ¿Cuál es el resultado del siguiente fragmento de código?

# from datetime import datetime

# dt1 = datetime(2020, 9, 29, 14, 41, 0)
# dt2 = datetime(2020, 9, 28, 14, 41, 0)

# print(dt1 - dt2)

# # 1 day, 0:00:00

###################
# Sección 4.6.1.2
###################

# import calendar
# print(calendar.calendar(2020))

# import calendar
# calendar.prcal(2020)

###################
# Sección 4.6.1.3
###################

# import calendar
# print(calendar.month(2020, 11))

# import calendar
# calendar.prmonth(2020, 11)

###################
# Sección 4.6.1.4
###################

# import calendar

# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2020, 12)

###################
# Sección 4.6.1.5
###################

# import calendar
# print(calendar.weekday(2020, 12, 24))

###################
# Sección 4.6.1.6
###################

# import calendar
# print(calendar.weekheader(2))

################

# import calendar

# print(calendar.weekheader(3))
# print(calendar.month(2020, 11, w = 3))

###################
# Sección 4.6.1.7
###################

# import calendar

# print(calendar.isleap(2020))
# print(calendar.leapdays(2010, 2021))  # Hasta 2021, pero sin incluirlo.

###################
# Sección 4.6.1.9
###################

# import calendar  

# c = calendar.Calendar(calendar.SUNDAY)

# for weekday in c.iterweekdays():
#     print(weekday, end=" ")
    
###################
# Sección 4.6.1.10
###################

# import calendar  

# c = calendar.Calendar()

# for date in c.itermonthdates(2019, 11):
#     print(date, end=" ")
    
###################
# Sección 4.6.1.11
###################

# import calendar  

# c = calendar.Calendar()

# for iter in c.itermonthdays(2019, 11):
#     print(iter, end=" ")
    
###################
# Sección 4.6.1.12
###################

# import calendar  

# c = calendar.Calendar()

# for data in c.monthdays2calendar(2020, 12):
#     print(data)

###################################
# Laboratorio de Sección 4.6.1.13
###################################

# import calendar

# class MyCalendar(calendar.Calendar):
#     def count_weekday_in_year(self, year, weekday):
#         current_month = 1
#         number_of_days = 0
#         while (current_month <= 12):
#             for data in self.monthdays2calendar(year, current_month):
#                 if data[weekday][0] != 0:
#                     number_of_days = number_of_days + 1

#             current_month = current_month + 1
#         return number_of_days

# my_calendar = MyCalendar()
# number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

# print(number_of_days)
