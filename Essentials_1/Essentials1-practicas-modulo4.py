######################
# Sección 4.1.1.3
######################

##  Código repetitivo

# print("Ingresa un valor: ")
# a = int(input())

# print("Ingresa un valor: ")
# b = int(input())

# print("Ingresa un valor: ")
# c = int(input())

######################
# Sección 4.1.1.3
######################

# def message(nombre):
#     print("Dentro de la función hemos recibido el valor", nombre)
    

# print("Se comienza aquí.")
# message("Cesar")
# print("Se termina aquí.")
# message()
# message()



# def message():
#     print("Ingresa un valor: ")

# message()
# a = int(input())

# message()
# b = int(input())

# message()
# c = int(input())

######################
# Sección 4.1.1.5
######################

# def message():
#     print("Ingresa un valor: ")

# message()
# a = int(input())

# message()
# b = int(input())

# message()
# c = int(input())

######################
# Sección 4.1.1.6
######################

##  Las funciones pueden aceptar parámetros

# def hello(name):            # definiendo una función con un argumento
#     print("Hola,", name)    # cuerpo de la función


# nombre = input("Ingresa tu nombre: ")

# hello(nombre)           # invocación de la función

# hello(name="César")     # invocación de la función

# hello("César")          # invocación de la función


## Las funciones pueden devolver valores

# def multiplicar(numero1, numero2):    # definiendo una función con dos argumentos
#     return numero1 * numero2

# resultado = multiplicar(2,4)

# print("El resultado de multiplicar 2 x 4 es",resultado)

######################
# Sección 4.2.1.2
######################

# def message(number):
#     print("Ingresa un número:", number)

# message(1)


## Es posible tener una variable con el mismo nombre del parámetro de la función.

## El siguiente código muestra un ejemplo de esto:

# def message(number):
#     print("Ingresa un número:", number)

# number = 1234

# message(number)

# number = 4321
# print(number)

######################
# Sección 4.2.1.3
######################

# def message(p1, p2):
#     print("Parámetro1:", p1, "- Parámetro2:", p2)

# message("teléfono", 11)
# message("precio", 5)
# message("número", "número")

######################
# Sección 4.2.1.4
######################

# def my_function(a, b, c):
#     print(a, b, c)

# my_function(1, 2, 3)

# def introduction(first_name, last_name):
#     print("Hola, mi nombre es", first_name, last_name)

# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

######################
# Sección 4.2.1.5
######################

# def introduction(first_name, last_name):
#     print("Hola, mi nombre es", first_name, last_name)

# introduction("César", "Martín")

# introduction(first_name = "James", last_name = "Bond")

# introduction(last_name = "Skywalker", first_name = "Luke")

# introduction("Luke", last_name = "Skywalker")

######################
# Sección 4.2.1.6
######################

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)


# adding(1, 2, 3)
# adding(c = 1, a = 2, b = 3)
# adding(3, c = 1, b = 2)

# # adding(3, a = 1, b = 2) # Error!!!
# adding(4, 3, c = 2)

######################
# Sección 4.2.1.7
######################

# def introduction(first_name, last_name="González"):
#     print("Hola, mi nombre es", first_name, last_name)

# introduction("Jorge", "Pérez")
# introduction("Enrique")
# introduction(first_name="Guillermo")


# def introduction(first_name="Juan", last_name="González"):
#     print("Hola, mi nombre es", first_name, last_name)

# introduction()
# introduction("Jorge", last_name="Rodríguez")
# introduction(last_name="Rodríguez")


# def introduction(first_name, last_name="González"):
#     print("Hola, mi nombre es", first_name, last_name)
    
# introduction("Jorge", "Pérez")
# introduction("Enrique")
# introduction(first_name = "Guillermo")

######################
# Sección 4.2.1.8
######################

# # Un ejemplo de una función con un parámetro:

# def hi(name):
#     print("Hola,", name)

# hi("Greg")

# # Un ejemplo de una función de dos parámetros:

# def hi_all(name_1, name_2):
#     print("Hola,", name_2)
#     print("Hola,", name_1)

# hi_all("Sebastián", "Konrad")

# # Un ejemplo de una función de tres parámetros:

# def address(street, city, postal_code):
#     print("Tu dirección es:", street, city, postal_code)

# s = input("Calle: ")
# p_c = input("Código Postal: ")
# c = input("Ciudad: ")

# address(s, c, p_c)

# # Se puede utilizar la técnica de argumentos con palabras clave para asignar 
# # valores predefinidos a los argumentos:

# def name(first_name, last_name="Pérez"):
#     print(first_name, last_name)

# name("Andy")    # salida: Andy Pérez
# name("Bety", "Rodríguez")    # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")

# # Ejercicio 1

# # ¿Cuál es la salida del siguiente código?

# def intro(a="James Bond", b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")

# intro()

# # Ejercicio 2

# # ¿Cuál es la salida del siguiente código?

# def intro(a="James Bond", b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")

# intro(b="Sergio López")

# # Ejercicio 3

# # ¿Cuál es la salida del siguiente fragmento de código?

# def intro(a, b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")

# intro("Susan")

# # Ejercicio 4

# # ¿Cuál es la salida del siguiente código?

# def add_numbers(a, b=2, c):
#     print(a + b + c)

# add_numbers(a=1, c=3)


######################
# Sección 4.3.1.1
######################

# def happy_new_year(wishes = True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
#     if not wishes:
#         return
    
#     print("¡Feliz año nuevo!")

# # happy_new_year()
# happy_new_year(False)

# retorno = happy_new_year(False)

# if retorno is None:
#     print("La función no ha devuelto nada")
    
# print("Valor devuelto por la función:", retorno)



# def boring_function():
#     return 123

# x = boring_function()

# print("La función boring_function ha devuelto su resultado:", x)

######################
# Sección 4.3.1.2
######################

# value = None

# if value is None:
#     print("Lo siento, no contienes ningún valor")

# No olvides esto: si una función no devuelve un cierto valor utilizando 
# una cláusula de expresión return, se asume que devuelve implícitamente None.

######################
# Sección 4.3.1.3
######################

# def strange_function(n):
#     if(n % 2 == 0):
#         return True

# print("La función ha devuelto:",strange_function(2))
# print("La función ha devuelto:",strange_function(1))

######################
# Sección 4.3.1.4
######################

# def list_sum(lst):
#     s = 0
    
#     for valor in lst:
#         s += valor
    
#     return s

# print(list_sum([5, 4, 3]))

# lista_numeros = [1,2,3,4,5]

# print(list_sum(lista_numeros))

######################
# Sección 4.3.1.5
######################

# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(5))

# for valor in strange_list_fun(5):
#     print(valor)

###################################
# Sección 4.3.1.6 - Laboratorio
###################################

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

# # #############################################
# datos_test =      [ 1900, 2000, 2016, 1987 ]
# resultados_test = [False, True, True, False]

# for i in range(len(datos_test)):
#     año = datos_test[i]
#     print(año,"-> ",end="")
#     resultado = es_bisiesto(año)
#     if resultado == resultados_test[i]:     # si el resultado del año coincide con el resultado correspondiente
#           print("OK")
#     else:
#           print("Fallido")

###################################
# Sección 4.3.1.7 - Laboratorio
###################################

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
# #############################

# def dias_del_mes(año, mes):
#  	if año < 1582 or mes < 1 or mes > 12:
#           print('Año o mes inválidos')
#           return None
#  	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  	resultado  = dias[mes - 1]

#  	if mes == 2 and es_bisiesto(año):
#  		 resultado = 29
#  	return resultado
 
# ################################

# test_años =       [1900, 2000, 2016, 1987]
# test_meses =      [ 2  ,   2 ,   1 , 11  ]
# test_resultados = [ 28 ,  29 ,  31 , 30  ]

# for i in range(len(test_años)):
#  	año = test_años[i]
#  	mes = test_meses[i]
#  	print(año, mes, "-> ",end="")
#  	resultado = dias_del_mes(año, mes)
#  	if resultado == test_resultados[i]:
#  		 print("OK")
#  	else:
#  		 print("Fallido")

###################################
# Sección 4.3.1.8 - Laboratorio
###################################

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
# #############################

# def dias_del_mes(año, mes):
#  	if año < 1582 or mes < 1 or mes > 12:
#           print('Año o mes inválidos')
#           return None

#  	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  	resultado  = dias[mes - 1]

#  	if mes == 2 and es_bisiesto(año):
#  		 resultado = 29
#  	return resultado
 
# ###############################

# def dia_del_año(año, mes, dia):
#  	dias = 0

#  	for mes_actual in range(1, mes):
#           dias_mes_actual = dias_del_mes(año, mes_actual)
#           if dias_mes_actual == None:
#               return None
#           dias += dias_mes_actual
          
#  	dias_mes_actual = dias_del_mes(año, mes)
     
#  	if dia >= 1 and dia <= dias_mes_actual:
#           print("Sumando",dia, "días restantes del mes actual ")
#           return dias + dia
#  	else:
#  		 return None

# print("Día del año", dia_del_año(2000, 2, 2))

# print("Día del año", dia_del_año(2000, 12, 31))

###################################
# Sección 4.3.1.9 - Laboratorio
###################################

# def is_prime(num):
#     for i in range(2, int(num)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 100):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")




## Con raíz cuadrada

# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

###################################
# Sección 4.3.1.10 - Laboratorio
###################################

# # 1 milla (mile) = 1609.344 metros(metres)
# # 1 galón (gallon) = 3.785411784 litros(litres)
    
# def liters_100km_to_miles_gallon(litres):
#     gallons = litres / 3.785411784
#     miles = 100 * 1000 / 1609.344
#     return miles / gallons

# def miles_gallon_to_liters_100km(miles):
#     km100 = miles * 1609.344 / 1000 / 100
#     litres = 3.785411784
#     return litres / km100

###############################################
# Alternativa más concisa

# def liters_100km_to_miles_gallon(liters):
#     return 1/(liters/3.785411784*1.609344/100)

# def miles_gallon_to_liters_100km(miles):
#     return 1/(miles/3.785411784*1.609344/100)

###############################################

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))

######################
# Sección 4.1.3.11
######################

## Ejercicio 1
## ¿Cuál es la salida del siguiente fragmento de código?

# def hi():
#     return
#     print("¡Hola!")

# hi()

## Ejercicio 2
## ¿Cuál es la salida del siguiente fragmento de código?

# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False

# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))

## Ejercicio 3
## ¿Cuál es la salida del siguiente fragmento de código?

# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst

# print(even_num_lst(11))

## Ejercicio 4
## ¿Cuál es la salida del siguiente fragmento de código?

# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list

# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))

######################
# Sección 4.1.4.1
######################

# Caso 1
# Una variable definida en una función no es accesible desde fuera de la función

# def scope_test():
#     x = 123

# scope_test()
# print(x)

###################################################################################

# Caso 2
# Una variable declarada fuera de la función es visible desde dentro de la función

# x = 123
# def scope_test2():
#     print(x)

# scope_test2()

###################################################################################


#  Caso 3
# redefinición de la variable x

# x = 123

# def scope_test2():

#     x = 321     # provoca la creación de otra variable llamada x
    
#     print("Dentro de la función el valor de x es", x)    


# print("Fuera de la función el valor de x es", x)  

# scope_test2()

# print("Fuera de la función el valor de x es", x)  
  
#################################################
#  Caso 4
#  Uso de global

# x = 123

# def scope_test2():

#     global x    # extender el alcance de la variable x al cuerpo de la función
#     x = 321     # ya no se crea una segunda variable x
    
#     print(x)    

# scope_test2()

# print(x)

###################################################################################
######################
# Sección 4.4.1.2
######################

## una variable que existe fuera de una función tiene alcance 
## dentro del cuerpo de la función.

# def my_function():
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)


# Excepción a la regla!!!!!


# def my_function():
#     var = 23                               # La asignación de valor crea una nueva variable var dentro de la función 
#     # var += 2                               # La asignación de valor crea una nueva variable var dentro de la función
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)

######################
# Sección 4.4.1.3
######################

# def my_function():
#     global var                                              # acceso a la variable var declarada fuera de la función!!!
#     print("El valor de la variable en éste punto es", var)
#     var = 2                                                 # No se crea una nueva variable var!!!!
#     print("¿Conozco a aquella variable?", var)

# var = 1
# my_function()                                               # Al llamar a la función ésta modifica el valor de var
# print(var)                                                  # Por lo tanto el valor que se imprime es 2

######################
# Sección 4.4.1.4
######################

# def my_function(n):
#     print("Yo recibí", n)
#     n += 1
#     print("Ahora tengo", n)

# var = 1
# my_function(var)
# print("var tiene valor",var)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)   # Referencia a variable externa my_list_2
#     my_list_1 = [0, 1]              # Asignamos una lista nueva!!
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)   # Referencia a variable externa my_list_2

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)   # Referencia a variable externa my_list_2
#     del my_list_1[0]                # Presta atención a esta línea.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)   # Referencia a variable externa my_list_2


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

######################
# Sección 4.4.1.5
######################

# # Ejercicio 1

# # ¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

# def message():
#     alt = 1
#     print("¡Hola, mundo!")


# print(alt)


# # Ejercicio 2

# # ¿Cuál es la salida del siguiente fragmento de código?

# a = 1


# def fun():
#     a = 2
#     print(a)


# fun()
# print(a)


# # Ejercicio 3

# # ¿Cuál es la salida del siguiente fragmento de código?

# a = 1


# def fun():
#     global a
#     a = 2
#     print(a)


# fun()
# a = 3
# print(a)


# # Ejercicio 4

# # ¿Cuál es la salida del siguiente fragmento de código?

# a = 1


# def fun():
#     global a
#     a = 2
#     print(a)


# a = 3
# fun()
# print(a)

######################
# Sección 4.5.1.1
######################

## Definamos una función que calcula el Índice de Masa Corporal (IMC).

# def masa_corporal(peso, altura):
#     return peso / altura ** 2


# print(masa_corporal(52.5, 1.65))

######################
# Sección 4.5.1.2
######################

# def masa_corporal(peso, altura):
#     if altura < 1.0 or altura > 2.5 or \
#     peso < 20 or peso > 200:
#         return None

#     return peso / altura ** 2


# print(masa_corporal(352.5, 1.65))

###################################################################
# # Función para convertir de libras a kilogramos
###################################################################

# def libras_a_kilos(libras):
#     return libras * 0.45359237


# print(libras_a_kilos(1))

###################################################################
# #  Función para convertir pies y pulgadas a metros y centímetros
###################################################################

# def pies_pulgadas_a_metros_centimetros(pies, pulgadas):
#     return pies * 0.3048 + pulgadas * 0.0254


# print(pies_pulgadas_a_metros_centimetros(1, 1))


# #  Convertir 6 pies a metros

# print(pies_pulgadas_a_metros_centimetros(6, 0))

######################################################################################
# #  Crear de nuevo la función para definir un valor por defecto para las pulgadas
######################################################################################

# def pies_pulgadas_a_metros_centimetros(pies, pulgadas = 0.0):
#     return pies * 0.3048 + pulgadas * 0.0254


# print(pies_pulgadas_a_metros_centimetros(6))

############################################
############# Solución final ###############
############################################

# def pies_pulgadas_a_metros_centimetros(pies, pulgadas = 0.0):
#     return pies * 0.3048 + pulgadas * 0.0254


# def libras_a_kilogramos(libras):
#     return libras * 0.45359237


# def masa_corporal(peso, altura):
#     if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
#         return None
#     return peso / altura ** 2

# # Implementación alternativa

# def masa_corporal(peso, altura):
#     if altura > 1.0 and altura < 2.5 and peso > 20 and peso < 200:
#         return peso / altura ** 2
    
# print(masa_corporal(peso = libras_a_kilogramos(176), 
#                     altura = pies_pulgadas_a_metros_centimetros(-5, 7)))

######################
# Sección 4.5.1.3
######################

# # Ahora trabajaremos con triángulos. 
# # Comenzaremos con una función que verifique si tres lados de 
# # ciertas longitudes pueden formar un triángulo.

# # la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado

# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))


# # Versión más compacta

# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# # #  Más compacta aún

# def is_a_triangle(a, b, c):
#     return (a + b > c) and (b + c > a) and (c + a > b)

# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

######################
# Sección 4.5.1.4
######################

## Verificar si un triángulo es un triángulo rectángulo

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Ingresa la longitud del primer lado: '))
# b = float(input('Ingresa la longitud del segundo lado: '))
# c = float(input('Ingresa la longitud del tercer lado: '))

# if is_a_triangle(a, b, c):
#     print('Si, si puede ser un triángulo.')
# else:
#     print('No, no puede ser un triángulo.')

# intentaremos verificar si un triángulo es un triángulo rectángulo.

# # Para ello haremos uso del Teorema de Pitágoras:
# # c**2 = a**2 + b**2

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
    
#     if c > a and c > b:
#         print("El lado más largo (hipotenusa) es c")
#         return c ** 2 == (a ** 2 + b ** 2)    # Teorema de Pitágoras
    
#     if a > b and a > c:
#         print("El lado más largo (hipotenusa) es a")
#         return a ** 2 == (b ** 2 + c ** 2 )   # Teorema de Pitágoras
    
#     if b > a and b > c:
#         print("El lado más largo (hipotenusa) es b")
#         return b ** 2 == (a ** 2 + c ** 2)    # Teorema de Pitágoras


# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))
# print(is_a_right_triangle(4, 5, 3))

######################
# Sección 4.5.1.5
######################

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5 # Raíz cuadrada


# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)


# print(area_of_triangle(1., 1., 2. ** .5))

######################
# Sección 4.5.1.6
######################

## Cálculo de Factorial
## (El producto de todos los números naturales previos al argumento o número dado.)

# def factorial_function(numero):
#     if numero < 0:
#         return None
#     if numero < 2:
#         return 1
    
#     producto = 1
#     for contador in range(2, numero + 1):
#         print("\tMultiplicando",producto,"x", contador,"=", producto * contador)
#         producto *= contador
#     return producto

# numero = 10
# # print("Factorial de", numero, "=" ,factorial_function(numero))

# for n in range(1, 6):  # probando
#     print("Factorial de", n,"=" ,factorial_function(n))

######################
# Sección 4.5.1.7
######################

##  Secuencia de Fibonacci

# El primer elemento de la secuencia es igual a uno (Fib1 = 1).
# El segundo elemento también es igual a uno (Fib2 = 1).
# Cada número después de ellos es la suma de los dos números anteriores.

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1                          # Inicializar las dos variables a 1 
#     suma = 0                                     # Inicializar la suma a 0
    
#     for i in range(3, n + 1):
#         print("\t",elem_1,"+", elem_2,"=", elem_1 + elem_2)
#         suma = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, suma            # a elem_1 se le asigna elem_2, a elem_2 se le asigna la suma   
#     return suma

# print("Resultado:",fib(10))

# for n in range(1, 10):  # probando
#     print("Fib",n, "->", fib(n))


## Alternativa con lista

# def fn(n):
#     number_pos = n - 1
#     if(n > 0):
#         list_fib = [1,1]
#         for i in range(1,n):
#             fib_numer = list_fib[-1] + list_fib[-2] 
#             list_fib.append(fib_numer)
#         print(list_fib)
#         print(list_fib[number_pos])

# fn(10)

######################
# Sección 4.5.1.8
######################

##  Versión de Fibonacci recursiva

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
    
#     print("\tfib(",n-1,") + ","fib(",n-2,")", sep="")

#     return fib(n - 1) + fib(n - 2)


# print("Resultado:",fib(5))

# for n in range(1, 10):  # probando
#     print(n, "->", fib(n))

# ##  Versión de Factorial recursiva

# def factorial_function(n):

#     if n < 0:
#         return None
#     if n < 2:
#         return 1

#     print("\t" * n, n, " * factorial_function(",n-1,")", sep="")
#     return n * factorial_function(n - 1)

# print(factorial_function(10))

##############################
# Ejercicio Recursividad 
##############################

# nivel_recursividad = 0

# def contar_elementos(lista):
#     global nivel_recursividad
#     nivel_recursividad += 1
    
#     print('\t' * nivel_recursividad, "Ejecutando contar_elementos con parámetro", lista)
    
#     count = 0
#     for elemento in lista:
        
#         if (type(elemento) == list):
#         # equivalente
#         # if isinstance(elemento, list):
#             count += contar_elementos(elemento)
#         else:
#             count += 1
    
#     return count

######################
# Sección 4.5.1.9
######################

# # Ejercicio 1

# # ¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y por qué?

# def factorial(n):
#     return n * factorial(n - 1)


# print(factorial(4))


# # Ejercicio 2

# # ¿Cuál es la salida del siguiente fragmento de código?

# def fun(a):
#     if a > 30:
#         print("\tDevolviendo 3")
#         return 3
#     else:
#         print("\tDevolviendo ", a, " + fun(", a + 3, ")", sep="")
#         return a + fun(a + 3)

# print(fun(25))

# Comprobar y modificar el limite recursividad

# import sys

# print(sys.getrecursionlimit())  # muestra el límite inicial = 1000 (¡¡¡¡¡en Spyder 3000 por defecto!!!!!)

# sys.setrecursionlimit(2000) # fijamos a 2000

# print(sys.getrecursionlimit()) # mostramos el limite a 2000

######################
# Sección 4.6.1.1
######################

## Tuplas

# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, .125

# print(tuple_1)
# print(tuple_2)

## Tupla vacía

# empty_tuple = ()

## Tupla con un solo elemento

# one_element_tuple_1 = (1, ) # si no se utiliza la coma se tratará como una variable normal!!!
# one_element_tuple_2 = 1.,   # si no se utiliza la coma se tratará como una variable normal!!!

######################
# Sección 4.6.1.2
######################

# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])

# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)

## no intentes modificar el contenido de la tupla ¡No es una lista!

# my_tuple.append(10000)  # Falla - AttributeError
# del my_tuple[0]         # Falla - TypeError
# my_tuple[1] = -10       # Falla - TypeError

######################
# Sección 4.6.1.3
######################

# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print("Longitud de t2:",len(t2))
# print("t1:",t1)
# print("t2:",t2)
# print("10 in my_tuple:",10 in my_tuple)
# print("-10 not in my_tuple:",-10 not in my_tuple)



# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1 # Intercambios

# print(t1, t2, t3)

######################
# Sección 4.6.1.4
######################

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# phone_numbers = {'jefe': 5551234567, 
#                  'Suzy': 22657854310}

# empty_dictionary = {}

# print(dictionary)
# print("gato: ", dictionary["gato"])

# print(phone_numbers)
# print(empty_dictionary)

######################
# Sección 4.6.1.5
######################

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# phone_numbers = {'jefe' : 5551234567, 
#                   'Suzy' : 22657854310}

# empty_dictionary = {}

# print(dictionary['gato'])
# print(phone_numbers['Suzy'])
# # print(phone_numbers['presidente']) # KeyError!!!


## El siguiente código busca de manera segura palabras en francés:

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# words = ['gato', 'león', 'caballo'] # lista!!!

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "no está en el diccionario")

######################
# Sección 4.6.1.6
######################

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# ## Salida ordenada

# for key in sorted(dictionary.keys()):
#     print("Ordenada:", key, "->", dictionary[key])
  

# ##############################################################################
# # función sorted() y método sort()

# def longitud(e):
#   return len(e)

# ###########################################################################

# lista1 = ['zapatería','barca','fenómeno','cocina','dedo','armario']

# lista2 = sorted(lista1)         # crea una nueva lista

# print(lista1)
# print(lista2)

# lista2 = sorted(lista1, key = longitud, reverse = True)

# print('\nLlamando a la función sorted() con parámetros key=longitud y reverse = True:\n')

# for elemento in lista2:
#     print(elemento)
    
    
# ##############################################################################

# lista1.sort(key = longitud, reverse = True)     # no produce una nueva lista, sino que ordena la lista actual

# print('\nLlamando al método sort() con parámetro key=longitud y reverse = True:\n')

# for elemento in lista1:
#     print(elemento)



######################
# Sección 4.6.1.7
######################

## Este método regresa una lista de tuplas 
## donde cada tupla es un par de cada clave con su valor.

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# for clave, valor in dictionary.items():
#     print(clave, "->", valor)


# También existe un método denominado values(), 
# funciona de manera muy similar al de keys(), 
# pero regresa una lista de valores.

# dictionary = {"gato" : "chat", 
#               "perro" : "chien", 
#               "caballo" : "cheval"}

# for french in dictionary.values():
#     print(french)


######################
# Sección 4.6.1.8
######################

# dictionary = {'gato': 'minou', 
#               'perro': 'chien', 
#               'caballo': 'cheval'}

## Actualización de valores

# dictionary['gato'] = 'minou'
# print(dictionary)

## Inserción de nuevos elementos

# dictionary['cisne'] = 'cygne'
# print(dictionary)

## Eliminación de elementos

# del dictionary['perro']

## Para eliminar el ultimo elemento de la lista, 
## se puede emplear el método popitem():

# dictionary.popitem()
# print(dictionary)    

######################
# Sección 4.6.1.9
######################

# # Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).
# # Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
# # Línea 4: se lee el nombre del alumno aquí.
# # Línea 5-6: si el nombre es una cadena vacía (), salimos del bucle.
# # Línea 8: se pide la calificación del estudiante (un valor entero en el rango del 1-10).
# # Línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle.
# # Línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).
# # Línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada.
# # Línea 17: se itera a través de los nombres ordenados de los estudiantes.
# # Línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
# # Línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
# # Línea 23: se calcula e imprime el promedio del alumno junto con su nombre.

# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
    
#     if score not in range(0, 11):
#  	    break
    
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

######################
# Sección 4.6.1.10
######################

## También se puede crear una tupla utilizando la función 
## integrada de Python tuple(). 
## Esto es particularmente útil cuando se desea convertir un iterable 
## (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:

# my_tuple = tuple((1, 2, "cadena"))
# print(my_tuple)

# my_list = [2, 4, 6]
# print(my_list)          # salida: [2, 4, 6]
# print(type(my_list))    # salida: <class 'list'>

# tup = tuple(my_list)

# print(tup)              # salida: (2, 4, 6)
# print(type(tup))        # salida: <class 'tuple'>

## De la misma manera, cuando se desea convertir un iterable en una lista, 
## se puede emplear la función integrada de Python denominada list():

# tup = 1, 2, 3, 

# my_list = list(tup)

# print(type(my_list))    # salida: <class 'list'>

######################
# Sección 4.6.1.12
######################

## Ejercicio 1
## ¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

# my_tup = (1, 2, 3)
# print(my_tup[2])

## Ejercicio 2
## ¿Cuál es la salida del siguiente fragmento de código?

# tup = 1, 2, 3
# a, b, c = tup

# print(a * b * c)

## Ejercicio 3
## Completa el código para emplear correctamente el método count() 
## para encontrar la cantidad de números 2 duplicados en la tupla siguiente.

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # salida: 4

## Ejercicio 4
## Escribe un programa que "una" los dos diccionarios (d1 y d2) 
## para crear uno nuevo (d3).

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)
# print(d3)

# #  update() para añadir una tupla al diccionario
# tupla = ("César","Martín")
# d3.update({tupla})
# print(d3)


## Ejercicio 5
## Escribe un programa que convierta la lista my_list en una tupla.

# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)

# print(t)

## Ejercicio 6
## Escribe un programa que convierta la tupla colors en un diccionario.

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)

# print(colors_dictionary)

## Ejercicio 7
## ¿Que ocurrirá cuando se ejecute el siguiente código?

# my_dictionary = {"A": 1, "B": 2}
# copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()

# print(copy_my_dictionary)


## Ejercicio 8
## ¿Cuál es la salida del siguiente programa?

# colors = {
#     "blanco": (255, 255, 255),
#     "gris": (128, 128, 128),
#     "rojo": (255, 0, 0),
#     "verde": (0, 128, 0)
#     }

# for col, rgb in colors.items():
#     print(col, ":", rgb)
#     # print(col, ":", rgb[0],rgb[1],rgb[2])

######################
# Sección 4.7.1.2
######################

# value = int(input('Ingresa un número natural: '))
# print('El recíproco de', value, 'es', 1/value)

# if type(value) is int:
#     print("El valor introducido es un entero")
# else:
#     print("El valor introducido NO es un entero")

######################
# Sección 4.7.1.3
######################

#  Estructura try/except

# try:
# 	# Es un lugar donde
# 	# tu puedes hacer algo 
#   # sin pedir permiso.
# except:
# 	# Es un espacio dedicado 
#   # exclusivamente para pedir perdón.

######################
# Sección 4.7.1.4
######################

# try:
#     value = input('Ingresa un número natural: ')
#     print('El recíproco de', value, 'es', 1/int(value))        
# except:
#     print('No se qué hacer con', value)

# Ejemplo 2

# while True:
#     try:
#         value = input('Ingresa un número natural: ')
#         print('El recíproco de', value, 'es', 1/int(value)) 
#         break
#     except:
#         print('\tNo se qué hacer con', value, ".Vuelve a probar...")

######################
# Sección 4.7.1.5
######################

# try:
#     value = input('Ingresa un número natural: ')
#     print('El recíproco de', value, 'es', 1/int(value))        
# except ValueError:
#     print('No se qué hacer con', value)    
# except ZeroDivisionError:
#     print('La división entre cero no está permitida en nuestro Universo.')  

######################
# Sección 4.7.1.6
######################

# try:
#     value = input('Ingresa un número natural: ')
#     print('El recíproco de', value, 'es', 1/int(value))        
# except ValueError:
#     print('No se que hacer con', value)    
# except ZeroDivisionError:
#     print('La división entre cero no está permitida en nuestro Universo.')    
# except:
#     print('Ha sucedido algo extraño, ¡lo siento!')

######################
# Sección 4.7.1.8
######################

# temperature = float(input('Ingresa la temperatura actual:'))

# if temperature > 0:
#     print("Por encima de cero")
# elif temperature < 0:
#     print("Por debajo de cero")
# else:
#     print("Cero")

######################
# Sección 4.7.1.9
######################

# temperature = float(input('Ingresa la temperatura actual:'))

# if temperature > 0:
#     print("Por encima de cero")
# elif temperature < 0:
#     prin("Por debajo de cero")
# else:
#     print("Cero")

######################
# Sección 4.7.1.13
######################

# ¿Cuál es la salida del siguiente programa si el usuario ingresa un 0?

# try:
#     value = int(input("Ingresa un número entero: "))
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except:
#     print("¡Buuuu!")

###################################################
########### Excepciones personalizadas ############
###################################################

# class CustomError(Exception):
#     pass

# ###

# try:
#     if input("Introduce una X para comprobar la excepción personalizada: ") == "X":
#         raise CustomError
# except CustomError:
#     print("Excepción personalizada!")

# try:
#     n = input("introduce un numero: ")
#     5 / n
# except Exception as e:
#     print(e)
#     print(type(e).__name__)





# class ValorInvalido(Exception):
#     pass
# ###
# def readint(prompt, min, max):
#     ok = False
#     while not ok:
#         try:
#             valor = int(input(prompt + str(min) + " y " + str(max) + ": "))
#             if not (valor >= min and valor <= max):

#                 raise ValorInvalido
            
#             print("Valor correcto")
#             ok = True
#         except ValueError:
#             print("Error: entrada incorrecta")
#         except ValorInvalido:
#             print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    
#     return valor
    
# v = readint("Ingresa un número entre: ", -10, 10)

# print("El numero es:", v)
#####################################
# Sección 4.7.2.1 - Laboratorio
#####################################

# from random import randrange

# def dibujar_tablero(tablero):
#   print("+-------" * 3,"+", sep="")
#   for fila in range(3):
#       print("|       " * 3,"|", sep="")
#       for columna in range(3):
#           print("|   " + str(tablero[fila][columna]) + "   ", end="")
#       print("|")
#       print("|       " * 3,"|",sep="")
#       print("+-------" * 3,"+",sep="")


# def introducir_movimiento(tablero):
#   ok = False	                                            # suposición falsa - la necesitamos para entrar en el bucle
#   while not ok:
#       movimiento = input("Ingresa tu movimiento: ") 
#       ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9' # ¿es válido lo que ingresó el usuario?
#       if not ok:
#           print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
#           continue
#       movimiento = int(movimiento) - 1  	                # numero de la celda, del 0 al 8
#       fila = movimiento // 3 	                            # fila de la celda
#       columna = movimiento % 3		                        # columna de la celda
#       posicion = tablero[fila][columna]	                    # marca el cuadro elegido
#       ok = posicion not in ['O','X'] 
#       if not ok:	                                        # está ocupado, ingresa una posición nuevamente
#           print("¡Cuadro ocupado, ingresa nuevamente!")
#           continue
#   tablero[fila][columna] = 'O' 	                            # colocar '0' al cuadro seleccionado


# def crear_lista_de_posiciones_libres(tablero):
#   libre = []	                                                # la lista esta vacía inicialmente
#   for fila in range(3):                                     # itera a través de las filas
#       for columna in range(3):                              # itera a través de las columnas
#           if tablero[fila][columna] not in ['O','X']:       # ¿Está la celda libre?
#               libre.append((fila,columna))                  # si, agrega una nueva tupla a la lista
#   return libre


# def victoria_para(tablero,señal):
#   if señal == "X":	                                        # ¿Estamos buscando X?
#       quien = 'yo'	                                        # Si, es la máquina
#   elif señal == "O":                                        # ... ¿o estamos buscando O?
#       quien = 'tú'	                                        # Si, es el usuario
#   else:
#       quien = None	                                        # ¡No debemos de caer aquí!
#   diagonal1 = diagonal2 = True                              # para las diagonales
#   for rc in range(3):
#       if tablero[rc][0] == señal and tablero[rc][1] == señal and tablero[rc][2] == señal:	# verificar fila rc
#           return quien
#       if tablero[0][rc] == señal and tablero[1][rc] == señal and tablero[2][rc] == señal:   # verificar columna rc
#           return quien
#       if tablero[rc][rc] != señal:                          # revisar la primera diagonal
#           diagonal1 = False
#       if tablero[2 - rc][2 - rc] != señal:                  # revisar la segunda diagonal
#           diagonal2 = False
#   if diagonal1 or diagonal2:
#       return quien
#   return None


# def dibujar_movimiento(tablero):
#     libre = crear_lista_de_posiciones_libres(tablero)        # crea una lista de los cuadros vacios o libres
#     contador = len(libre)
#     if contador > 0:	                                         # si la lista no esta vacía, elegir un lugar para 'X' y colocarla
#       this = randrange(contador)
#       fila, columna = libre[this]
#       tablero[fila][columna] = 'X'

# #####################################33


# tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
# tablero[1][1] = 'X'                                               # colocar la primera 'X' en el centro
# libre = crear_lista_de_posiciones_libres(tablero)
# turno_humano  = True                                              # ¿De quien es el turno ahora?
# while len(libre):
#     dibujar_tablero(tablero)
#     if turno_humano:
#         introducir_movimiento(tablero)
#         victoria = victoria_para(tablero,'O')
#     else:	
#         dibujar_movimiento(tablero)
#         victoria = victoria_para(tablero,'X')
        
#     if victoria != None:
#         break
#     turno_humano  = not turno_humano 		
#     libre = crear_lista_de_posiciones_libres(tablero)


# dibujar_tablero(tablero)

# if victoria == 'tú':
#  	print("¡Has ganado!")
# elif victoria == 'yo':
#  	print("Gana la máquina!")
# else:
#  	print("¡Empate!")

#################################

# ## Minimax

# from random import randrange

# def dibujar_tablero(tablero):
#   print("+-------" * 3,"+", sep="")
#   for fila in range(3):
#       print("|       " * 3,"|", sep="")
#       for columna in range(3):
#           print("|   " + str(tablero[fila][columna]) + "   ", end="")
#       print("|")
#       print("|       " * 3,"|",sep="")
#       print("+-------" * 3,"+",sep="")

# def introducir_movimiento(tablero):
#   ok = False	                                            # suposición falsa - la necesitamos para entrar en el bucle
#   while not ok:
#       movimiento = input("Ingresa tu movimiento: ") 
#       ok = len(movimiento) == 1 and \
#       movimiento >= '1' and movimiento <= '9'               # ¿es válido lo que ingresó el usuario?
#       if not ok:
#           print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
#           continue
#       movimiento = int(movimiento) - 1  	                # numero de la celda, del 0 al 8
#       fila = movimiento // 3 	                            # fila de la celda
#       columna = movimiento % 3		                        # columna de la celda
#       posicion = tablero[fila][columna]	                    # marca el cuadro elegido
#       ok = posicion not in ['O','X'] 
#       if not ok:	                                        # está ocupado, ingresa una posición nuevamente
#           print("¡Cuadro ocupado, ingresa nuevamente!")
#           continue
#   tablero[fila][columna] = 'O' 	                            # colocar '0' al cuadro seleccionado


# def crear_lista_de_posiciones_libres(tablero):
#   libre = []	                                            # la lista esta vacía inicialmente
#   for fila in range(3):                                     # itera a través de las filas
#       for columna in range(3):                              # itera a través de las columnas
#           if tablero[fila][columna] not in ['O','X']:       # ¿Está la celda libre?
#               libre.append((fila,columna))                  # si, agrega una nueva tupla a la lista
#   return libre


# def victoria_para(tablero,señal):
#   if señal == "X":	                                        # ¿Estamos buscando X?
#       quien = 'yo'	                                        # Si, es la máquina
#   elif señal == "O":                                        # ... ¿o estamos buscando O?
#       quien = 'tú'	                                        # Si, es el usuario
#   else:
#       quien = None	                                        # ¡No debemos de caer aquí!
#   diagonal1 = diagonal2 = True                              # para las diagonales
#   for rc in range(3):
#       if tablero[rc][0] == señal and tablero[rc][1] == señal and tablero[rc][2] == señal:	# verificar fila rc
#           return quien
#       if tablero[0][rc] == señal and tablero[1][rc] == señal and tablero[2][rc] == señal:   # verificar columna rc
#           return quien
#       if tablero[rc][rc] != señal:                          # revisar la primera diagonal
#           diagonal1 = False
#       if tablero[2 - rc][2 - rc] != señal:                  # revisar la segunda diagonal
#           diagonal2 = False
#   if diagonal1 or diagonal2:
#       return quien
#   return None


# def minimax(tablero, depth, is_maximizing):
#     # Base case: check for terminal states (win, lose, draw)
#     result = victoria_para(tablero, 'X' if is_maximizing else 'O')
#     if result is not None:
#         if result == 'yo':
#             return -1
#         elif result == 'tú':
#             return 1
#         else:
#             return 0

#     if is_maximizing:
#         best_score = float('-inf')
#         for fila in range(3):
#             for columna in range(3):
#                 if tablero[fila][columna] not in ['O', 'X']:
#                     tablero[fila][columna] = 'X'
#                     score = minimax(tablero, depth + 1, False)
#                     tablero[fila][columna] = ' '  # Undo the move
#                     best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float('inf')
#         for fila in range(3):
#             for columna in range(3):
#                 if tablero[fila][columna] not in ['O', 'X']:
#                     tablero[fila][columna] = 'O'
#                     score = minimax(tablero, depth + 1, True)
#                     tablero[fila][columna] = ' '  # Undo the move
#                     best_score = min(score, best_score)
#         return best_score


# def dibujar_movimiento_minimax(tablero):
#     libre = crear_lista_de_posiciones_libres(tablero)
#     best_score = float('-inf')
#     best_move = None
#     for fila in range(3):
#         for columna in range(3):
#             if tablero[fila][columna] not in ['O', 'X']:
#                 tablero[fila][columna] = 'X'
#                 score = minimax(tablero, 0, False)
#                 tablero[fila][columna] = ' '  # Undo the move
#                 if score > best_score:
#                     best_score = score
#                     best_move = (fila, columna)

#     if best_move is not None:
#         fila, columna = best_move
#         tablero[fila][columna] = 'X'


# 


# tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # create an empty board
# tablero[1][1] = 'X'  # place the first 'X' in the center
# libre = crear_lista_de_posiciones_libres(tablero)
# turno_humano = True
# while len(libre):
#     dibujar_tablero(tablero)
#     if turno_humano:
#         introducir_movimiento(tablero)
#         victoria = victoria_para(tablero, 'O')
#     else:
#         dibujar_movimiento_minimax(tablero)  # Use minimax for AI moves
#         victoria = victoria_para(tablero, 'X')

#     if victoria is not None:
#         break
#     turno_humano = not turno_humano
#     libre = crear_lista_de_posiciones_libres(tablero)

# dibujar_tablero(tablero)

# if victoria == 'tú':
#     print("¡Has ganado!")
# elif victoria == 'yo':
#     print("Gana la máquina!")
# else:
#     print("¡Empate!")