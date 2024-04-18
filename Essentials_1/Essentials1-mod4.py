# print("Ingresa un valor: ")
# a = int(input())

# print("Ingresa un valor: ")
# b = int(input())

# print("Ingresa un valor: ")
# c = int(input())

# En modo función para eliminar código repetido

# def message():
#     print("Ingresa un valor: ")
#     return int(input())
    

# a = message()

# b = message()

# c = message()

# print(a,b,c)

###############################


# def message():
#     print("Ingresa un valor: ")

# print("Se comienza aquí.")
# message()
# print("Se termina aquí.")

######################################################

# Una función que reciba una cadena de caracteres y la devuelva invertida

# def invertir(cadena):
#     return cadena[::-1]


# texto = input("Introduce una cadena de texto: ")
# print(invertir(texto))

####################################################

# Javier

# def invertir(cadena):

#     lista=[]
    
#     for i in cadena:
#         lista.append(i)
#     lista.reverse()
#     print(lista)

# invertir(input("Ingrese cualquier cadena de caracteres: "))

################################
# def invertir(mensaje):            
    
#     mensaje_invertido = ''

#     for letra in mensaje:
#         mensaje_invertido = letra + mensaje_invertido
#         # print(mensaje_invertido)
    
#     return mensaje_invertido

####################################

# def invertir(palabra):
   
#    for indice in range(len(palabra)):
#      print(palabra[len(palabra) - indice -1], end="")
   
# cadena = input("introduce una palabra ")
# invertir(cadena)

######################################


# def funcion(mes, dia):
#     print('mes:', mes)
#     print('dia:', dia)

# #########################################

# var1 = 12
# var2 = 4

# funcion(12, 4)

# funcion(mes = 12, dia = 4)

################################

# def funcion(p1, p2, p3 = 333, p4 = 444, p5 = 555):       

#     print(p1,p2,p3,p4,p5,sep=' --- ')
# #########################################


# funcion(1,2,3,4,5)                                  # por posición
# funcion(p1 = 1, p2 = 2, p3 = 3, p4 = 4, p5 = 5)     # por palabra clave
# funcion(1,2, p3 = 3, p4 = 4, p5 = 5)                # por combinación de los métodos anteriores

# funcion(1,2, p4 = 4)                                # por combinación de los métodos anteriores


# ###################################################

# def funcion_con_retorno():       
#     return 'valor devuelto por la funcion'

# def funcion_sin_retorno():       
#     pass

# #########################################

# resultado = funcion_con_retorno()
# print(resultado)

# resultado = funcion_sin_retorno()
# print(resultado)

# ##############################

# def funcion_sin_retorno():   

#     print('mensaje generado desde el cuerpo de la función')

#     if 1 == 1:
#         return
    
#     print('otro mensaje generado desde el cuerpo de la función')



# funcion_sin_retorno()

#####################################

# def list_sum(lst):
    
#     if type(lst).__name__ != 'list':
#         print("No es una lista")
#         return
#     s = 0
    
#     for elem in lst:
#         s += elem
    
#     return s

# print(list_sum(5))

####################################

# 4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones

# def is_year_leap(year):

#     if year >= 1582:
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400 == 0:
#                     return True
#                 else:
#                     return False
#             else:
#                 return True
#         else:
#             return False

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Fallido")
  
############################################

# 4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones

# def is_year_leap(year):
#     if year >= 1582:
#             if year % 4 == 0:
#                 if year % 100 == 0:
#                     if year % 400 == 0:
#                         return True
#                     else:
#                         return False
#                 else:
#                     return True
#             else:
#                 return False

# def days_in_month(year, month):
#     if month < 1 or month > 12:
#         return None
#     else:
#         dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         mes = dias_meses[month - 1]
#         if month == 2 and is_year_leap(year):
#             mes = 29
#         return mes
        

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Fallido")


#######################################################

# # 4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones

# def is_year_leap(year):
#     if year >= 1582:
#                 if year % 4 == 0:
#                     if year % 100 == 0:
#                         if year % 400 == 0:
#                             return True
#                         else:
#                             return False
#                     else:
#                         return True
#                 else:
#                     return False

# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     else:
#         dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         # dias_meses = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         mes = dias_meses[month - 1]
#         if month == 2 and is_year_leap(year):
#             mes = 29
#         return mes

# def day_of_year(year, month, day):
    
#     dias = 0
    
#     for days_in_month in range(1, month): # ej dic, month sería 11
#         dias_mes_actual = days_in_month(year, days_in_month)
#         if days_in_month == None:
#             return None
#         dias += dias_mes_actual
    
#     dias_mes_actual = day_of_year(year, month)
    
#     if day >= 1 and day <= days_in_month:
#         print("Sumando",day,"días restantes del mes actual")
#         return dias + day
#     else:
#         return None
        
        
        

# print(day_of_year(2000, 12, 31))


#######################

# def es_bisiesto(año):
#     if año < 1582:
#         return False
    
#     if año % 4:
#         return False
#     elif año % 100:
#         return True
#     elif año % 400:
#           return False
#     else:
#           return True

# def dias_del_mes(año, mes):
#     if año < 1582 or mes < 1 or mes > 12:
#         print('Año o mes inválidos')
#         return None
      
#     dias = [31, 29 if es_bisiesto(año) else 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     resultado  = dias[mes - 1]

#     # if mes == 2 and es_bisiesto(año):
#     #     resultado = 29
    
#     return resultado
# def dia_del_año(año, mes, dia):
#     dias = 0
#     for mes_actual in range(1, mes):
#           dias_mes_actual = dias_del_mes(año, mes_actual)
          
#           if dias_mes_actual == None:
#               return None
          
#           dias += dias_mes_actual

#     dias_mes_actual = dias_del_mes(año, mes)
    
#     if dia >= 1 and dia <= dias_mes_actual:
#         #   print("Sumando",dia, "días restantes del mes actual ")
#           return dias + dia
#     else:
#          return None

# print("Día del año", dia_del_año(2000, 2, 2))

# print("Día del año", dia_del_año(2000, 12, 31))

# ###############################

# def is_year_leap(year):
# 	if year % 4 != 0:
# 		return False
# 	elif year % 100 != 0:
# 		return True
# 	elif year % 400 != 0:
# 		return False
# 	else:
# 		return True

# def days_in_month(year, month):
# 	if year < 1582 or month < 1 or month > 12:
# 		return None
# 	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	res  = days[month - 1]
# 	if month == 2 and is_year_leap(year):
# 		res = 29
# 	return res

# def day_of_year(year, month, day):
# 	days = 0
# 	for m in range(1, month):
# 		md = days_in_month(year, m)
# 		if md == None:
# 			return None
# 		days += md
# 	md = days_in_month(year, month)
# 	if day >= 1 and day <= md:
# 		return days + day
# 	else:
# 		return None

# print(day_of_year(2000, 12, 31))

###################################################

# Números Primos

# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()


#####

# def is_prime(num):
#     for i in range(2, int(num)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 100):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

#############################################

# 1 milla (mile) = 1609.344 metros(metres)
# 1 galón (gallon) = 3.785411784 litros(litres)
    
# def liters_100km_to_miles_gallon(litres):
#     gallons = litres / 3.785411784
#     miles = 100 * 1000 / 1609.344
#     return miles / gallons

# def miles_gallon_to_liters_100km(miles):
#     km100 = miles * 1609.344 / 1000 / 100
#     litres = 3.785411784
#     return litres / km100

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


########################################

# def my_function():
#     global var # Con global podemos hacer que la variable interna tenga alcance global
#     var = 2
#     print("¿Conozco a aquella variable?", var)


# #var = 1
# my_function()
# print(var)

#########################

## los valores de dentro NO son visibles desde fuera

# def scope_test():
#     x = 123


# scope_test()
# print(x)

#############
## los valores de fuera SI son visibles desde dentro

# def my_function():
#     print("¿Conozco a la variable?", var)

# var = 1
# my_function()
# print(var)

################

# def my_function():
#     var = 2     # asignar un valor a la variable provoca la creación de otra variable var diferente!!!!!!
#     print("¿Conozco a la variable después de asignar un nuevo valor?", var)

# var = 1
# my_function()
# print(var)

# ###################

# def my_function():
#     global var  # extiende el alcance de la variable var declarada fuera de la función
#     var = 2
#     print("¿Conozco a aquella variable?", var)

# var = 1
# my_function()
# print(var)

###########################################

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range(2, n + 1):
#         print(product,'*',i,'=',product * i)
#         product *= i

#     return product


# factorial_function(5)

# ######################

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1

#     the_sum = 0

#     for i in range(3, n + 1):
#         print(elem_1, '+', elem_2 , '=', elem_1 + elem_2)
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# print(fib(10))

# ##########################

# def factorial_function(n):

#     if n < 0:
#         return None
#     if n < 2:
#         return 1

#     print("\t" * n, n, " * factorial_function(",n-1,")", sep="")
#     return n * factorial_function(n - 1)

# print(factorial_function(10))

#############################

# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)


# print(fun(25))

########################
## Las tuplas son inmutables pero los objetos que están en su interios, sí se pueden modificar
# tupla = ([1,2,3],2,3)

# tupla[0][0] = 3 # Modifica el valor 1 de la lista de la posicion 0 de la tupla.
# # tupla[2] = 4 # Error porque 3 es un primitivo que es inmutable
# print(tupla)

#######################

# lista = [1,2,3,4,5]

# tupla = (lista, 22, 33)

# tupla[0][:2] = "nuevo valor"

# del tupla[0][3]

# print(tupla)

##########################

# # Diccionarios

# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}

# print(dictionary["gato"])
# print(phone_numbers['Suzy'])

# dictionary["leon"] = "Lion" # Crea una clave y valor nuevas
# dictionary["gato"] = "cat" # Modifica el valor de la clave porque existe la clave

# print(dictionary) 
# ####################

# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

# # lista de claves mediante .keys()
# for key in sorted(dictionary.keys()):
#     print(key, "->", dictionary[key])

# # lista de valores mediante .values()
# for french in dictionary.values():
#     print(french)

# # lista de tuplas con (clave, valor)  mediante .items()
# for spanish, french in dictionary.items():
#     print(spanish, "->", french)
    
    
# ##########################################

# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
#         break
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)
    
#############################
# Mismo código pero más eficiente cambiando la tupla por una lista

# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
#         break
#     if name in school_class:
#         school_class[name].append(score) # Añade elementos a la lista existente
#     else:
#         school_class[name] = [score]
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)
    
####################################

# # Vamos pedir nombres y salarios y guardar en un diccionario

# # Dividir el salrio entre 1000
# # Cesar: 25000 / 1000 --> 25
# # Marta: 37500
# # Jorge: 45000

# # Imprimir tantos asteriscos como el salario dividido entre 1000
# # y ordenar de menor a mayor
# # Cesar * 25 asteriscos
# # Ordenar de menor a mayor

# trabajadores = {}

# # Añado los empleados y el sueldo
# while True:
#     nombre = input("Introduce el nombre del trabajador: ")
#     if nombre == "":
#         break
#     salario = int(input("Introduce el salario: "))
#     trabajadores[nombre] = salario

# # # Ordenar el diccionario por salario
# # diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda elemento: elemento[1], reverse = True))


# # Divido los salarios

# for nombre in trabajadores:
#     trabajadores[nombre] //= 1000
#     print(nombre, "*" * trabajadores[nombre] )
    

################################

# diccionario = {}

# # Pedir datos
# while True:
#     nombre = input('Introduce el nombre del empleado: ')
    
#     if nombre == '':
#         break

#     salario = float(input('Introduce el salario del empleado: '))

#     diccionario[nombre] = salario

# # Ordenar el diccionario por salario
# diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda tupla: tupla[1], reverse = True))

# # Imprimir
# for nombre, salario in diccionario_ordenado.items():
#     print('Salario de', nombre.ljust(15, ' '), '-->', '*' * int(salario // 1000))
    

###############################
# x1= 1
# x2 = 2
# x3 = 3


# tup = x1, x2, x3  # empaquetado de tupla
# a, b, c = tup     # desempaquetado de tupla

# print(a * b * c)

###################################

# my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
# print(my_tuple)

# my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
# print(my_list)

###################################

# # Excepciones

# try:
#     value = int(input('Ingresa un número natural: '))
#     print('El recíproco de', value, 'es', 1 / value)

# except ValueError:
#     print('Has introducido algo que no puede convertirse a entero')
# except ZeroDivisionError:
#     print('Has intentado dividir por cero')
# except:
#     print('Ha fallado alguna otra cosa')

# print('Otra instrucción')

################################################

# try:
#     value = input('Ingresa un número natural: ')
#     value = int(value)
#     print('El recíproco de', value, 'es', 1 / value)

# except ValueError:
#     print('Has introducido el valor' , value, 'que no puede convertirse a entero')
# except ZeroDivisionError:
#     print('Has intentado dividir por cero')
# except:
#     print('Ha fallado alguna otra cosa')

# print('Otra instrucción')

# # Otra forma

# while True:
#     try:
#         value = input('Ingresa un número natural: ')
#         value = int(value)
#         print('El recíproco de', value, 'es', 1 / value)
#         break
#     except ValueError:
#         print('Has introducido el valor' , value, 'que no puede convertirse a entero.')
#     except ZeroDivisionError:
#         print('Has intentado dividir por cero.')
#     except:
#         print('Ha fallado alguna otra cosa.')
        
## Con funcion recursiva

# def calcular_reciproco():
#     try:
#         numero = input("introduce un numero natural: ")
#         numero = int(numero)
#         print("El recíproco de este numero es ", 1/numero)
#     except ValueError:
#         print('Has introducido el valor' , numero, 'que no puede convertirse a entero.')
#         calcular_reciproco()
#     except ZeroDivisionError:
#         print('Has intentado dividir por cero.')
#         calcular_reciproco()
#     except:
#         calcular_reciproco()
# ##
# calcular_reciproco()


##########################

# def es_bisiesto(año):
#     if año < 1582:
#         return False
    
#     if año % 4:
#         return False
#     elif año % 100:
#         return True
#     elif año % 400:
#           return False
#     else:
#           return True
# def dias_del_mes(año, mes):
#     if año < 1582 or mes < 1 or mes > 12:
#         print('Año o mes inválidos')
#         return None
#     dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     resultado  = dias[mes - 1]
#     if mes == 2 and es_bisiesto(año):
#         resultado = 29
    
#     return resultado
# def dia_del_año(año, mes, dia):
#     dias = 0
#     for mes_actual in range(1, mes):
#           dias_mes_actual = dias_del_mes(año, mes_actual)
#           if dias_mes_actual == None:
#               return None
#           dias += dias_mes_actual
    
#     dias_mes_actual = dias_del_mes(año, mes)
    
#     if dia >= 1 and dia <= dias_mes_actual:
#           print("Sumando",dia, "días restantes del mes actual ")
#           return dias + dia
#     else:
#          return None

# print("Día del año", dia_del_año(2000, 2, 2))


########################
# Tic tac toe

# def DisplayBoard(board):
#     # La función acepta un parámetro el cual contiene el estado actual del tablero
#     # y lo muestra en la consola.

# def EnterMove(board):
#     # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
#     # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

# def MakeListOfFreeFields(board):
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

# def VictoryFor(board, sign):
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

# def DrawMove(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.






from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado


def make_list_of_free_fields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # itera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free


def victory_for(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'me'	# Si, es la maquina
	elif sgn == "O": # ... ¿o estamos buscando O?
		who = 'you'	# Si, es el usuario
	else:
		who = None	# ¡No debemos de caer aquí!
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("¡Has ganado!")
elif victor == 'me':
	print("¡He ganado!")
else:
	print("¡Empate!")


##########################