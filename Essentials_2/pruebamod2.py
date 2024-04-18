# import math

# for name in dir(math):
#     print(name, end="\t")

# ##################################

# # numeros aleatorios con la misma semilla

# from random import random, seed

# seed(0) # Siempre saldrá la misma información

# for i in range(5):
#     print(random())

# #######################

# from random import randrange, randint

# for i in range(10):
#     print(randrange(10), end=' ')
#     print(randrange(8, 10), end=' ')
#     print(randrange(0, 10, 3), end=' ')
#     print(randint(0, 10), end = ' ') # no excluye el valor maximo


######################################

# from random import choice, sample

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(10):
#     print(choice(my_list))
#     print(sample(my_list, 5))
#     print(sample(my_list, 10))

############################
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
    
    
#     ############################
#     import random

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


# #######################################

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

# #############################################

# # Accediendo al hardwware

# from platform import platform, machine, processor, system, version, uname

# # S.O.
# print(platform())
# print(platform(1))
# print(platform(0, 1))

# # Tipo de maquina
# print(machine())

# # Procesador
# print(processor())

# # Nombre del sistema operativo
# print(system())

# # Versión del S.O.
# print(version())
# print(uname()) # Información completa en formato Tupla

###########################################

# # Información sobre el Python que estamos utilizando

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     #print(atr)
#     print(atr, ".", end="", sep="")

#############################################

# pip para instalar un paquete (ej pygame)
#
# pip help # ayuda
# pip help install
# pip list # muestra una lista de paquetes instalados
# pip 
# pip show pip # muestra informacion del paquete
# pip install pygame # instala pygame
# pip install -U nombre_del_paquete # Update
# pip install pygame==1.9.2 # instala una versión concreta
# pip uninstall pygame # Desinstalas el paquete



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

###############################################

# # UNICODE 

# print("Código ASCII:")

# for caracter in range(32, 128, 16):

#     print('\nCaracter:',end="")

#     for codigo in range(caracter, caracter + 16):
#       print('%4s'%chr(codigo), end="")
#     print()

#     print('Código:   ',end="")

#     for codigo in range(caracter, caracter + 16):
#       print('%4s'%codigo, end="")
#     print()
    
#####################
    
# # Imprimir los primeros 10000 caracteres unicode

# for i in range(0,10000):
#     print('\\u' + str(i), "- Caracter:", chr(i))

#####################

# print(ord('a')) # ord es el ordinal asociado al carácter
# print(chr('a')) # ord es el carácter asociado

####################################################

# str1 = 'a'
# str2 = 'b'

# print(str1 + str2) # ab
# print(str2 + str1) # ba
# print(5 * 'a') # aaaaa
# print('b' * 4) # bbbb

# #####################

# # Imprimir los caracteres ascii

# # for i in range(128):
# #     print(f"Carácter: {chr(i)}, Valor ASCII: {i}")
    
# for i in range(128):
#     print('ASCII', i, '=', chr(i))

# ########################

# # Conversión de carácter a ordinal

# # # Demostración de la función ord ().

# char_1 = 'a'
# char_2 = ' '  # space

# print(ord(char_1))
# print(ord(char_2))


###########

# De Ordinal a Cahracter

# Demostración de la función chr.

# print(chr(97))
# print(chr(945))



#############################

## Rebanadas

# alpha = "abdefg"

# print("alpha[1:3]: ", alpha[1:3])
# print("alpha[3:]:  ", alpha[3:])
# print("alpha[:3]:  ", alpha[:3])
# print("alpha[3:-2]:", alpha[3:-2])
# print("alpha[-3:4]:", alpha[-3:4])
# print("alpha[::2]: ", alpha[::2])  # incremento!!!
# print("alpha[1::2]:", alpha[1::2]) # incremento!!!

#######################

# # in or not in

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# print('"f" in alphabet:  ',"f" in alphabet)
# print('"F" in alphabet:  ',"F" in alphabet)
# print('"1" in alphabet:  ',"1" in alphabet)
# print('"ghi" in alphabet:',"ghi" in alphabet)
# print('"Xyz" in alphabet:',"Xyz" in alphabet)


# print('"f" not in alphabet:  ',"f" not in alphabet)
# print('"F" not in alphabet:  ',"F" not in alphabet)
# print('"1" not in alphabet:  ',"1" not in alphabet)
# print('"ghi" not in alphabet:',"ghi" not in alphabet)
# print('"Xyz" not in alphabet:',"Xyz" not in alphabet)

################################


# solicitamos una clave de cifrado entre 1 y 10
# solicitamos una cadena
# y la ciframos con la clave de cifrado introducida
# después la desciframos de nuevo con la misma clave para volver a mostrar el mensaje descifrado

# # Define una función para cifrar un mensaje
# def cifrar(mensaje, clave):
#     mensaje_cifrado = ""
#     for char in mensaje:
#         mensaje_cifrado += chr(ord(char) + clave)
#     return mensaje_cifrado

# # Define una función para descifrar un mensaje
# def descifrar(mensaje_cifrado, clave):
#     mensaje_descifrado = ""
#     for char in mensaje_cifrado:
#         mensaje_descifrado += chr(ord(char) - clave)
#     return mensaje_descifrado

# # Solicita una clave al usuario
# clave = int(input("Por favor, introduce una clave de cifrado entre 1 y 10: "))

# # Solicita un mensaje al usuario
# mensaje = input("Por favor, introduce un mensaje para cifrar: ")

# # Cifra el mensaje
# mensaje_cifrado = cifrar(mensaje, clave)
# print(f"El mensaje cifrado es: {mensaje_cifrado}")

# # Descifra el mensaje
# mensaje_descifrado = descifrar(mensaje_cifrado, clave)
# print(f"El mensaje descifrado es: {mensaje_descifrado}")


###########

# mensaje_original = input ('Introduce una cadena de caracteres: ')
# clave_cifrado = int(input('Introduce la clave de cifrado (1-10): '))

# def cifrar(mensaje, clave):
#     mensaje_cifrado = ''
#     for caracter in mensaje:
#         mensaje_cifrado += chr(ord(caracter) + clave)
#     return mensaje_cifrado

# def descifrar(mensaje, clave):
#     mensaje_descifrado = ''
#     for caracter in mensaje:
#         mensaje_descifrado += chr(ord(caracter) - clave)
#     return mensaje_descifrado


# # Cifrar
# cifrado = cifrar(mensaje_original, clave_cifrado)
# print('Cifrado:    -->' , cifrado)

# # Descifrar
# descifrado = descifrar(cifrado, clave_cifrado)
# print('Descifrado: -->' , descifrado)

##################################################
# # Cifrado César.
# text = input("Ingresa tu mensaje: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)

# print(cipher)

##################

# # Cifrado César - descifrar un mensaje.
# cipher = input('Ingresa tu criptograma: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)

# print(text)



###################################################

# # Busqueda de indices de un caracter

# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)
    

######################################################

# 1. Algunos de los métodos que ofrecen las cadenas son:

# capitalize(): cambia todas las letras de la cadena a mayúsculas.
# center(): centra la cadena dentro de una longitud conocida.
# count(): cuenta las ocurrencias de un carácter dado.
# join(): une todos los elementos de una tupla/lista en una cadena.
# lower(): convierte todas las letras de la cadena en minúsculas.
# lstrip(): elimina los caracteres en blanco al principio de la cadena.
# replace(): reemplaza una subcadena dada con otra.
# rfind(): encuentra una subcadena comenzando por el final de la cadena.
# rstrip(): elimina los caracteres en blanco al final de la cadena.
# split(): divide la cadena en una subcadena usando un delimitador dado.
# strip(): elimina los espacios en blanco iniciales y finales.
# swapcase(): intercambia las mayúsculas y minúsculas de las letras.
# title(): hace que la primera letra de cada palabra sea mayúscula.
# upper(): convierte todas las letras de la cadena en letras mayúsculas.

# 2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

# endswith(): ¿La cadena termina con una subcadena determinada?
# isalnum(): ¿La cadena consta solo de letras y dígitos?
# isalpha(): ¿La cadena consta solo de letras?
# islower(): ¿La cadena consta solo de letras minúsculas?
# isspace(): ¿La cadena consta solo de espacios en blanco?
# isupper(): ¿La cadena consta solo de letras mayúsculas?
# startswith(): ¿La cadena consta solo de letras mayúsculas?

###################################################

# # Método lstrip de Strings. Elimina por la izquierda.

# print("www.cisco.com".lstrip(".w"))

# print("wa ww. cisco.com".lstrip(".a w")) # !!!!!!!!!!!!!!!!!!!!!!!

# print("pythoninstitute.org".lstrip(".org"))

# print("gro.pythoninstitute.org".lstrip(".org")) # !!!!!!!!!!!!!!!!!!!!!!!!

#######################################

# # Demostración del método rfind(): Elimina por la derecha.

# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau tau".rfind("ta", 3, 9))

#########################################

# # Demostración del método replace():

# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))

# El tercer argumento indica cuantos reemplazos puede haber

# print("This is it!".replace("is", "are", 1))
# print("This is it!".replace("is", "are", 2))


#########################################

# # Demostración del método split():

# print("phi       chi\npsi".split())

# ####

# registro = "nombre, apellido, salario, direccion"

# lista = registro.split(',')

# print(lista)

####################################

# # Demostración del método startswith():
# print("omega".startswith("meg"))
# print("omega".startswith("om"))

# print()

# # Demostración del método strip():
# print("[" + "   aleph   ".strip() + "]")

###################

# # Demostración del método swapcase():
# print("Yo sé que no sé nada.".swapcase())

# print()

# # Demostración del método title():
# print("Yo sé que no sé nada. Part 1.".title())

# print()

# # Demostración del método upper():
# print("Yo sé que no sé nada. Part 2.".upper())

#############################

# Escenario
# Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

# Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

# Debe aceptar únicamente un argumento: una cadena.
# Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
# Si la cadena está vacía, la función debería devolver una lista vacía.
# Su nombre debe ser mysplit().
# Utiliza la plantilla en el editor. Prueba tu código con cuidado.


# Solicitar cadena de caracteres
# Variable de tipo vacia
# variable palabra=''

# Crear función mysplit()
#   Bucle for para procesar cada caracter
#   si el caracter es una letra o digito, entonces lo almaceno en la variable palabra
#   iremos acumulando en esa variable los caracteres hasta encontrar un espacio
#   si el caracter es un espacio, entonces guardar esa variable como elemento de la lista
#   y volver a empezar.

# def mysplit(strng):
#     # devolver [] si la cadena está vacía o solo contiene espacios en blanco
#     if strng == '' or strng.isspace():
#         return [ ]
#     # preparar una lista para devolver
#     lst = []
#     # preparar una palabra para construir palabras subsecuentes
#     word = ''
#     # verificar si actualmente estamos dentro de una palabra (es decir, si la cadena comienza con una palabra)
#     inword = not strng[0].isspace()
#     # iterar a través de todos los caracteres en cadena
#     for x in strng:
#          # si actualmente estamos dentro de una cadena ...
#         if inword:
#             # ... y el carácter actual no es un espacio ...
#             if not x.isspace():
#                 # ... actualizar palabra actual
#                 word = word + x
#             else:
#                 # ... de lo contrario, llegamos al final de la palabra, por lo que debemos agregarla a la lista ...
#                 lst.append(word)
#                 # ... y señalar que estamos ahora fuera de la palabra
#                 inword = False
#         else:
#             # si estamos fuera de la palabra y llegamos a un carácter no que no es un espacio en blanco
#             if not x.isspace():
#                 # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y ...
#                 inword = True
#                  # ... almacenar la primera letra de la nueva palabra
#                 word = x
#             else:
#                 pass
#        # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
#     if inword:
#         lst.append(word)
#     # devolver la lista a invocador
#     return lst

# print(mysplit("Ser o no ser, esa es la pregunta"))
# print(mysplit("Ser o no ser,esa es la pregunta"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

############

# def mysplit(cadena):
#     lista = []
#     palabra = ""
#     for caracter in cadena:
#         if caracter.isalnum():
#             palabra += caracter
#         elif palabra != '':         
#             lista.append(palabra)
#             palabra = ""

#     # ya hemos recorrido todos los caracteres y hay que añadir la última palabra
#     if palabra != '':
#         lista.append(palabra)
    
#     print(lista)

# cadena_original = input("Inroduce una cadena de caracteres: ")
# mysplit(cadena_original)
# def mysplit(cadena):
#     lista = []
#     palabra = ""
#     for caracter in cadena:
#         if caracter.isalnum():
#             palabra += caracter
#         elif palabra != '':         
#             lista.append(palabra)
#             palabra = ""

#     # ya hemos recorrido todos los caracteres y hay que añadir la última palabra
#     if palabra != '':
#         lista.append(palabra)
    
#     return lista

# cadena_original = input("Inroduce una cadena de caracteres: ")
# print(mysplit(cadena_original))

###############################################################

# # Demostración de la función sorted():
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)

# print(first_greek)
# print(first_greek_2)

# print()

# # Demostración del método sort():
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()
# print(second_greek)

############################################

# # Ordenamiento

# # Demostración de la función sorted():
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)

# print(first_greek)
# print(first_greek_2)

# print()

# # Demostración del método sort():
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()
# print(second_greek)


###############################################

# Escenario
# Seguramente has visto un display de siete segmentos.

# Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia: https://en.wikipedia.org/wiki/Seven-segment_display.

# Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

# Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:
    
# Nota: el número 8 muestra todas las luces LED encendidas.

# Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

# Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.


# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]


# def print_number(num):
# 	global digits
# 	digs = str(num)
# 	lines = [ '' for lin in range(5) ]
# 	for d in digs:
# 		segs = [ [' ',' ',' '] for lin in range(5) ]
# 		ptrn = digits[ord(d) - ord('0')]
# 		if ptrn[0] == '1':
# 			segs[0][0] = segs[0][1] = segs[0][2] = '#'
# 		if ptrn[1] == '1':
# 			segs[0][2] = segs[1][2] = segs[2][2] = '#'
# 		if ptrn[2] == '1':
# 			segs[2][2] = segs[3][2] = segs[4][2] = '#'
# 		if ptrn[3] == '1':
# 			segs[4][0] = segs[4][1] = segs[4][2] = '#'
# 		if ptrn[4] == '1':
# 			segs[2][0] = segs[3][0] = segs[4][0] = '#'
# 		if ptrn[5] == '1':
# 			segs[0][0] = segs[1][0] = segs[2][0] = '#'
# 		if ptrn[6] == '1':
# 			segs[2][0] = segs[2][1] = segs[2][2] = '#'
# 		for lin in range(5):
# 			lines[lin] += ''.join(segs[lin]) + ' '
# 	for lin in lines:
# 		print(lin)


# print_number(int(input("Ingresa el número que deseas mostrar: ")))

################
# Otra alternativa

# digits = [
# 	  "111101101101111"		# 0
# 	, "001001001001001"		# 1
# 	, "111001111100111"		# 2
# 	, "111001111001111"		# 3
# 	, "101101111001001"		# 4
# 	, "111100111001111"		# 5
# 	, "100100111101111"		# 6
# 	, "111001001001001"		# 7
# 	, "111101111101111"		# 8
# 	, "111101111001001"		# 9
# ]

# # 0 <= n <= 9
# def printedNumber( n, ch = "#" ):
# 	out = ""
# 	shape = digits[ n ]
# 	count = 0
# 	for i in shape:
# 		match i:
# 			case "1":
# 				out += ch
# 			case "0":
# 				out += " "
# 			case _:
# 				pass
# 		count += 1
# 		if count % 3 == 0:
# 			out += "\n"
# 	return out
# def printedNumberLine( ch, *args ):
# 	out = ""
# 	total_n = len( args )
# 	if total_n <= 0:
# 		return ""
# 	for i in range(5):
# 		for n in args:
# 			shape = digits[ n ]
# 			for q in range(3):
# 				if shape[ i*3 + q ] == "1":
# 					out += ch
# 				else:
# 					out += " "
# 			out += " "
# 		out += "\n"
# 	return out
	

# if __name__ == "__main__":
# 	for i in range( 10 ):
# 		print( printedNumber( i ) )
# 		print()

# 	print( printedNumberLine( "#", 1, 2, 3 ) )
  
  
#######################################################

# #Procesador de Números.

# line = input("Ingresa una línea de números, sepáralos con espacios: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("El total es:", total)
# except:
#     print(substr, "no es un numero.")


##################################

# # Validador IBAN.

# iban = input("Ingresa un IBAN, por favor: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("Has introducido caracteres no válidos.")
# elif len(iban) < 15:
#     print("El IBAN ingresado es demasiado corto.")
# elif len(iban) > 31:
#     print("El IBAN ingresado es demasiado largo.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("El IBAN ingresado es válido.")
#     else:
#         print("El IBAN ingresado no es válido.")

#######################################

# # Pruebas con las excepciones

# class MiExcepcionPersonalizada(Exception):
#     pass

# ####

# def fun1():
#     try:
#         fun2()
#     except MiExcepcionPersonalizada:
#         print('Capturando la excepción en fun1()')

# def fun2():
#     try:
#         fun3()
#     except ZeroDivisionError:
#         print('Capturando la excepción en fun2()')
#         raise MiExcepcionPersonalizada()

# def fun3():
#     try:
#         fun4()
#     except ZeroDivisionError:
#         print('Capturando la excepción en fun3()')
#         raise

# def fun4():
#     return 10 / 0

# ####
# fun1()

########################################################

# try:
#     print("1")
#     x = 1 / 0
#     print("2")
# except:
#     print("Oh cielos, algo salió mal...")

# print("3")


#######################################################

# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")


# #####

# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("No puedes dividir entre cero, lo siento.")
# except ValueError:
#     print("Debes ingresar un valor entero.")
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")


####

# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
#     print(y)
# except ValueError:
#     print("Debes ingresar un valor entero.")
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")


# ####

# try:
#     x = int(input("Ingresa un número: "))
#     y = 1 / x
#     print(y)
# except ValueError:
#     print("Debes ingresar un valor entero.")

# print("FIN.")

# ########

# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("¡División entre Cero!")
# except ArithmeticError:
#     print("¡Problema Aritmético!")

# print("FIN.")

#######

# Manejar excepción dentro de una función

# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print("¡Problema Aritmético!")
#     return None

# bad_fun(0)

# print("FIN.")

#######

# Manejar excepción fuera de una función

# def bad_fun(n):
#     raise ZeroDivisionError


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¿Que pasó? ¿Un error?")

# print("FIN.")


##############################################################################

# Provocar excepciones específicas como si fuerse generada de manera natural:

# def bad_fun(n):
#     raise ZeroDivisionError


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¿Que pasó? ¿Un error?")

# print("FIN.")


# ########

# # Si se usa raise solo, vuelve a generar la execpción y propagarla.

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("¡Lo hice otra vez!")
#         raise


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¡Ya veo!")

# print("FIN.")


####################################################

# assert, identifica el punto donde se ejecuta un error
# No reemplazan a las excepciones ni validan datos.

# import math

# x = float(input("Ingresa un número: "))
# assert x >= 0.0

# x = math.sqrt(x)

# print(x)

#--------------------------------------#
# Traceback (most recent call last):
#   File ".main.py", line 4, in 
#     assert x >= 0.0
# AssertionError
#--------------------------------------#

###########################################################

# # Este código no puede ser terminado
# # presionando Ctrl-C.

# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("¡No hagas eso!")


##################################

# # Este código causa la excepción MemoryError.
# # Advertencia: el ejecutar este código puede afectar tu Sistema Operativo.
# # ¡No lo ejecutes en entornos de producción!

# string = 'x'
# try:
#     while True:
#         string = string + string
#         print(len(string))
# except MemoryError:
#     print('¡Esto no es gracioso!')


####################################################

# def read_int(prompt, min, max):
#     ok = False
#     while not ok:
#         try:
#             value = int(input(prompt))
#             ok = True
#         except ValueError:
#             print("Error: entrada incorrecta")
#         if ok:
#             ok = value >= min and value <= max
#         if not ok:
#             print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
#     return value;

###############

# # Más efectivo

# def read_int(mensaje, minimo, maximo):
#     while True:
#         try:
#             valor = int(input(mensaje))
#             if valor >= minimo and valor <= maximo: # if min_val <= value <= max_val:
#                 return valor
#             else:
#                 print("Error: el valor no está dentro del rango permitido",minimo,"a",maximo)
#         except ValueError:
#             print("Error: entrada incorrecta")


# v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

# print("El número es:", v)

############################################################

# 1. Algunas excepciones integradas abstractas de Python son:

# ArithmeticError.
# BaseException.
# LookupError.

# 2. Algunas excepciones integradas concretas de Python son:

# AssertionError.
# ImportError.
# IndexError.
# KeyboardInterrupt.
# KeyError.
# MemoryError.
# OverflowError.

###################################


