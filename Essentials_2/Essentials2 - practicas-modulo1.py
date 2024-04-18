######################
# Sección 1.1.1.3
######################

# import math

# # # Alternativa

# import math
# import sys

# # # Alternativa

# import math, sys

######################
# Sección 1.1.1.5
######################

# import math

# print(math.sin(math.pi/2))

######################
# Sección 1.1.1.6
######################

# import math


# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None


# pi = 3.14

# print(sin(pi/2))

# print(math.sin(math.pi/2))

######################
# Sección 1.1.1.7
######################

# from math import pi

# print(pi)

# print(math.pi) # no hay namespace!

## Nota: no se importan otras entidades, únicamente las especificadas. 
## Además, no se pueden importar entidades adicionales utilizando una línea 
## como esta:

# print(math.e) # Error

# from math import sin, pi

# print(sin(pi/2))

######################
# Sección 1.1.1.8
######################

# ## llevar a cabo la importación selectiva.
# from math import sin, pi

# # ## hacer uso de las entidades importadas y obtiene el resultado esperado (1.0).

# print(sin(pi / 2))

# # ## redefinir el significado de pi y sin - en efecto, 
# # reemplazan las definiciones originales (importadas) dentro del namespace del código.

# pi = 3.14

# # # ## comprobar la redefinición

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# print(sin(pi / 2))


## Prueba 2

# pi = 3.14


# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None


# print(sin(pi / 2))

# from math import sin, pi

# print(sin(pi / 2)) # en módulo math!


######################
# Sección 1.1.1.9
######################
 
# from math import *

# # pi = 222222

# print(sin(pi/2))



# import math as m

# print(m.sin(m.pi / 2))

######################
# Sección 1.1.1.10
######################

# import math as m

# print(m.sin(m.pi/2))


# from math import pi as PI, sin as seno

# print(seno(PI/2))


######################
# Sección 1.1.1.11
######################

## Ejercicio 1
## Quieres invocar la función make_money() contenida en el módulo llamado mint. 
## Tu código comienza con la siguiente línea:
## ¿Cuál es la forma adecuada de invocar a la función?

# import mint



## Ejercicio 2
## Quieres invocar la función make_money() contenida en el módulo llamado mint. 
## ¿Cuál es la forma adecuada de invocar a la función?

# from mint import make_money
	



## Ejercicio 3
## Has escrito una función llamada make_money por tu cuenta. 
## Necesitas importar una función con el mismo nombre del módulo mint 
## y no deseas cambiar el nombre de ninguno de tus nombres previamente definidos. 
## ¿Qué variante de la sentencia import puede ayudarte con el problema?


## Ejercicio 4
## ¿Qué forma de invocación de la función make_money es válida 
## si tu código comienza con la siguiente línea?

# from mint import *

######################
# Sección 1.2.1.1
######################

# import math

# for name in dir(math):
#     print(name, end="\t")

# import math
# print(dir(math))

######################
# Sección 1.2.1.2
######################

# sin(x) → el seno de x.
# cos(x) → el coseno de x.
# tan(x) → la tangente de x.

# asin(x) → el arcoseno de x.
# acos(x) → el arcocoseno de x.
# atan(x) → el arcotangente de x.

# sinh(x) → el seno hiperbólico.
# cosh(x) → el coseno hiperbólico.
# tanh(x) → la tangente hiperbólica.
# asinh(x) → el arcoseno hiperbólico.
# acosh(x) → el arcocoseno hiperbólico.
# atanh(x) → el arcotangente hiperbólico.

# from math import pi, radians, degrees, sin, cos, tan, asin

# ad = 90
# ar = radians(ad)
# ad = degrees(ar)

# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

######################
# Sección 1.2.1.3
######################

# e → una constante con un valor que es una aproximación del número de Euler (e).
# exp(x) → encontrar el valor de ex.
# log(x) → el logaritmo natural de x.
# log(x, b) → el logaritmo de x con base b.
# log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
# log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).

# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

######################
# Sección 1.2.1.4
######################

# ceil(x) → devuelve el entero más pequeño mayor o igual que x.
# floor(x) → el entero más grande menor o igual que x.
# trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
# factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
# hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).


# from math import ceil, floor, trunc

# x = 1.4
# y = 2.6

# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

######################
# Sección 1.2.1.6
######################

# from random import random

# for i in range(500):
#     print(random())


# from random import random, seed

# seed(10)

# for i in range(5):
#     print(random())

######################
# Sección 1.2.1.7
######################

# from random import randrange, randint

# print(randrange(10), end=' ')
# print(randrange(8, 10), end=' ')
# print(randrange(0, 10, 3), end=' ')

# print(randint(0, 1))    # sin excluir el valor máximo

######################
# Sección 1.2.1.8
######################

# from random import randint


# for i in range(10):
#     print(randint(1, 10), end=',')

## choice(secuencia)
## sample(secuencia, elementos_a_elegir=1)

# from random import choice, sample

# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]

# # for i in range(10):
# #     print(choice(my_list), end = ' ')



# print(sample(my_list, 10))

######################

# from random import randint

# def tirar_dado():
#     return randint(1,6)

# # los mismos puntos de vida para ambos jugadores
# vida_jugador1 = vida_jugador2 = 100 

# while True:

#     # ¿en qué orden se atacan los jugadores?
#     # jugador 1 ataca primero
#     if randint(1,2) == 1:        
#         print('El jugador 1 ataca primero en éste turno\n')
#         vida_jugador2 -= tirar_dado() 

#         if vida_jugador2 <= 0:
#             print('El jugador 1 ha ganado y conserva', vida_jugador1, 'puntos de vida\n')
#             break
#         vida_jugador1 -= tirar_dado()
    
#         if vida_jugador1 <= 0:
#             print('El jugador 2 ha ganado y conserva', vida_jugador2, 'puntos de vida\n')
#             break
#     # jugador 2 ataca primero
#     else:     
#         print('El jugador 2 ataca primero en éste turno\n')
                         
#         vida_jugador1 -= tirar_dado() 

#         if vida_jugador1 <= 0:
#             print('El jugador 2 ha ganado y conserva', vida_jugador2, 'puntos de vida\n')
#             break
#         vida_jugador2 -= tirar_dado()
    
#         if vida_jugador2 <= 0:
#             print('El jugador 1 ha ganado y conserva', vida_jugador1, 'puntos de vida\n')
#             break
    
#     print('vida jugador 1 -->', vida_jugador1)
#     print('vida jugador 2 -->', vida_jugador2)
#     print()


#####################################################

# from random import randint
# import sys

# # los mismos puntos de vida para ambos jugadores
# vida_jugador1 = vida_jugador2 = 100 

# def tirar_dado():
#     return randint(1,6)

# def atacar(jugador):
#     global vida_jugador1, vida_jugador2
#     if jugador == 1:
#         vida_jugador2 -= tirar_dado() 
#         if vida_jugador2 <= 0:
#             print('El jugador 1 ha ganado y conserva', vida_jugador1, 'puntos de vida\n')
#             sys.exit()
#     else:
#         vida_jugador1 -= tirar_dado() 
#         if vida_jugador1 <= 0:
#             print('El jugador 2 ha ganado y conserva', vida_jugador2, 'puntos de vida\n')
#             sys.exit()

# while True:
#     # ¿en qué orden se atacan los jugadores?
#     # jugador 1 ataca primero
#     if randint(1,2) == 1:        
#         print('El jugador 1 ataca primero en éste turno\n')
#         atacar(1) 
#         atacar(2)
        
#     # jugador 2 ataca primero
#     else:     
#         print('El jugador 2 ataca primero en éste turno\n')                 
#         atacar(2)
#         atacar(1)

#     print('\tvida jugador 1 -->', vida_jugador1)
#     print('\tvida jugador 2 -->', vida_jugador2)
#     print()

######################

# from random import randint
# import sys

# # los mismos puntos de vida para ambos jugadores
# vida_jugador1 = vida_jugador2 = 100 

# def tirar_dado():
#     return randint(1,6)

# def comprobar_vida(jugador):
#     if jugador == 1 and vida_jugador1 <= 0:
#             print('El jugador 2 ha ganado y conserva', vida_jugador2, 'puntos de vida\n')
#             sys.exit()
#     elif jugador == 2 and vida_jugador2 <= 0:
#             print('El jugador 1 ha ganado y conserva', vida_jugador1, 'puntos de vida\n')
#             sys.exit()

# def atacar(jugador):
#     global vida_jugador1, vida_jugador2
#     if jugador == 1:
#         vida_jugador2 -= tirar_dado() 
#         comprobar_vida(2)
#     else:
#         vida_jugador1 -= tirar_dado()
#         comprobar_vida(1) 
        
# while True:
#     # ¿en qué orden se atacan los jugadores?
#     # jugador 1 ataca primero
#     if randint(1,2) == 1:        
#         print('El jugador 1 ataca primero en éste turno\n')
#         atacar(1) 
#         atacar(2)
        
#     # jugador 2 ataca primero
#     else:     
#         print('El jugador 2 ataca primero en éste turno\n')                 
#         atacar(2)
#         atacar(1)

#     print('\tvida jugador 1 -->', vida_jugador1)
#     print('\tvida jugador 2 -->', vida_jugador2)
#     print()

#####################################################

# import random

# DICE_VALUES = (1,2,3,4,5,6)

# MAX_LIFE = 40

# players = [ MAX_LIFE ] * 3
# players_positions = list( range( len( players ) ) )

# playing = True
# while playing:
# 	print( "Vidas de los jugadores:", players )

# 	random.shuffle( players_positions )
	
# 	print( "\tDart: ", players_positions )
# 	for i in players_positions:
# 		value = random.choice( DICE_VALUES )
# 		players[ i ] -= value
# 		if players[ i ] <= 0:
# 			print( f"\n\t>>> El jugador {i + 1} (pos = {i}) ha perdido." )
# 			playing = False
# 			break

# print( "Vidas de los jugadores: " + str( players ) )

######################
# Sección 1.2.1.10
######################

# platform(aliased = False, terse = False)

# aliased → cuando se establece a True (o cualquier valor distinto a cero) 
# puede hacer que la función presente los nombres de capa subyacentes 
# alternativos en lugar de los comunes.

# terse → cuando se establece a True (o cualquier valor distinto a cero) 
# puede convencer a la función de presentar una forma más breve del resultado 
# (si fuera posible).

# from platform import platform

# print(platform())
# print(platform(1))
# print(platform(0, 1))

######################
# Sección 1.2.1.11
######################

# # identificación del nombre genérico del procesador

# from platform import machine

# print(machine())

######################
# Sección 1.2.1.12
######################

# # identificación del nombre específico del procesador

# from platform import processor

# print(processor())

######################
# Sección 1.2.1.13
######################

# # identificación del nombre genérico del sistema operativo

# from platform import system

# print(system())

######################
# Sección 1.2.1.14
######################

# # identificación de la versión del sistema operativo

# from platform import version, uname

# print(version())
# print(uname())

######################
# Sección 1.2.1.15
######################

# # python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
# # python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
# # La parte mayor de la versión de Python.
# # La parte menor.
# # El número del nivel de parche.

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr, '.',end='', sep='')

######################
# Sección 1.2.1.16
######################

# Módulos estándar de Python

# https://docs.python.org/3/py-modindex.html

######################
# Sección 1.2.1.17
######################

# Ejercicio 1
# ¿Cuál es el valor esperado de la variable result 
# después de que se ejecuta el siguiente código?

# import math
# result = math.e == math.exp(1)
# print(result)

# Ejercicio 2
# (Completa el enunciado) 
# Establecer la semilla del generador con el mismo valor 
# cada vez que se ejecuta tu programa garantiza que ...
# ... los valores pseudoaleatorios emitidos desde el módulo random serán exactamente los mismos.



# Ejercicio 3
# ¿Cuál de las funciones del módulo platform utilizarías para determinar el nombre de la CPU que corre dentro de tu computadora?
# La función processor()



# Ejercicio 4
# ¿Cuál es el resultado esperado del siguiente fragmento de código?

# import platform

# print(len(platform.python_version_tuple()))

# print(platform.python_version_tuple())

######################
# Sección 1.3.1.2
######################

# ficheros module.py y main.py

######################
# Sección 1.3.1.3
######################

# ficheros module.py y main.py

######################
# Sección 1.3.1.4
######################

# ficheros module.py y main.py

######################
# Sección 1.3.1.5
######################

# Paso 11 - Probar también con IDLE u otra herramienta!!

# import sys

# for p in sys.path:
#     print(p)



# Paso 12

# from sys import path

# path.append('..\\modules')

# import module

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))

######################
# Sección 1.3.1.6
######################

# Ejemplos en carpeta extra!!!

######################
# Sección 1.3.1.7
######################

# La ubicación de una función llamada funT() del paquete tau puede describirse como: 

#   extra.good.best.tau.funT()


# Una función marcada como: 

#   extra.ugly.psi.funP()

# Proviene del módulo psi el cual esta almacenado 
# en el subpaquete ugly del paquete extra.

######################
# Sección 1.3.1.8
######################

# Descargar estructura de directorios
# A continuación trabajamos con el fichero main2.py (carpeta test)

######################
# Sección 1.3.1.9
######################

# Paso 7 del fichero main2.py 

######################
# Sección 1.3.1.10
######################

# Pasos 8 y 9 del fichero main2.py 

######################
# Sección 1.3.1.11
######################

# # Ejercicio 1
# # Deseas evitar que el usuario de tu módulo ejecute tu código como un script ordinario.
# # ¿Cómo lograrías tal efecto?

# import sys

# if __name__ == "__main__":
#     print("¡No hagas eso!")
#     sys.exit()

# # Ejercicio 2
# # Algunos paquetes adicionales y necesarios se almacenan 
# # dentro del directorio D:\Python\Project\Modules. 
# # Escribe un código asegurándote de que Python recorra el directorio 
# # para encontrar todos los módulos solicitados.

# import sys

# # ¡Toma en cuenta las diagonales invertidas dobles!
# sys.path.append("D:\\Python\\Project\\Modules")

# # Ejercicio 3
# # El directorio mencionado en el ejercicio anterior contiene un subárbol 
# # con la siguiente estructura:

# # abc
# #  |__ def
# #       |__ mymodule.py


# # Asumiendo que D:\Python\Project\Modules se ha adjuntado con éxito 
# # a la lista sys.path, escribe una directiva de importación que te permita 
# # usar todas las entidades de mymodule.

# import abc.def.mymodule

######################
# Sección 1.4.1.2
######################

# Python Software Foundation:
# https://wiki.python.org/psf/PackagingWG.


# El sitio web de PyPI (administrado por PWG) se encuentra en la dirección: 
# https://pypi.org/.

######################
# Sección 1.4.1.3
######################

# Instalar pip en MacOS
# https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

# Instalar pip en distribuciones de Linux
# https://www.tecmint.com/install-pip-in-linux/

# Instalar pip en Windows
# https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

######################
# Sección 1.4.1.11
######################

# comandos de sistema operativo:

# ayuda de pip
# pip3 help

# ayuda sobre comando especifico
# pip3 help install

# ¿qué paquetes se han instalado hasta el momento?
# pip3 list

######################
# Sección 1.4.1.12
######################

# comandos de sistema operativo:
# pip3 show nombre_del_paquete
   
# pip3 show pip

# búsqueda de paquetes

# pip3 search pip # API desactivada - será deprecada en el futuro

# Version online:
# https://pypi.org/search/

######################
# Sección 1.4.1.13
######################

# Instalación de paquete pygame
# pip3 install pygame

# Instalacion solo para el usuario actual
# pip3 install --user pygame

# pip show pygame
# pip3 list

######################
# Sección 1.4.1.14
######################

# Spyder con otros paquetes:
# https://docs.spyder-ide.org/5/faq.html#using-packages-installer

# (ejecutar en IDLE o VS Code)

# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Bienvenido a pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False

######################
# Sección 1.4.1.15
######################

# # pip_install Es capaz de actualizar un paquete instalado localmente; 
# # por ejemplo, si deseas asegurarte de que estás utilizando la última versión 
# # de un paquete en particular, puedes ejecutar el siguiente comando: 

# pip install -U nombre_del_paquete

# # Es capaz de instalar una versión seleccionada por el usuario de un paquete 
# # (pip instala por defecto la versión más nueva disponible); 
# # para lograr este objetivo debes utilizar la siguiente sintaxis: 

# pip install nombre_del_paquete==versión_del_paquete


# # (toma en cuenta el doble signo de igual), por ejemplo: 

# pip install pygame==1.9.2

######################
# Sección 1.4.1.16
######################

# pip uninstall nombre_del_paquete

# # Para desinstalar pygame, puedes ejecutar el siguiente comando:

# pip uninstall pygame

######################
# Sección 1.4.1.18
######################
# The Cheese Shop (La Tienda de Queso). 
# Su sitio web está disponible en https://pypi.org/.

# Para verificar la versión de pip, se deben emitir los siguientes comandos:

# pip --version

# o

# pip3 --version


# La lista de las actividades principales de pip tiene el siguiente aspecto:

# pip help operación_o_comando 

#     muestra una breve descripción de pip.
    
# pip list

#     muestra una lista de los paquetes instalados actualmente.
    
# pip show nombre_del_paquete

#     muestra información que incluyen las dependencias del paquete.
    
# pip search cadena

#     busca en los directorios de PyPI para encontrar paquetes 
#     cuyos nombres contengan cadena.
    
# pip install nombre

#     instala el paquete nombre en todo el sistema 
#     (espera problemas cuando no tengas privilegios de administrador).
    
# pip install --user nombre

#     instala nombre solo para ti; ningún otro usuario de la plataforma 
#     podrá utilizarlo.
    
# pip install -U nombre

#     actualiza un paquete previamente instalado.
    
# pip uninstall nombre

#     desinstala un paquete previamente instalado.

# Ejercicio 1
# ¿De donde proviene el nombre The Cheese Shop?

# Es una referencia a un viejo sketch de Monty Python que lleva el mismo nombre.



# Ejercicio 2

# ¿Por qué deberías asegurarte de cuál pip o pip3 es el correcto para ti?

# Cuando Python 2 y Python 3 coexisten en el sistema operativo, 
# es probable que pip identifique la instancia de pip que trabaja 
# solo con paquetes de Python 2.



# Ejercicio 3

# ¿Cómo puedes determinar si tu pip funciona con Python 2 o Python 3?


# pip --version 


# Ejercicio 4

# Desafortunadamente, no tienes privilegios de administrador. 
# ¿Qué debes hacer para instalar un paquete en todo el sistema?

# Tienes que consultar a tu administrador del sistema
# ¡no intentes hackear tu sistema operativo!









####################################
# Otros
####################################

# # https://www.juniper.net/documentation/us/en/software/junos/automation-scripting/topics/task/junos-python-modules-psutil-module.html
# import psutil
# import datetime

# ### *** CPU FUNCTIONS ***

# # Number of logical CPUs in the system
# print ("psutil.cpu_count() = {0}".format(psutil.cpu_count()))


# ### *** DISK FUNCTIONS ***

# # List of named tuples containing all mounted disk partitions
# dparts = psutil.disk_partitions()
# print("psutil.disk_partitions() = {0}".format(dparts))

# # Disk usage statistics
# du = psutil.disk_usage('/')
# print("psutil.disk_usage('/') = {0}".format(du))


# ### *** MEMORY FUNCTIONS ***

# # System memory usage statistics
# mem = psutil.virtual_memory()
# print("psutil.virtual_memory() = {0}".format(mem))

# THRESHOLD = 100 * 1024 * 1024  # 100MB
# if mem.available <= THRESHOLD:
#     print("warning, available memory below threshold")


# ### *** PROCESS FUNCTIONS ***

# # List of current running process IDs.
# pids = psutil.pids()
# print("psutil.pids() = {0}".format(pids))


# # Check whether the given PID exists in the current process list.
# for proc in psutil.process_iter():
#     try:
#         pinfo = proc.as_dict(attrs=['pid', 'name'])
#     except psutil.NoSuchProcess:
#         pass
#     else:
#         print(pinfo)


# ### *** SYSTEM INFORMATION FUNCTIONS ***

# # System boot time expressed in seconds since the epoch
# boot_time = psutil.boot_time()
# print("psutil.boot_time() = {0}".format(boot_time))

# # System boot time converted to human readable format
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# # Users currently connected on the system
# users = psutil.users()
# print("psutil.users() = {0}".format(users))

################################################

## tensorflow 2.x

## https://stackoverflow.com/questions/60143148/tensorflow-2-1-0-attributeerror-module-tensorflow-has-no-attribute-runmeta

# import tensorflow as tf
# from tensorflow.keras.models import Sequential 
# from tensorflow.keras.layers import Dense 
# print(tf.__version__)
# def get_flops(model):
#     run_meta = tf.compat.v1.RunMetadata()
#     opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()

#     # We use the Keras session graph in the call to the profiler.
#     flops = tf.compat.v1.profiler.profile(graph=tf.compat.v1.keras.backend.get_session().graph,
#                                 run_meta=run_meta, cmd='op', options=opts)

#     return flops.total_float_ops  # Prints the "flops" of the model.

# # .... Define your model here ....
# model = Sequential() 
# model.add(Dense(8, activation = 'softmax')) 
# print(get_flops(model))



## Ejemplo para tensorflow 1.x
# https://www.pythonfixing.com/2021/12/fixed-tensorflow-is-there-way-to.html
# (pip3 install tensorflow)

# import tensorflow as tf
# import tensorflow.python.framework.ops as ops 
# g = tf.Graph()
# run_meta = tf.RunMetadata()
# with g.as_default():
#     A = tf.Variable(tf.random_normal( [25,16] ))
#     B = tf.Variable(tf.random_normal( [16,9] ))
#     C = tf.matmul(A,B) # shape=[25,9]

#     opts = tf.profiler.ProfileOptionBuilder.float_operation()    
#     flops = tf.profiler.profile(g, run_meta=run_meta, cmd='op', options=opts)
#     if flops is not None:
#         print('Flops should be ~',2*25*16*9)
#         print('25 x 25 x 9 would be',2*25*25*9) # ignores internal dim, repeats first
#         print('TF stats gives',flops.total_float_ops)

####################################
# #  Pruebas de rendimiento
####################################

# import time
# import numpy as np

# numbers = 100000000

# ## Peor rendimiento, el for en C pero la suma en Python

# start = time.time()

# suma=0

# for i in range(1,numbers):
#     suma += i

# print (time.time()-start,"Segundos","Total Suma:", suma)

# ## Rendimiento medio, mejor con las funciones integradas

# start = time.time()

# suma=0

# suma = sum(range(1,numbers)) 

# print (time.time()-start,"Segundos","Total Suma:", suma)

# ## Alto rendimiento con funciones específicas de numpy - la mayor parte en C

# start = time.time()

# suma=0

# suma = np.nansum(np.arange(1,numbers))

# print (time.time()-start,"Segundos","Total Suma:", suma)
