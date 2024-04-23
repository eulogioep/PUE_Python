################### Generadores (Iteradores) #############

#### Fibonacci ########

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

#########

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

########### Sentencia Yield ################################

### Fibonacci con yield ###

# def GenFib2( n ):
# 	s0 = 0
# 	s1 = 1
# 	for i in range( n ):
# 		yield s0
# 		s0, s1 = s1, (s0 + s1)

# for v in GenFib2( 10 ):
# 	print( v )

######################


# def fun(n):
#     for i in range(n):
#         return i

# print(fun(10)) # Devuelve un solo valor
######

# def fun(n):
#     for i in range(n):
#         yield i # con yield, es como un generador


# for v in fun(5):
#     print(v)


#### Potencia de 2 ######

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# for v in powers_of_2(8):
#     print(v)


#### Potencia de 2 en formato Lista por comprensión #####

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# t = [x for x in powers_of_2(5)]
# print(t)


###### Tranformando a Lista ###

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# t = list(powers_of_2(3))
# print(t)


### in también se puede usar como iterador ###

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# for i in range(20):
#     if i in powers_of_2(4):
#         print(i)

### Fibonacci en Lista ###

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

#### Lista por comprensión ###

# list_1 = []

# for ex in range(6):
#     list_1.append(10 ** ex)

# list_2 = [10 ** ex for ex in range(6)]

# print(list_1)
# print(list_2)


####

# the_list = []

# for x in range(10):
#     the_list.append(1 if x % 2 == 0 else 0)

# print(the_list)


######## Diferencia entre Lista y Generador ################

# Solo un cambio puede convertir cualquier comprensión en un generador.
# Son los paréntesis. Los corchetes hacen una comprensión, los paréntesis hacen un generador.

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

# # for v in the_list:
# #     print(v, end=" ")
# print(the_list)

# the_generator = (str(x) + " - Par"  if x % 2 == 0 else str(x)+ " - Impar" for x in range(10))

# # for v in the_generator:
# #     print(v, end=" ")
# print(the_generator.__next__())
# print(the_generator.__next__())
# print(the_generator.__next__())
# print(the_generator.__next__())
# print(the_generator.__next__())
# print(the_generator.__next__())
# print(the_generator.__next__())

### En un diccionario ###

# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# print(counters)

######### La función lambda ###########################

# Una función lambda es una función sin nombre (también puedes llamarla una función anónima). 

# lambda parámetros: expresión

# Una función metida en una variable que se puede invocar.

# Se suele utilizar para crear funciones simples.

# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y

# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

###

# def ejecutarFuncion(numero, funcion):
#     return funcion(numero)

# print(ejecutarFuncion(9, lambda x: x * x))
# print(ejecutarFuncion(9, lambda x: x + x))

#################

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')


# def poly(x):
#     return 2 * x**2 - 4 * x + 2


# print_function([x for x in range(-2, 3)], poly)

# ### Mismo programa pero con lambda ###

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')

# print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)



############ Lambdas y la función map() ###################################

# La función map() aplica la función pasada por su primer argumento a todos los 
# elementos de su segundo argumento y devuelve un iterador que entrega todos los 
# resultados de funciones subsequentes.
# Puedes usar el iterador resultante en un bucle o convertirlo en una lista usando la función list().

# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1)) # map que convierto en una lista
# print(list_2)

# for x in map(lambda x: x * x, list_2): # Map como interador
#     print(x, end=' ')
# print()

############## Lambdas y la función filter() ###########################

# Espera el mismo tipo de argumentos que map(), pero hace algo diferente: 
# filtra su segundo argumento mientras es guiado por direcciones que fluyen 
# desde la función especificada en el primer argumento (la función se invoca 
# para cada elemento de la lista, al igual que en map() ).

# Los elementos que devuelven True de la función pasan el filtro, los otros son rechazados.

# from random import seed, randint

# seed()
# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# print(data)
# print(filtered)

############## Cierres ###############

# Comencemos con una definición: cierres es una técnica que permite almacenar valores 
# a pesar de que el contexto en el que se crearon ya no existe. 
# Un cierre se debe invocar exactamente de la misma manera en que se ha declarado.

# Los cierres son como pequeñas burbujas de memoria que contienen variables. 
# Imagina que tienes una caja con algunas cosas dentro. Esa caja es el cierre. 
# En Python, los cierres ocurren cuando una función interna 
# (una función dentro de otra función) recuerda las variables de la función externa 
# incluso después de que la función externa haya terminado de ejecutarse.

# Este programa falla porque la variable loc es interna

# def outer(par):
#     loc = par


# var = 1
# outer(var)

# print(var)
# print(loc)

# Con el cierre se puede solventar asignando a una variable una función interna:

# def outer(par):
#     loc = par

#     def inner():
#         return loc
#     return inner


# var = 1
# fun = outer(var)
# print(fun())


### Otro ejemplo ###
# Un cierre se debe invocar exactamente de la misma manera en que se ha declarado.

# def crear_cierre(numero):
#     valor = numero

#     def potencia(parametro):
#         return parametro ** valor
    
#     return potencia



# cuadrado = crear_cierre(2)
# cubo = crear_cierre(3)

# for numero in range(5):
#     print(numero, cuadrado(numero), cubo(numero))

### Otro ejemplo ###

# def contador():
#     n = 0
#     def incrementar():
#         nonlocal n
#         n += 1
#         return n
#     return incrementar

# contador1 = contador()
# print(contador1())  # Imprime 1
# print(contador1())  # Imprime 2


############# Decoradores ########

# Los decoradores son como “envoltorios” para funciones. Imagina que tienes 
# un regalo y quieres ponerle un papel bonito alrededor. El papel es el decorador. 
# En Python, los decoradores son funciones que modifican o mejoran otras funciones. 
# ¿Por qué querríamos hacer esto? Bueno, aquí tienes algunos ejemplos:

# Registrar funciones: Los decoradores pueden llevar un registro de cuántas 
# veces se llama una función o cuánto tiempo tarda en ejecutarse.
# Validación: Pueden verificar si los argumentos de una función son válidos antes de ejecutarla.
# Autenticación: Pueden verificar si un usuario tiene permiso para acceder a una función.


# def decorador(funcion_original):
#     def funcion_envoltorio():
#         print("Antes de llamar a la función")
#         funcion_original()
#         print("Después de llamar a la función")
#     return funcion_envoltorio

# @decorador
# def saludar():
#     print("¡Hola!")

# saludar()

# @decorador
# def darlasbuenasnoches():
#     print("¡Buenas noches!")

# darlasbuenasnoches()

########## Archivos #############################

#stream = open(file, mode = 'r', encoding = None)

# Modos para abrir los streams:

## r modo de apertura: lectura

# El stream será abierto en modo lectura.
# El archivo asociado con el stream debe existir y tiene que ser legible, 
# de lo contrario la función open() generará una excepción.

## w modo de apertura: escritura

# El stream será abierto en modo escritura.
# El archivo asociado con el stream no necesita existir. Si no existe, 
# se creará; si existe, se truncará a la longitud de cero (se borra); 
# si la creación no es posible (por ejemplo, debido a permisos del sistema) 
# la función open() generará una excepción.

## a modo de apertura: adjuntar

# El stream será abierto en modo adjuntar.
# El archivo asociado con el stream no necesita existir; si no existe, 
# se creará; si existe, el cabezal de grabación virtual se establecerá
# al final del archivo (el contenido anterior del archivo permanece intacto).

## r+ modo de apertura: lectura y actualización

# El stream será abierto en modo lectura y actualización.
# El archivo asociado con el stream debe existir y tiene que permitir escritura, 
# de lo contrario la función open() generará una excepción.
# Se permiten operaciones de lectura y escritura en el stream.

## w+ modo de apertura: escritura y actualización

# El stream será abierto en modo escritura y actualización.
# El archivo asociado con el stream no necesita existir; si no existe, se creará; 
# el contenido anterior del archivo permanece intacto.
# Se permiten operaciones de lectura y escritura en el stream.

# Seleccionando modo de texto y modo binario:
# Si hay una letra b al final de la cadena del modo significa que el stream se 
# debe abrir en el modo binario.

# Si la cadena del modo termina con una letra t el stream es abierto en modo texto.

# El modo texto es el comportamiento predeterminado que se utiliza cuando no se especifica 
# ya sea modo binario o texto.

# Finalmente, la apertura exitosa del archivo establecerá la posición actual del archivo 
# (el cabezal virtual de lectura/escritura) antes del primer byte del archivo si el modo 
# no es a y después del último byte del archivo si el modo es a.

# También puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el 
# modo de apertura x. Si el archivo ya existe, la función open() generará una excepción.

# Resumen:

# Modo Texto     # Modo Binario       # Descripción

# rt                  rb                  lectura
# wt                  wb                  escritura
# at                  ab                  adjuntar
# r+t                 r+b                 lectura y actualización
# w+t                 w+b                 escritura y actualización

### Ejemplos:

# try:
#     stream = open("E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt", "rt")
#     # El procesamiento va aquí.
#     stream.close()
# except Exception as exc:
#     print("No se puede abrir el archivo:", exc)

# Diagnosticando problemas con los streams

# El objeto IOError está equipado con una propiedad llamada errno (el nombre viene 
# de la frase error number, número de error) y puedes accederla de la siguiente manera:

# try:
#     pass
#     # Algunas operaciones con streams.
# except IOError as exc:
#     print(exc.errno)
    
# Algunas de las constantes para identificar errores con los archivos:

# errno.EACCES → Permiso denegado -> El error se produce cuando intentas, por ejemplo, abrir 
# un archivo con atributos de solo lectura para abrirlo.

# errno.EBADF → Número de archivo incorrecto -> El error se produce cuando intentas, por ejemplo,
# operar un stream sin abrirlo.

# errno.EEXIST → Archivo existente -> El error se produce cuando intentas, por ejemplo,
# cambiar el nombre de un archivo con su nombre anterior.

# errno.EFBIG → Archivo demasiado grande - > El error ocurre cuando intentas crear un archivo 
# que es más grande que el máximo permitido por el sistema operativo.

# errno.EISDIR → Es un directorio -> El error se produce cuando intentas tratar un nombre de
# directorio como el nombre de un archivo ordinario.

# errno.EMFILE → Demasiados archivos abiertos -> El error se produce cuando intentas abrir 
# simultáneamente más streams de los aceptables para el sistema operativo.

# errno.ENOENT → El archivo o directorio no existe -> El error se produce cuando intentas 
# acceder a un archivo o directorio inexistente.

# errno.ENOSPC → No queda espacio en el dispositivo -> El error ocurre cuando no hay espacio 
# libre en el dispositivo.

# Todas las constantes: https://docs.python.org/es/3/library/errno.html

###

# import errno

# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("El archivo no existe.")
#     elif exc.errno == errno.EMFILE:
#         print("Demasiados archivos abiertos.")
#     else:
#         print("El numero del error es:", exc.errno)



### Ej Lectura de un archivo de texto plano ###

# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
# stream = open("E:/Documentos/Python/Cursos PUE/Python/Essentials_2/tzop.txt", "rt", encoding = "utf-8")

# Se imprime el contenido del archivo:
# print(stream.read()) 

### Ej Contador de caracteres de un archivo de texto ###

# from os import strerror

# try:
#     counter = 0
#     stream = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', "rt")
#     char = stream.read(1)
#     while char != '':
#         print(char, end='')
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))


### Si aumentamos el tamaño del buffer, conseguimos que se realicen menos lecturas del disco

# from os import strerror

# try:
#     counter = 0
#     stream = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', "rt")
#     char = stream.read(128)
    
#     counter += 128
#     while char != '':
#         print(char, end='')
        
#         char = stream.read(128)
#         counter += len(char)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

### Si sabemos que el archivo no es muy grande, podemos leerlo entero con read()#########

# from os import strerror

# try:
#     counter = 0
#     stream = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', "rt")
#     content = stream.read()
#     for char in content:
#         print(char, end='')
#         counter += 1
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

### Procesando archivos de texto: readline() ###

# El método intenta leer una línea completa de texto del archivo, y la devuelve como una 
# cadena en caso de éxito. De lo contrario, devuelve una cadena vacía.

# from os import strerror

# try:
#     character_counter = line_counter = 0
#     stream = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', 'rt')
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
    

### 

# from os import strerror

# try:
#     character_counter = line_counter = 0
#     stream = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', 'rt')
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

### Con un iterador ###

# from os import strerror

# try:
# 	character_counter = line_counter = 0
# 	for line in open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/text.txt', 'rt'):
# 		line_counter += 1
# 		for char in line:
# 			print(char, end='')
# 			character_counter += 1
# 	print("\n\nCaracteres en el archivo: ", character_counter)
# 	print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))
 
####### Escritura de archivos de texto plano ########################################

# from os import strerror

# try:
# 	file = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/newtext.txt', 'wt', encoding='utf-8') # Un nuevo archivo (newtext.txt) es creado.
# 	for i in range(10):
# 		s = "línea #" + str(i+1) + "\n"
# 		for char in s:
# 			file.write(char) # Escribe caracter a caracter
# 	file.close()
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))
 
### Escribir todos los caraceres y no de uno en uno.

# from os import strerror

# try:
#     file = open('E:/Documentos/Python/Cursos PUE/Python/Essentials_2/newtext.txt', 'wt', encoding='utf-8')
#     for i in range(10):
#         file.write("línea #" + str(i+1) + "\n")
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

#################### Procesar archivos de bytes ##################################

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 - i

# for b in data:
#     print(hex(b))
    
# ### Ejemplo de un programa que copia archivos ###

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


### Lee un archivo en bytes y lo copia 


# from os import strerror

# try:
#     imagen_original = open('python.png', 'rb')
#     duplicado = open('duplicado-logo.png', 'wb')

#     contenido = imagen_original.read()

#     duplicado.write(contenido)

#     imagen_original.close()
#     duplicado.close()

#     print("Imagen duplicada correctamente.")

# except IOError as e:
#     print("Error de Entrada/Salida:", strerror(e.errno))
    
    
####### Laboratorios ###############

# from os import strerror

# # Inicializa 26 contadores para cada letra latina.
# # Nota: hemos usado una comprensión para esto.
# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
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


####################

# from os import strerror

# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# file_name = input("Ingresa el nombre del archivo a analizar: ")
# try:
#     file = open(file_name, "rt")
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 counters[char.lower()] += 1
#     file.close()
#     file = open(file_name + '.hist', 'wt')
#     # Nota: hemos utilizado una lambda para acceder a los elementos del directorio y se ha establecido revese a True para obtener un orden válido.
#     for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
#         c = counters[char]
#         if c > 0:
#             file.write(char + ' -> ' + str(c) + '\n')
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))

###

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

##############

# def mi_generador():
#     for i in range(65,123):
#         if i > 90 and i < 97:
#             continue
#         else:
#             yield chr(i)
      

# abecedario = {}

# abecedario = {caracter: 0 for caracter in mi_generador()}

# print(abecedario)
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
# abecedario_ordenado_por_valor = dict(sorted(abecedario.items(), key=lambda item: item[1],reverse=True))
# for clave, valor in abecedario_ordenado_por_valor.items():
#     if valor != 0:
#         print('{:<5} {}'.format(clave, valor))
        
#############################

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


########## Módulo OS  ######################################

# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())
# print(os.uname())
# print(os.name)


##### Eliminar Directorios ###

# import os

# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())


### Laboratorio ###

## Búsqueda en directorios con recursividad ###

# import os

# def buscar(ruta, directorio_a_buscar):
#     try:
#         # cambiar el directorio de trabajo actual
#         os.chdir(ruta)
#     except OSError:
#         # No procesa un archivo que no es un directorio.
#         return
    
#     # Saber en qué directorio estamos actualmente
#     directorio_actual = os.getcwd()
    
#     # recorrer el directorio actual
#     for entrada_actual in os.listdir(directorio_actual):

#         # si encontramos una coincidencia, imprimirla
#         if entrada_actual == directorio_a_buscar:
#             print(directorio_actual + "/" + directorio_a_buscar)
            
#         # Llamada recursiva a find() para buscar en subdirectorios
#         buscar(directorio_actual + "/" + entrada_actual, directorio_a_buscar)

# buscar("./tree", "python")

####

# import os

# def find(path, directory):
#     for root, dirs, files in os.walk(path):
#         if directory in dirs:
#             print(os.path.join(root, directory))

# path = "./tree"
# directory = "python"
# find(path, directory)

#####

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


######## Módulo Datetime #######################################

# from datetime import date

# today = date.today()

# print("Hoy:", today)
# print("Año:", today.year)
# print("Mes:", today.month)
# print("Día:", today.day)


### 

# from datetime import date
# import time

# timestamp = time.time()
# print("Marca de tiempo:", timestamp)

# d = date.fromtimestamp(timestamp)
# print("Fecha:", d)


# ###

# from datetime import date

# d = date.fromisoformat('2019-11-04')
# print(d)


# ###

# from datetime import date

# d = date(1991, 2, 5)
# print(d)

# d = d.replace(year=1992, month=1, day=16)
# print(d)


# ###

# from datetime import date

# d = date(2019, 11, 4)
# print(d.weekday())


# ###

# from datetime import time

# t = time(14, 53, 20, 1)

# print("Tiempo:", t)
# print("Hora:", t.hour)
# print("Minuto:", t.minute)
# print("Segundo:", t.second)
# print("Microsegundo:", t.microsecond)


# ###

# import time

# class Student:
#     def take_nap(self, seconds):
#         print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
#         time.sleep(seconds)
#         print("¡Dormí bien! ¡Me siento genial!")

# student = Student()
# student.take_nap(5)


# ###

# import time

# timestamp = 1572879180
# print(time.ctime(timestamp))


# ###

# import time

# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))


# ###

# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


# ###

# from datetime import datetime

# dt = datetime(2019, 11, 4, 14, 53)

# print("Fecha y Hora:", dt)
# print("Fecha:", dt.date())
# print("Hora:", dt.time())


# ###

# from datetime import datetime

# print("hoy:", datetime.today())
# print("ahora:", datetime.now())
# print("utc_ahora:", datetime.utcnow())


# ###

# from datetime import datetime

# dt = datetime(2020, 10, 4, 14, 55)
# print("Marca de tiempo:", dt.timestamp())


# ###

# from datetime import time
# from datetime import datetime

# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))

# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S"))


# ###

# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))


# ###

# from datetime import datetime
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


# ###

# from datetime import date
# from datetime import datetime

# d1 = date(2020, 11, 4)
# d2 = date(2019, 11, 4)

# print(d1 - d2)

# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)

# print(dt1 - dt2)


# ###

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


# ### Laboratorio #########

# from datetime import datetime

# my_date = datetime(2020, 11, 4, 14, 53)

# print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
# print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
# print(my_date.strftime("%a, %Y %b %d"))
# print(my_date.strftime("%A, %Y %B %d"))
# print(my_date.strftime("Día de la semana: %w"))
# print(my_date.strftime("Día del año: %j"))
# print(my_date.strftime("Número de semana en el año: %W"))


#########################


