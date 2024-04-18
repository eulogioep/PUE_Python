# print("Fundamentos","Programación","en", sep="***", end="...")
# print("Python")


# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# #Con menos invocaciones de print())

# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  ***** ")

# #Más alto

# print("        *")
# print("       * *")
# print("      *   *")
# print("     *     *")
# print("    *       *")
# print("   *         *")
# print("  *           *")
# print(" *             *")
# print("******     ******")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *******")

# #Doble

# print("        *        "*2)
# print("       * *       "*2)
# print("      *   *      "*2)
# print("     *     *     "*2)
# print("    *       *    "*2)
# print("   *         *   "*2)
# print("  *           *  "*2)
# print(" *             * "*2)
# print("******     ******"*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *******     "*2)


# print("    *     "*2 , 
#       "   * *    "*2 , 
#       "  *   *   "*2 , 
#       " *     *  "*2 , 
#       "***   *** "*2 , 
#       "  *   *   "*2 , 
#       "  *   *   "*2 , 
#       "  *****   "*2 , sep="\n")

# asterisco = "*"
# espacio = " "

# print(8*espacio + asterisco, 
#       7 * espacio + asterisco + espacio + asterisco, 
#       6 * espacio + asterisco + 3 * espacio + asterisco, 
#       5 * espacio + asterisco + 5 * espacio + asterisco, 
#       4 * espacio + asterisco + 7 * espacio + asterisco, 
#       3 * espacio + asterisco + 9 * espacio + asterisco, 
#       2 * espacio + asterisco + 11 * espacio + asterisco,
#       espacio+asterisco + 13 * espacio + asterisco, 
#       sep="\n" )
# print("******     ******")
# print("     *     *")
# print("     *     *")
# print("     *******")

# # minimizar el número de invocaciones de la función print

# # solucion 1

# # print("\
# #       *\n\
# #      * *\n\
# #     *   *\n\
# #    *     *\n\
# #   ***   ***\n\
# #     *   *\n\
# #     *   *\n\
# #     *****")

# # solución 2

# print("     *     ",      
#       "    * *    ",     
#       "   *   *   ",    
#       "  *     *  ",   
#       " ***   *** ",  
#       "   *   *   ",    
#       "   *   *   ",    
#       "   *****   ",    
#       sep="\n")

# # solución 3

# print("    *",      
#       "   * *",     
#       "  *   *",    
#       " *     *",   
#       "***   ***",  
#       "  *   *",    
#       "  *   *",    
#       "  *****",    
#       sep="\n")



# # hacer la flecha dos veces más grande pero mantener las proporciones

# # print(
# #     "        *         " ,
# #     "       * *        " ,
# #     "      *   *       " ,
# #     "     *     *      " ,
# #     "    *       *     " ,
# #     "   *         *    " ,
# #     "  *           *   " ,
# #     " *             *  " ,
# #     "******     ****** " ,
# #     "     *     *      " ,
# #     "     *     *      " ,
# #     "     *     *      " ,
# #     "     *     *      " ,
# #     "     *******      " ,
# #     sep="\n")

# print("""
#             *         
#            * *        
#           *   *       
#          *     *      
#         *       *     
#        *         *    
#       *           *   
#      *             *  
#     ******     ****** 
#          *     *      
#          *     *      
#          *     *      
#          *     *      
#          *******      """)

# # Duplicar la flecha, colocando ambas flechas lado a lado

# print("    *     " * 2 ,
#       "   * *    " * 2 ,
#       "  *   *   " * 2 ,
#       " *     *  " * 2 ,
#       "***   *** " * 2 ,
#       "  *   *   " * 2 ,
#       "  *   *   " * 2 ,
#       "  *****   " * 2 ,
#       sep="\n")

# # Duplicar la flecha, colocando ambas flechas lado a lado

# print("    *     " * 2 ,
#       "   * *    " * 2 ,
#       "  *   *   " * 2 ,
#       " *     *  " * 2 ,
#       "***   *** " * 2 ,
#       "  *   *   " * 2 ,
#       "  *   *   " * 2 ,
#       "  *****   " * 2 ,
#       sep="\n")
# # Modificar las siguientes líneas para conseguir éste resultado: 
    
# # Fundamentos***Programación***en...Python

# # print("Fundamentos","Programación","en")
# # print("Python")

# # solución

# # print("Fundamentos","Programación","en", sep="***", end="...")
# # print("Python")

# # Tipado dinámico, tipado fuerte
# print("2" + str(2))
# print(int("2") + 2)

# print(type('hola'))

# print(type(4))

# print(type(4.0))

# def x(*args):
#     print(type(args))


# x(1,2,3,4,5,6,7,8,9)

# # print(type('hola'))

# # print(type(4))

# # print(type(4.0))

# print('Me gusta \"el tbo\"')

# print('Me gusta "Monty Python"')
# print("Me gusta \"Monty Python\"")

# # ¿cómo imprimir este valor? --> I'm "Monty Python"
# print('I\'m "Monty Python"')
# print('''I'm "Monty Python"''')

# cadena = "hola"
# print(id(cadena))

# cadena = cadena + "pepe"
# print(id(cadena))

# # # nueva_cadena = cadena
# # # print(id(nueva_cadena))juan = 3
# # juan = 3
# # maria = 5
# # adan = 6

# # total_manzanas = juan + maria + adan
# # #total_manzanas = juan - maria - adan
# # #total_manzanas = juan * maria * adan
# # #total_manzanas = juan // maria // adan

# # print(juan, maria, adan)
# # print("El total de manzanas es:", total_manzanas)

# # # Definimos la cantidad de manzanas que tienen cada persona
# # juan = 3
# # maria = 5 
# # adan = 6

# # # Calculamos el total de manzanas
# # total_manzanas = juan + maria + adan

# # # Mostramos la cantidad de manzanas que tiene cada persona y el total
# # print("Juan tiene:", juan, "manzanas.")
# # print("María tiene:", maria, "manzanas.")
# # print("Adán tiene:", adan, "manzanas.")
# # print("Número total de manzanas:", total_manzanas)

# # # Otros ejemplos
# # # Podemos agregar más personas y sus respectivas cantidades de manzanas
# # pedro = 4
# # ana = 7

# # # Calculamos el nuevo total de manzanas
# # total_manzanas_nuevo = total_manzanas + pedro + ana

# # # Mostramos la cantidad de manzanas que tienen las nuevas personas y el total actualizado
# # print("\nPedro tiene:", pedro, "manzanas.")
# # print("Ana tiene:", ana, "manzanas.")
# # print("Número total de manzanas ahora es:", total_manzanas_nuevo)

# # Conversor de Kilometros <-> Millas
# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = (miles * 1.61)
# kilometers_to_miles = (kilometers / 1.61)

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# x =  0
# x = float(x)
# y = (3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1
# print("y =", y)

# x =  1
# x = float(x)
# y = (3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1
# print("y =", y)

# x =  -1
# x = float(x)
# y = (3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1
# print("y =", y)

# ## convertidor de dolar-euro

# cotizacion_actual_dolar = 0.93

# euros = 1
# dolares = 1

# dolar_a_euro = (dolares * cotizacion_actual_dolar)
# euro_a_dolar = (euros / cotizacion_actual_dolar)

# print (euros , "euros son", round(euro_a_dolar, 3), "dólares")
# print (dolares, "dólares son", round(dolar_a_euro, 3), "euros")

# def my_Calc(x):
#      return (3 * x ** 3) - (2 * x ** 2) + (3 * x - 1)
    
    
# x = 0 # codifica aquí tus datos de prueba
# x = float(x)
# # escribe tu código aquí
# #y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", my_Calc(x))
# x = 1
# #y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", my_Calc(x))
# x = -1
# #y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", my_Calc(x))


# este programa calcula los segundos en cierto número de horas determinadas 
# Fecha de creación: día 3 de Abril de 2024
# autor: cesar.martin@numaconsulting.com

# numero_horas = 2                # número de horas
# segundos = 3600                 # número de segundos en una hora

# print("Horas: ", numero_horas)  # imprime el numero de horas

# # se imprime el numero de segundos en determinado numero de horas
# print("Segundos en Horas: ", numero_horas * segundos) 

# print("Adiós")

# print("+" + (10 * "-") + "+")
# print(("|" + (" " * 10) + "|\n") * 5, end="")
# print("+" + (10 * "-") + "+")
# print("+" + (10 * "-") + "+")
# print(("|" + (" " * 10) + "|\n") * 5, end="")
# print("+" + (10 * "-") + "+")

# # Solicitar el ancho y el alto del rectángulo
# ancho = int(input("Introduce el ancho del rectángulo: "))
# alto = int(input("Introduce el alto del rectángulo: "))

# # Imprimir la parte superior del rectángulo
# print("+" + "-" * ancho + "+")

# # Imprimir el cuerpo del rectángulo
# print(("|" + " " * ancho + "|\n") * alto, end="")

# # Imprimir la parte inferior del rectángulo
# print("+" + "-" * ancho + "+")

# ancho=int(input("Dime el ancho del cuadrado:",))
# largo=int(input("Dime el largo del cuadrado:",))
# print("+" + (ancho * "-") + "+")
# print(("|" + (" " * largo) + "|\n") * largo, end="")
# print("+" + (ancho * "-") + "+")


# print("+" + (10 * "-") + "+")
# print(("|" + (" " * 10) + "|\n") * 5, end="")
# print("+" + (10 * "-") + "+")

# wide = int(input("Introduce el ancho del rectángulo: "))
# high = int(input("Introduce el alto del rectángulo: "))
# def print_rectangle(wide, high):
#     print("+" + (wide * "-") + "+")
#     print(("|" + (" " * wide) + "|\n") * high, end="")
#     print("+" + (wide * "-") + "+")
    
# print_rectangle(12,7)

# a = float(input("Ingresa el primer valor: "))
# b = float(input("Ingresa el segundo valor: "))

# print("Suma:", a + b)
# print("Resta:", a - b)
# print("Multiplicación:", a * b)
# print("División:", a / b)

# print("\n¡Eso es todo, amigos!")

# print('    1     ',
#       '----------',
#       '     1    ',
#       'x + ------',
#       '      1   ',
#       ' x + -----',
#       '       1  ',
#       '  x + ----',
#       '        x ',
#       sep='\n'
#       )

# x = float(input("Ingresa un valor para x: "))

# y = 1./(x + 1./(x + 1./(x + 1./x)))

# print("y =", y)

# #####################################

# x = float(input("Ingrese el valor para x: "))

# Necesitamos comenzar desde la fracción más interna y avanzar hacia afuera.
# La expresion es: 1 / (x + 1 / (x + 1 / (x + 1 / x)))
# 1/x es la más interna, luego tenemos x + ese resultado, y así sucesivamente.
# Usamos paréntesis para mantener el orden correcto de las operaciones.

# mas_interna = 1 / x
# segunda = x + mas_interna
# tercera = 1 / segunda
# cuarta = x + tercera
# y = 1 / cuarta

# print("y =", y)

#####################################


# hour = int(input("Hora de inicio (horas): "))
# mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos): "))
# mins = mins + dura # encuentra el número total de minutos
# hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
# mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
# hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
# print(hour, ":", mins, sep='')

# hora_inicial = int(input("Hora de inicio (horas): "))
# minutos_iniciales = int(input("Minuto de inicio (minutos): "))
# duracion = int(input("Duración del evento (minutos): "))

# print("Hora inicial: " + str(hora_inicial) + ":" + str(minutos_iniciales))

# total_minutos = minutos_iniciales + duracion 

# print("Total minutos:", total_minutos)

# minutos_finales = total_minutos % 60 # resto de la división

# print("Minutos finales: " + str(minutos_finales))

# horas_adicionales = total_minutos // 60 # división entera

# print("Horas adicionales:",horas_adicionales )

# hora_final = hora_inicial + horas_adicionales

# hora_final_de_0_a_24 = hora_final % 24 # por si nos pasamos de las 24 horas!!

# print(str(hora_final_de_0_a_24) + ":" + str(minutos_finales))

# # solución con menos variables

# horas_iniciales = int(input("Hora de inicio (horas): "))
# minutos_iniciales = int(input("Minuto de inicio (minutos): "))
# duracion = int(input("Duración del evento (minutos): "))

# print((horas_iniciales + ((duracion + minutos_iniciales) // 60)) % 24,':',
#       (duracion + minutos_iniciales) % 60,sep='')

# print('El evento terminará a las ',
#       str((horas_iniciales + ((duracion + minutos_iniciales) // 60)) % 24).zfill(2),
#       ':',
#       str((duracion + minutos_iniciales) % 60).zfill(2),
#       ' horas',
#       sep='')

# ##########################

# mensaje = 11

# print(str(mensaje).zfill(10)) #Pone 0 a la izquierda

# #########################

# x = input("Ingresa un número: ") # El usuario ingresa un 2 
# print(type(x).__name__)

# Precedencia de operadores actualizada

# Prioridad	
# 1	+, -                       operadores unarios
# 2	**	
# 3	*, /, //, %
# 4	+, -                       operadores binarios
# 5 +=, -=, *=, /=, //=, %=    operadores abreviados
# 6	<, <=, >, >=	               
# 7	==, !=


# hat_list = [1, 2, 3, 4, 5]

# # Paso 1
# hat_list[2] = int(input("Ingresa un número entero: "))

# # Paso 2
# del hat_list[-1]

# # Paso 3
# print(len(hat_list))

############################

# recuento = 0
# suma = 0

# while True:
    
#     numero_actual = int(input('Introduce un número superior a 0 (0 o inferior para terminar): '))
    
#     # Salir del bucle si se introduce un valor menor o igual a cero
#     if numero_actual <= 0:
#         break

#     recuento += 1
#     suma += numero_actual

# # Imprimir resultados
# print('\nHas introducido', recuento, 'números')
# print('La suma de los números introducidos es', suma)
# print()

######################################


# ## Con listas

# lista_numeros = []
# recuento = 0
# suma = 0

# while True:

#     numero_actual = int(input('Introduce un número superior a 0 (0 o inferior para terminar): '))
    
#     # Salir del bucle si se introduce un valor menor o igual a cero
#     if numero_actual <= 0:
#         break

#     # Añadiendo los elementos a la lista
#     lista_numeros.append(numero_actual)

# # Imprimir elementos en la lista
# print('\nElementos de la lista:', lista_numeros)

# # Recorrer la lista para contar y sumar
# for elemento in lista_numeros:

#     recuento += 1
#     suma += elemento

# # Imprimir resultados
# print('\nHas introducido', recuento, 'números')
# print('La suma de los números introducidos es', suma)
# print()

# ###########
# # Se podría haber calculado suma y recuento directamente:

# print('\nHas introducido', len(lista_numeros), 'números')
# print('La suma de los números introducidos es', sum(lista_numeros))


# # ###################################


# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# #
# ###############################



# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)


# ###############################

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)

# ###############################

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for indice in range(len(my_list)):
#     total += my_list[indice]

# print(total)

# total = 0

# for elemento in my_list:
#     total += elemento

# print(total)

########################

# my_list = [10, 1, 8, 3, 5,3,4,5,6,7,8,9]
# length = len(my_list)

# for i in range(length // 2):
#     print('reemplazando', i, 'por', length - i - 1)
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)
# my_list = [10, 1, 8, 3, 5,3,4,5,6,7,8,9]
# length = len(my_list)

# for i in range(length // 2):
#     print('reemplazando elemento en posición', i, 'por elemento en posición', length - i - 1)
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)


#############################

# # paso 1:
# Beatles = []
# print("Paso 1:", Beatles)

# # paso 2:

# Beatles.append("John Lennon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")
# print("Paso 2:", Beatles)

# # paso 3:
# for members in range(2):
#     Beatles.append(input("Nuevo miembro de la banda: "))
# print("Paso 3:", Beatles)

# # paso 4:
# del Beatles[-1]
# del Beatles[-1]
# print("Paso 4:", Beatles)

# # paso 5:
# Beatles.insert(0, "RingoStarr")
# print("Paso 5:", Beatles)
# print("Los Fav:",len(Beatles))

##############################


# # Paso 1: Crea una lista vacía llamada beatles.

# Beatles = []
# print("Paso 1:", Beatles)

# # Paso 2: Emplea el método append() para agregar los siguientes miembros 
# # de la banda a la lista: John Lennon, Paul McCartney y George Harrison.

# Beatles.append("John Lennon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")
# print("Paso 2:", Beatles)

# # Paso 3: Emplea el bucle for y el append() para pedirle al usuario 
# # que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.

# for _ in range(2):
#     Beatles.append(input("Nuevo miembro de la banda: "))
# print("Paso 3:", Beatles)

# #  Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.

# del Beatles[-1]
# del Beatles[-1]

# # Alternativa a eliminar por posición
# # Beatles.remove("Stu Sutcliffe")
# # Beatles.remove("Pete Best")

# print("Paso 4:", Beatles)

# # Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.

# Beatles.insert(0, "Ringo Starr")
# print("Paso 5:", Beatles)
# print("Los Fav:",len(Beatles))


##########################


# # Ordenacion de la Burbuja
# my_list = [8, 10,200, 6, 2, 4, 22]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)

#############################

# lista = [8, 10, 6, 2, 4]  # lista a ordenar
# intercambio = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# longitud = len(lista)

# while intercambio:
    
#     intercambio = False  # no hay intercambios hasta ahora

#     for indice in range(longitud - 1):
#         if lista[indice] > lista[indice + 1]:

#             intercambio = True  # ¡ocurrió el intercambio!
            
#             lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
    
#     longitud -= 1 # reduce el número de comparaciones en la siguiente ejecucion del bucle for
    
# print(lista)

##################################

# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)


#########################################

# lst = [5, 3, 1, 2, 4]
# print(lst)

# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]

# #################################

# lst = [5, 3, 1, 2, 4]
# print(lst)

# lst.reverse()
# print(lst)  # salida: [4, 2, 1, 3, 5]

#################################

# a = "A"
# b = "B"
# c = "C"
# d = " "

# lst = [ord(a), ord(b), ord(c), ord(d)]

# print(lst)

##################################

# Cuando se tratan de objetos, al asignar una variable otra variable, dicha variable hace referencia
# al objeto en memoria. Es como tener 2 mandos a distancia que apuntan en memoria a un mismo objeto.
# Esto sucede con objetos e Strings.

# Esto es diferente si se usan datos escalares (enteros, booleanos, flotantes, etc)

# list_1 = [1]

# list_2 = list_1

# list_1[0] = 2

# print(id(list_1))
# print(id(list_2))

# list_2.append('otro valor')

# print(list_1)
# print(list_2)

# ##############################

# list_1 = [1]

# list_2 = list_1[:] # Si se usan los ":" hace una copia de la lista, por tanto, ya tienen un id diferente.

# list_1[0] = 2 # Modifica el elemento en posición 0 de la lista 1

# print(id(list_1))
# print(id(list_2))

# list_2.append('otro valor')

# print(list_1)
# print(list_2)

########################################

# # Copiando parte de la lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

##########################

# # Copiando parte de la lista.
# my_list = [100, 80.75, 60.66, 22.48, 23.55]

# my_list.sort()      # ordena en sentido ascendente
# my_list.reverse()   # por eso invertimos, lo queremos de mayor a menor

# new_list = my_list[  : 3 ] ## nos quedamos con los tres mayores importes

# print(new_list)

############################

# # Saber el número mayor de una lista

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# maximo = -999999

# for elemento in my_list:
#     if elemento > maximo:
#         maximo = elemento

# print(maximo)

# # Igual que usamos print(max(my_list))
##################################

# # Ahora encontremos la ubicación de un elemento dado dentro de una lista:

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for indice in range(len(my_list)):
    
#     found = (my_list[indice] == to_find)

#     if found:
#         break

# if found:
#     print("Elemento encontrado en el índice", indice)
# else:
#     print("ausente")

######################################

# Acierto de numeros de la loteria

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)

###########################################

# # Elimina los valores repetidos de una lista

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
# for number in my_list:  # Recorre todos los números de la lista original.
# 	if number not in new_list:  # Si el número no aparece dentro de la nueva lista...
# 		new_list.append(number)  # ...agregarlo aquí.
# my_list = new_list[:]  # Crea una copia de new_list.
# print("La lista con elementos únicos:")
# print(my_list)

# #############################################

# ## SIN MANEJO DE EXCEPCIONES

# lista = [1, 2, 33, 4, 5, 6, 7, 8, 33, 9, 33, 10]
# valor_a_buscar = 33

# posicion_actual = 0

# while True:

#     if valor_a_buscar not in lista[ posicion_actual : ]:    # sintáxis de rebanadas
#         break

#     posicion_actual = lista.index(valor_a_buscar, posicion_actual)
#     print('Valor',valor_a_buscar,'encontrado en índice',posicion_actual)

#     posicion_actual += 1    # para comenzar la siguiente búsqueda a partir de la siguiente posición

# print('Ya no hay más coincidencias')


# ###########################################################

# ## CON MANEJO DE EXCEPCIONES

# lista = [1, 2, 33, 4, 5, 6, 7, 8, 33, 9, 33, 10]
# valor_a_buscar = 33

# posicion_actual = 0

# while True:
#     try:

#         posicion_actual = lista.index(valor_a_buscar, posicion_actual)
#         print('Valor',valor_a_buscar,'encontrado en índice',posicion_actual)

#         posicion_actual += 1    # para comenzar la siguiente búsqueda a partir de la siguiente posición

#     except:
#         print('Ya no hay más coincidencias')
#         break


# #################

# mi_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# nueva_lista = []

# for number in mi_lista:                # Recorremos todos los números de la lista original.
#     if number not in nueva_lista:      # Si el número no aparece dentro de la nueva lista ...
#         nueva_lista.append(number)     # ... añadirlo aquí.

# mi_lista = nueva_lista                 # Asignamos la nueva lista a la variable original.
# del nueva_lista                        # y eliminamos la nueva lista

# print("La lista con elementos únicos:")
# print(mi_lista)
# miLista = [1, 22, 4, 44, 22, 1, 44, 2, 6, 2, 9]

# indice = 0
# miLista.sort()

# while indice in range(len(miLista)):
#     if miLista[indice] in miLista[indice:]:
        
#         del miLista[indice]

#     indice += 1
# print(miLista)

# ######################################

# ## Antonio

# lista=[1, 2, 2, 4, 5, 7, 6, 7]
# for numero1 in lista:
#     contador=0
#     for numero2 in lista:
#         if numero1 == numero2:
#             contador+=1
#     if contador >= 2:
#         lista.remove(numero1)
# print(lista)

# #########################

## Juanjo # Más eficiente

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# i = len(my_list) - 1

# while i >= 0:
#     if my_list[i] in my_list[:i]:
#         del my_list[i]
#     i -= 1

# print("The list with unique elements only:")
# print(my_list)

###################################

# def eliminar_duplicados(lista):
#     indice = 0
#     lista.sort()
#     while indice in range(len(lista)):
        
#         if lista[indice] in lista[indice:]:
        
#             del lista[indice]

#         indice += 1

#     print(lista)
#     del lista

# #########################################
# miLista = [1, 22, 4, 44, 22, 1, 44, 2, 6, 2, 9]

# eliminar_duplicados(miLista)

###############################

# row = []

# for i in range(8):
#     row.append("peón blanco")
# print(row)

# row = ["peón blanco" for i in range(8)]
# print(row)

# # Ejemplo #1:

# squares = [numero ** 2 for numero in range(10)]
# print(squares)

# # # Ejemplo #2:

# twos = [2 ** i for i in range(8)]
# print(twos)

# # # Ejemplo #3:

# impares = [elemento for elemento in squares if elemento % 2 != 0 ]

# print(impares)

# # # Ejemplo #4:

# lista_letras = [letra for letra in 'Palabra']

# print(lista_letras)

########################################

# filas = 8
# columnas = 8

# matriz = []
# letras = ['A','B','C','D','E','F','G','H'] 

# for fila in range(filas):
#     matriz.append([])               # crea una lista vacía por cada fila

#     for columna in range(columnas):
#         matriz[fila].append(letras[fila] + "-" + str(columna))

# print(matriz)

# # #  Impresión de la matriz con formato

# for fila in range(len(matriz)):
#     print() 
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end =" ")
# EMPTY = "--------"
# PAWN = "PEON"
# ROOK = "TORRE"
# KNIGHT = "CABALLO"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# board[7][1] = KNIGHT
# board[7][6] = KNIGHT
# board[7][2] = "ALFIL"
# board[7][5] = "ALFIL"
# board[7][3] = "REINA"
# board[7][4] = "REY"

# print(board)

# for row in board:
#     print()
#     for cell in row:
#         print(format(cell.center(8),"8"), end =" ")
        
        
# ###########################

import random

# temps = [[0.0 for h in range(24)] for d in range(31)]

# total = 0.0

# # # Rellenar con valores aleatorios

# for fila in range(len(temps)):
#     for columna in range(len(temps[fila])):
#         temps[fila][columna] = random.choice(range(10, 450))/10

# for day in temps:
#     total += day[11] # Las 12:00 horas

# average = total / 31

# print("Temperatura promedio al mediodía:", round(average,1), "grados centígrados")
# Imprimir lista con formato

# for fila in range(len(temps)):
#     print("\nDía", fila + 1)
#     for columna in range(len(temps[fila])):
#         print(temps[fila][columna], end = "  ")
     

# print()
# highest = -100.0

# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
            
# print("La temperatura más alta fue de", highest, "grados")

# # #  Días con temperatura superior a 20 grados a las 12 del mediodía

# hot_days = 0

# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1

# print(hot_days, "fueron los días calurosos.")

########################################

# EMPTY = "-"
# PAWN = "PEON"
# ROOK = "TORRE"
# KNIGHT = "CABALLO"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# print(board)

#####################################


# [expression for element in list if conditional]

# for element in list:
#     if conditional:
#         expression


# cubed = [num ** 3 for num in range(5)]
# print(cubed)  # outputs: [0, 1, 8, 27, 64]


###########################################

# #  Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]

# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'

# #########################################

# # Cubo - un arreglo tridimensional (3x3x3)

# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],

#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],

#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]

# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'

# #####################################
