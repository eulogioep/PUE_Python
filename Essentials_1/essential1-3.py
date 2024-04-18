# Prioridad	Operador	
# 1	~, +, -	unario
# 2	**	
# 3	*, /, //, %	
# 4	+, -	binario
# 5	<<, >>	
# 6	<, <=, >, >=	
# 7	==, !=	
# 8	&	
# 9	|	
# 10 =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

# print(int(input("Introduce un número: ")) >= 100)

# print("¿n es mayor o igual que 100?", int(input('Valor N ')) >= 100)


# n = int(input("introduce un número: "))

# if n<0:
#     print("El número es negativo")
# elif n == 0:
#     print("El número es 0")
# else:
#     print("El número es mayor a 0")
    
# numero = int(input("Introduce un número: "))


# resultado = 'Positivo' if numero > 0 else 'Negativo o igual a cero'

# print(resultado)

# numero = int(input("Introduce un número: "))


# resultado = 'Positivo' if numero > 0 else ('Negativo' if numero < 0  else 'Igual a cero')

# print(numero,'es',resultado)

# # Se leen tres números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# # Asumimos temporalmente que el primer número
# # es el más grande.
# # Lo verificaremos pronto.
# largest_number = number1

# # Comprobamos si el segundo número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number2 > largest_number:
#     largest_number = number2

# # Comprobamos si el tercer número es más grande que el mayor número actual
# # y actualiza el número más grande si es necesario.
# if number3 > largest_number:
#     largest_number = number3

# # Imprime el resultado.
# print("El número más grande es:", largest_number)

# # Se leen tres números.
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))

# # Verifica cuál de los números es el mayor
# # y pásalo a la variable largest_number
    
# largest_number = max(number1, number2, number3)

# # Imprime el resultado.
# print("El número más grande es:", largest_number)

# entrada = input("Introduce el nombre de la flor: ")

# if entrada == "ESPATIFILIO":
#     print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
# elif entrada == "espatifilo":
#     print("No, ¡quiero un gran ESPATIFILIO!")
# else:
#     print("!ESPATIFILIO!, ¡No", entrada + "!")


# income = float(input("Introduce el ingreso anual: "))

# if income <= 85528:
# 	tax = (income * 0.18) - 556.02
# else:
# 	tax = ((income - 85528) * 0.32) + 14839.02

# ## if tax < 0.0:
# ## tax = 0.0



# tax = round(max(tax,0),0)
# print("El impuesto es:", tax, "pesos")


# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No dentro del período del calendario Gregoriano")
# else:
# 	if year % 4:
# 		print("Año Común")
# 	elif year % 100:
# 		print("Año Bisiesto")
# 	elif year % 400:
# 		print("Año Común")
# 	else:
# 		print("Año Bisiesto")
  
# numero = 54321.12345

# print(int(round(numero,-3)))
# print(round(numero,-2))
# print(round(numero,-1))
# print(round(numero,0))
# print(round(numero,1))
# print(round(numero,2))
# print(round(numero,3))

# v1 = 10
# v2 = 20
# v3 = 30

# # vtemp = v1
# # v1 = v3
# # v3 = vtemp

# v1, v3 = v3, v1 # sintáxis de intercambio

# print(v1, v2, v3)

# numero = 1

# while numero <= 100:

#     print(numero)

#     numero += 1

# print('Terminado')

#num 1 al 10 excepto el 7 y el 9

# num = 1

# while num <= 10:
#     if num != 7 and num != 9:
#         print(num)
#     num += 1

# num = 1

# while num <= 10:
#     if num == 7 or num == 9:
#         num += 1
#     else:
#         print(num)
#         num += 1
 
# # Hace menos iteracciones
# numero = 1

# while numero <= 10:
#     print(numero)
#     numero += 1
#     if(numero == 7 or numero == 9):
#         numero += 1

# num = 1

# while num <= 10:
    
#     print(num)
#     if num != 6 and num != 8:

#         num += 1
        
#     else:
#         num += 2
    
# numero = 1

# while True:

#     print(numero)
#     numero += 1                         # incremento en 1
#     if (numero == 7 or numero == 9):
#         numero += 1                     # incremento en otro 1

#     if numero > 10:
#         break

###############

# import random

# secret_number = random.randint(1,10)

# print(
# """
# +==================================+
# | ¡Bienvenido a mi juego, muggle!  |
# | Introduce un número entero       |
# | y adivina qué número he          |
# | elegido para ti.                 |
# | Entonces,                        |
# | ¿Cuál es el número secreto?      |
# +==================================+
# """)

# user_number = int(input("Ingresa un número del 1 al 10: "))

# while user_number != secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     user_number = int(input("Ingresa un número nuevo del 1 al 10: "))

# print(secret_number, "¡Bien hecho, muggle! Eres libre ahora")

######

# import random

# numero_secreto = random.randint(1,10)

# while True:
#     numero = int(input("Intenta adivinar el número secreto: "))
#     if numero == numero_secreto:
#         print("\tBien hecho muggle!.", "Eres libre ahora!")
#         break
#     else:
#         print("\t¡Ja, ja! ¡Estás atrapado en mi bucle!")


######


# for i in range(2, 8, 3):
#     print("El valor de i es actualmente", i)


# mensaje ='Hola buenos dias'

# print(mensaje[0])
# print(mensaje[1])
# print(mensaje[2])
# print(mensaje[3])
# print(mensaje[4])
# print(mensaje[5])

# for letra in mensaje:
#     print(letra)
    
# import time

#     # Escribe un bucle for que cuente hasta cinco.
#     # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
#     # Cuerpo del bucle - usar: time.sleep (1)

# # Escribe una función de impresión con el mensaje final.

# import time

# for i in range(1,6):
#     print(i, "Mississippi")
#     time.sleep(1)

# print("¡Listos o no, ahí voy!")

# # Calcula el tiempo
# import time

# inicio = time.time()

# final = time.time()

# tiempo = final - inicio
# print('Tiempo de ejecución:', tiempo, 'segundos')

# ###########
# import time

# inicio = time.time()

# for second in range(1, 6):
#     print(second, "Mississippi")
#     time.sleep(1)
	
# print("¡Listos o no, ahí voy!")

# final = time.time()

# tiempo = final - inicio
# print('Tiempo de ejecución:', round(tiempo), 'segundos')

#####################

# while True:
#     palabra = input("¡Esto es un bucle infinito. Di la palabra mágica para salir: ")
#     if palabra == "chupacabra":
#         break
# print("¡Has dejado el bucle con éxito!")

#####################################

# user_word = input("Ingresa tu palabra: ")upper()
## user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
#     else:
#         print(letter)

####################################

# word_without_vowels = ""

# user_word = input("Ingresa tu palabra: ").upper()
# # user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
#     else:
#         word_without_vowels += letter
		
# print(word_without_vowels)

###################################

# blocks = int(input("Indica la cantidad de bloques: "))
# height = 0
# capa = 1
# while capa <= blocks:
#     height += 1
#     blocks -= capa
#     capa += 1
# else:
#     print("No hay suficientes bloques para una nueva capa")

# print("La altura de la pirámide es:", height, "y han sobrado:", blocks,"bloques.")

#######################################
# bloques = int(input("Ingrese el número de bloques: "))
# altura = 0

# if bloques <= 0:
#     print("Debes introducir al menos un bloque para la pirámide")
# else:
#     while altura < bloques:
        
#         altura +=1               # incrementamos el número de niveles
#         bloques -= altura        # restamos del total el número de bloques utilizados 

#         print('Altura:',altura,'- Bloques restantes:' ,bloques)

#     print("La altura de la pirámide es de", altura, 'niveles')

####################################
# Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
# 2 Si es par, evalúa un nuevo c0 como c0 / 2.
# 3 De lo contrario, si es impar, evalúe un nuevo  c0  como c0 * 3  + 1.
# 4 Si c0 es distinto de 1, salta al punto 2.

# c0 = int(input("Introduce un número positivo y distinto de 0: "))
# pasos = 0

# if c0 > 0:
#     #print("Numero correcto")
#     while c0 != 1:
#         if c0 % 2 == 0:
#             c0 //= 2
#             print(c0)
#         elif c0%2 != 0:
#             c0 = (c0*3)+1
#             print(c0)
#         else:
#             c0 //= 2
#             print(c0)
#         pasos += 1
# else:
#     print("Numero incorrecto. El número que introduces tiene que ser mayor que 0.")

# print("Pasos utilizados:",pasos)
####################################
# c0=int(input("Introduce un número positivo diferente de cero:")) 
# while c0 <= 0:
#     print("Has introducido un valor incorrecto, vuelve a intentarlo...")
#     c0=int(input("Introduce un número positivo diferente de cero:"))
# else:
#     pasos = 0
#     while c0 != 1:
#         if c0 % 2:
#             c0 = 3*c0 + 1
#             print(c0)
#             pasos += 1
#         else:
#             c0 //= 2
#             print(c0)
#             pasos += 1
#     else:
#         print("pasos =",pasos)


####################################
## Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
## Si es par, evalúa un nuevo c0 como c0 // 2.
## De lo contrario, si es impar, evalúe un nuevo  c0  como c0 * 3  + 1
## Si c0 es distinto de 1, salta al punto 2.

# c0 = int(input("Introduce un número: "))

# pasos = 0

# while c0 > 1:               # iteramos hasta llegar al 1

#     if c0 % 2 == 0:         # si es par se divide entre 2
#         c0 = c0 // 2        # división entera
#     else:                   
#         c0 = c0 * 3 + 1     # en caso de impar se multiplica por 3 y se suma 1
        
#     pasos += 1
#     print(c0)
    
# print("pasos = ",pasos)





######################################

# # Ejercicio 1

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

# # Ejercicio 2

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# # Ejercicio 3

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end = "")

# resultado = ""
# for letra in "john.smith@pythoninstitute.org":
#     if letra == "@":
#         break
#     resultado += letra
     
# print(resultado)

# # Ejercicio 4

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end = "")
#         continue
#     print(digit, end = "")

# resultado = ""
# for digit in "0165031806510":
#     if digit != "0":
#         resultado += digit
#         continue
#     else:
#         resultado += "x"
# print(resultado)

# numero = "0165031806510"
# #numero.replace("0","x")       # Las cadenas son inmutables y hay que guardar en una nueva variable
# print(numero.replace("0","x")) # O imprimir en el print.
###############################

## Representación en binario

# print("Número 1:", "\t" * 4, bin(numero1))
# print("Número 2:", "\t" * 4, bin(numero2))

# The expression x and y first evaluates x; if x is false, 
# its value is returned; otherwise, 
# y is evaluated and the resulting value is returned.

# print("numero1 and numero2:", "\t", numero1 and numero2)

# #  AND a nivel de bits
# print("Conjunción lógica a nivel de bits (&):")
# print("numero1 & numero2:", "\t" * 2, format(numero1 & numero2 , '#032b'))

# #  OR a nivel de bits
# print("Disyucción lógica a nivel de bits (|):")
# print("numero1 | numero2:", "\t" * 2, format(numero1 | numero2 , '#032b'))

#  OR exclusivo a nivel de bits
# print("Disyucción exclusiva a nivel de bits o xor (^):")
# print("numero1 ^ numero2:", "\t" * 2, format(numero1 ^ numero2 , '#032b'))

# print("not numero1:", "\t" * 3, not numero1)

# print("~numero1:", "\t" * 4, format(~numero1, '#032b'))

########################################

flag_register = 8

the_mask = 12

print(format(the_mask, '#032b'))

