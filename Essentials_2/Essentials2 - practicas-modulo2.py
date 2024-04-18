######################
# Sección 2.1.1.1
######################

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

######################
# Sección 2.1.1.3
######################

# # Imprimir los primeros 10000 caracteres unicode

# for i in range(0,10000):
#     print('\\u' + str(i), "- Caracter:", chr(i))

#################
# print(ord('a'))

######################
# Sección 2.1.1.4
######################

# Ejercicio 1

# ¿Qué es BOM?

# BOM (Byte Order Mark), Una Marca de Orden de Bytes 
# es una combinación especial de bits que anuncia la codificación 
# utilizada por el contenido de un archivo (por ejemplo, UCS-4 o UTF-B).


# Ejercicio 2

# ¿Está Python 3 internacionalizado?

# Sí, está completamente internacionalizado: podemos usar caracteres UNICODE dentro de nuestro código, leerlos desde la entrada y enviarlos a la salida.

######################
# Sección 2.2.1.1
######################

# # Ejemplo 1

# word = 'by'
# print(len(word))


# # Ejemplo 2

# empty = ''
# print(len(empty))


# # Ejemplo 3

# i_am = 'I\'m'
# print(len(i_am))


######################
# Sección 2.2.1.2
######################

# multiline = '''Línea #1
# Línea #2'''

# print(len(multiline))

######################
# Sección 2.2.1.3
######################

# str1 = 'a'
# str2 = 'b'

# print("str1 + str2:\t",str1 + str2)
# print("str2 + str1:\t", str2 + str1)

# print("5 * 'a':\t\t", 5 * 'a')
# print("'b' * 4:\t\t",'b' * 4)

# str1 += str2

# str2 *= 10

# print('str1 += str2:\t',str1)
# print('str2 *= 10:  \t', str2)

######################
# Sección 2.2.1.4
######################

# Si deseas saber el valor del punto de código ASCII/UNICODE 
# de un carácter específico, puedes usar la función ord() (proveniente de ordinal).

# # Demostración de la función ord()

# char_1 = 'a'
# char_2 = ' '  # espacio

# print(ord(char_1))

# print(ord(char_2))

######################
# Sección 2.2.1.5
######################

# Si conoces el punto de código (número) y deseas obtener el 
# carácter correspondiente, puedes usar la función llamada chr().


# Demostración de la función chr()

# print(chr(97))
# print(chr(945))


# x = 'a'

# print(chr(ord(x)) == x)

# x = 90

# print(ord(chr(x)) == x)

######################
# Sección 2.2.1.6
######################

# # Indexando cadenas.

# the_string = 'silly walks'

# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ')

# print()

# # Iterando a través de una cadena.

# the_string = 'silly walks'

# for character in the_string:
#     print(character, end=' ')

# print()

######################

# multiline = '''Línea #1
# Línea #2'''


# for caracter in multiline:
#     print('Ordinal:', ord(caracter), "-\tCaracter:", caracter)


######################

# multiline = '''Linea 1
# Linea 2
# '''

# print(len(multiline))

# for i in range(0,len(multiline)):
#     print (chr(ord(multiline[i])), end = " - ")
#     print(i)
    
######################
# Sección 2.2.1.7
######################

# # Rebanadas

# alpha = "abdefg"

# print("alpha[1:3]: ", alpha[1:3])
# print("alpha[3:]:  ", alpha[3:])
# print("alpha[:3]:  ", alpha[:3])
# print("alpha[3:-2]:", alpha[3:-2])
# print("alpha[-3:4]:", alpha[-3:4])
# print("alpha[::2]: ", alpha[::2])  # incremento!!!
# print("alpha[1::2]:", alpha[1::2]) # incremento!!!

######################
# Sección 2.2.1.8
######################

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

######################
# Sección 2.2.1.9
######################

# # No se permite usar la instrucción del para eliminar cualquier cosa de una cadena.

# # El ejemplo siguiente no funcionará:

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# del alphabet[0]

# # Lo único que puedes hacer con del y una cadena es eliminar la cadena como un todo. 
# # Intenta hacerlo.

# del alphabet

# # Las cadenas de Python no tienen el método append()
# # no se pueden expander de ninguna manera.

# # El siguiente ejemplo es erróneo:

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet.append("A")

# # Con la ausencia del método append(), el método insert() también es ilegal:

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet.insert(0, "A")

######################
# Sección 2.2.1.10
######################

# alphabet = "bcdefghijklmnopqrstuvwxy"

# alphabet = "a" + alphabet
# alphabet = alphabet + "z"

# print(alphabet)

######################
# Sección 2.2.1.11
######################

# # Comenzaremos con la función min().

# # Esta función encuentra el elemento mínimo de la secuencia pasada como argumento. 
# # Existe una condición - la secuencia (cadena o lista) no puede estar vacía, 
# # de lo contrario obtendrás una excepción ValueError.

# # Demostrando min() - Ejemplo 1:
# print(min("aAbByYzZ"))

# # Demostrando min() - Ejemplo 2:
# texto = 'Los Caballeros Que Dicen "¡Ni!"'
# print('[' + min(texto) + ']')

# # Demostrando min() - Ejemplo 3:
# lista = [0, 1, 2]
# print(min(lista))

######################
# Sección 2.2.1.12
######################

# # Del mismo modo, una función llamada max() encuentra el elemento máximo de la secuencia.

# # Demostración de max() - Ejemplo 1:
# print(max("aAbByYzZ"))

# # Demostración de max() - Ejemplo 2 & 3:
# texto = 'Los Caballeros Que Dicen "¡Ni!"'
# print('[' + max(texto) + ']')

# lista = [0, 1, 2]
# print(max(lista))

######################
# Sección 2.2.1.13
######################

# El método index() (es un método, no una función) busca la secuencia desde el principio, 
# para encontrar el primer elemento del valor especificado en su argumento.

# Demostrando el método index():

# print("aAbByYzZaA".index("b"))
# print("aAbByYzZaA".index("Z"))
# print("aAbByYzZaA".index("A"))

# print("aAbByYzZaA".index("AbB"))

# print("aAbByYzZaA".index("R")) # ValueError

# El método devuelve el índice de la primera aparición del argumento 
# (lo que significa que el resultado más bajo posible es 0, 
# mientras que el más alto es la longitud del argumento menos 1).


# Encontrar todas las ocurrencias de un caracter en una cadena

# palabra = "abcABCabcABCabc"
  
# for itr in range(len(palabra)):
 
#     if(palabra[itr] == 'a'): 
#         print(itr, end=' ')

######################
# Sección 2.2.1.14
######################

# # La función list() toma su argumento (una cadena) y crea una nueva lista 
# # que contiene todos los caracteres de la cadena, uno por elemento de la lista.

# # Nota: no es estrictamente una función de cadenas - list() 
# # es capaz de crear una nueva lista de muchas otras entidades 
# # (por ejemplo, de tuplas y diccionarios).

# # Demostración de la función list():
# print(list("abcabc"))

# # Demostración del método count():
# print("abcabc".count("b"))
# print('abcabc'.count("d"))

# # El método count() cuenta todas las apariciones del elemento dentro de la secuencia. 
# # La ausencia de tal elemento no causa ningún problema.

# Las cadenas de Python tienen un número significativo de métodos destinados 
# exclusivamente al procesamiento de caracteres. 
# No esperes que trabajen con otras colecciones. 
# La lista completa se presenta aquí: https://docs.python.org/3.4/library/stdtypes.html#string-methods.

######################
# Sección 2.2.1.15
######################

# Ejercicio 1

# ¿Cuál es la longitud de la siguiente cadena asumiendo que no hay 
# espacios en blanco entre las comillas?

# """
# """

# # 1

# Ejercicio 2

# ¿Cuál es el resultado esperado del siguiente código?

# s = 'yesteryears'
# the_list = list(s)
# print(the_list[3:6])

# # ['t', 'e', 'r']

# Ejercicio 3

# ¿Cuál es el resultado esperado del siguiente código?

# for ch in "abc":
#     print(chr(ord(ch) + 1), end='')

# # bcd

######################
# Sección 2.3.1.1
######################

# # Si el primer carácter dentro de la cadena es una letra 
# # (nota: el primer carácter es el elemento con un índice igual a 0, 
# # no es el primer carácter visible), se convertirá a mayúsculas.

# # Todas las letras restantes de la cadena se convertirán a minúsculas.

# # Demostración del método capitalize():

# print("'aBcD'.capitalize():  ", 'aBcD'.capitalize())
# print('"Alpha".capitalize(): ', "Alpha".capitalize())
# print("'ALPHA'.capitalize(): ", 'ALPHA'.capitalize())
# print("' Alpha'.capitalize():", ' Alpha'.capitalize())
# print("'123'.capitalize():   ", '123'.capitalize())
# print('"αβγδ".capitalize():  ', "αβγδ".capitalize())

# print('"buenas tardes".capitalize():  ', "buenas tardes".capitalize())

######################
# Sección 2.3.1.2
######################

# # La variante de un parámetro del método center() genera una copia 
# # de la cadena original, tratando de centrarla dentro de un campo 
# # de un ancho especificado.

# # El centrado se realiza realmente al agregar algunos espacios antes y 
# # después de la cadena.

# # No esperes que este método demuestre habilidades sofisticadas. Es bastante simple.


# Demostración del método center():
# print('[' + 'alpha'.center(10) + ']')

# for contador in range(10,15):
#     print('[' + 'alpha'.center(contador) + ']')

# La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio. Analiza el siguiente ejemplo:

# print('[' + 'gamma'.center(20, '*') + ']')

######################
# Sección 2.3.1.3
######################

# # El método endswith() comprueba si la cadena dada termina con el argumento 
# # especificado y devuelve True(verdadero) o False(falso), dependiendo del resultado.

# # Demostración del método endswith():
    
# if "epsilon".endswith("on"):
#     print("si")
# else:
#     print("no")

# t = "zeta"
# print('t.endswith("a"):  ', t.endswith("a"))
# print('t.endswith("a"):  ', t.endswith(chr(97)))
# print('t.endswith("A"):  ', t.endswith("A"))
# print('t.endswith("et"): ', t.endswith("et"))
# print('t.endswith("eta"):', t.endswith("eta"))

######################
# Sección 2.3.1.4
######################

# # El método find() es similar al método index(), el cual ya conoces
# # busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, 
# # pero:

# # Es más seguro, no genera un error para un argumento que contiene una subcadena 
# # inexistente (devuelve -1 en dicho caso).

# # Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.

# # Demostración del método find():
    
# print("Eta".find("ta"))
# print("Eta".find("mma"))

# t = 'theta'
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))

# # Si deseas realizar la búsqueda, no desde el principio de la cadena, 
# # sino desde cualquier posición, puedes usar una variante de dos parámetros d
# # el método find(). Mira el ejemplo:

# print('kappa'.find('a', 2))

# # Se puede emplear el método find() para buscar todas las ocurrencias de la subcadena, 
# # como aquí:

# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = the_text.find('the')

# while fnd != -1:
#     print("Posición", fnd)
#     fnd = the_text.find('the', fnd + 1)


# # Existe también una mutación de tres parámetros del método find()
# # el tercer argumento apunta al primer índice que no se tendrá en cuenta 
# # durante la búsqueda (en realidad es el límite superior de la búsqueda).

# # Observa el ejemplo a continuación:

# print('kappa'.find('a', 1, 4))
# print('kappa'.find('a', 2, 4))

######################
# Sección 2.3.1.5
######################

# # El método sin parámetros llamado isalnum() comprueba si la cadena 
# # contiene solo dígitos o caracteres alfabéticos (letras) y 
# # devuelve True(verdadero) o False(falso) de acuerdo al resultado.

# # Demostración del método the isalnum():
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())


# t = 'Six lambdas'
# print(t.isalnum())

# t = 'ΑβΓδ'
# print(t.isalnum())

# t = '20E1'
# print(t.isalnum())

######################
# Sección 2.3.1.6
######################

# El método isalpha() es más especializado, se interesa en letras solamente.

# Al contrario, el método isdigit() busca solo dígitos
# cualquier otra cosa produce False(falso) como resultado.

# # Ejemplo 1: Demostración del método isapha():
# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # Ejemplo 2: Demostración del método isdigit():
# print('2018'.isdigit())
# print("Year2019".isdigit())

######################
# Sección 2.3.1.7
######################

# # El método islower() es una variante de isalpha()
# # solo acepta letras minúsculas.

# # El método isspace() identifica espacios en blanco solamente
# # no tiene en cuenta ningún otro carácter (el resultado es entonces False).

# # El método isupper() es la versión en mayúscula de islower()
# # se concentra solo en letras mayúsculas.

# # Ejemplo 1: Demostración del método islower():
# print("Moooo".islower())
# print('moooo'.islower())

# # Ejemplo 2: Demostración del método isspace(:
# print(' \n '.isspace())
# print(" ".isspace())
# print("mooo mooo mooo".isspace())

# # Ejemplo 3: Demostración del método isupper():
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

######################
# Sección 2.3.1.8
######################

# # El método join() es algo complicado, así que déjanos guiarte paso a paso:

# # Como su nombre lo indica, el método realiza una unión y espera un argumento 
# # del tipo lista; se debe asegurar que todos los elementos de la lista sean cadenas: 
# # de lo contrario, el método generará una excepción TypeError.

# # Todos los elementos de la lista serán unidos en una sola cadena pero...
# # ... la cadena desde la que se ha invocado el método será utilizada como separador, 
# # puesta entre las cadenas.

# # La cadena recién creada se devuelve como resultado.

# # Demostración del método join():
    
# print(",".join(["omicron", "pi", "rho"]))

######################
# Sección 2.3.1.9
######################

# # El método lower() genera una copia de una cadena, 
# # reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas, 
# # y devuelve la cadena como resultado. 
# # Nuevamente, la cadena original permanece intacta.

# # Demostración del método lower():
# print("SiGmA=60".lower())

######################
# Sección 2.3.1.10
######################

# # El método sin parámetros lstrip() devuelve una cadena recién creada formada 
# # a partir de la original eliminando todos los espacios en blanco iniciales.

# # Demostración del método lstrip():
# print("[" + "    tau ".lstrip() + "]")

# # El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, 
# # pero elimina todos los caracteres incluidos en el argumento (una cadena), no solo espacios en blanco:

# print("www.cisco.com".lstrip(".w"))

# print("wa ww. cisco.com".lstrip(".a w")) # !!!!!!!!!!!!!!!!!!!!!!!

# print("pythoninstitute.org".lstrip(".org"))

# print("gro.pythoninstitute.org".lstrip(".org")) # !!!!!!!!!!!!!!!!!!!!!!!!

######################
# Sección 2.3.1.11
######################

# # El método replace() con dos parámetros devuelve una copia de la cadena original 
# # en la que todas las apariciones del primer argumento han sido reemplazadas 
# # por el segundo argumento.

# # Demostración del método replace():
    
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))

# print("Apple juice".replace("juicskjkasjkasjkase", ""))

# # Si el segundo argumento es una cadena vacía, 
# # reemplazar significa realmente eliminar el primer argumento de la cadena. 

# # ¿Qué tipo de magia ocurre si el primer argumento es una cadena vacía?

# print("Apple juice".replace("", "-"))

# # La variante del método replace() con tres parámetros emplea un tercer argumento 
# # (un número) para limitar el número de reemplazos.

# print("This is it!".replace("is", "are", 1))
# print("This is it!".replace("is", "are", 2))

# print("Apple juice".replace("", "-", 3))

######################
# Sección 2.3.1.12
######################

# # Los métodos de uno, dos y tres parámetros denominados rfind() 
# # hacen casi lo mismo que sus contrapartes (las que carecen del prefijo r), 
# # pero comienzan sus búsquedas desde el final de la cadena, 
# # no el principio (de ahí el prefijo r, de reversa).

# # Demostración del método rfind():
    
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9)) # fuera de rango
# print("tau tau tau".rfind("ta", 3, 9))

######################
# Sección 2.3.1.13
######################

# # Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip, 
# # pero afecta el lado opuesto de la cadena.

# # Demostración del método rstrip():
    
# print("[" + " upsilon ".rstrip() + "]")
# print("cisco.com".rstrip("moc."))

# print("cisco.com".rstrip(".soc")) # como si estuviéramos en un bucle buscando cualquiera de los caracteres al final de la cadena

######################
# Sección 2.3.1.14
######################

# El método split() divide la cadena y crea una lista de todas las subcadenas 
# detectadas.

# El método asume que las subcadenas están delimitadas por espacios en blanco
# los espacios no participan en la operación y no se copian en la lista resultante.

# Si la cadena está vacía, la lista resultante también está vacía.

# Demostración del método split():
# print("phi       chi\npsi".split())

######################
# Sección 2.3.1.15
######################

# # El método startswith() es un espejo del método endswith()
# # comprueba si una cadena dada comienza con la subcadena especificada.

# # El método strip() combina los efectos causados por rstrip() y lstrip()
# # crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.

# # Demostración del método startswith():
# print("omega".startswith("meg"))
# print("omega".startswith("om"))

# print()

# # Demostración del método strip():
# print("[" + "   aleph   ".strip() + "]")

######################
# Sección 2.3.1.16
######################

# # El método swapcase() crea una nueva cadena intercambiando todas las letras 
# # por mayúsculas o minúsculas dentro de la cadena original: 
# # los caracteres en mayúscula se convierten en minúsculas y viceversa.

# # Todos los demás caracteres permanecen intactos.

# # El método title() realiza una función algo similar 
# # cambia la primera letra de cada palabra a mayúsculas, 
# # convirtiendo todas las demás a minúsculas.

# # Por último, pero no menos importante, el método upper() hace una copia 
# # de la cadena de origen, reemplaza todas las letras minúsculas con sus 
# # equivalentes en mayúsculas, y devuelve la cadena como resultado.

# # Demostración del método swapcase():
# print("Yo sé que no sé nada.".swapcase())

# print()

# # Demostración del método title():
# print("Yo sé que no sé nada. Part 1.".title())

# print()

# # Demostración del método upper():
# print("Yo sé que no sé nada. Part 2.".upper())

######################
# Sección 2.3.1.17
######################

# # 1. Algunos de los métodos que ofrecen las cadenas son:

# # capitalize(): Convierte la inicial a Mayúsculas y el resto de la cadena a minúsculas.
# # center():     centra la cadena dentro de una longitud conocida.
# # count():      cuenta las ocurrencias de un carácter dado.
# # join():       une todos los elementos de una tupla/lista en una cadena.
# # lower():      convierte todas las letras de la cadena en minúsculas.
# # lstrip():     elimina los caracteres en blanco al principio de la cadena.
# # replace():    reemplaza una subcadena dada con otra.
# # rfind():      encuentra una subcadena comenzando por el final de la cadena.
# # rstrip():     elimina los caracteres en blanco al final de la cadena.
# # split():      divide la cadena en una subcadena usando un delimitador dado.
# # strip():      elimina los espacios en blanco iniciales y finales.
# # swapcase():   intercambia las mayúsculas y minúsculas de las letras.
# # title():      hace que la primera letra de cada palabra sea mayúscula.
# # upper():      convierte todas las letras de la cadena en letras mayúsculas.

# # 2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

# # endswith():   ¿La cadena termina con una subcadena determinada?
# # isalnum():    ¿La cadena consta solo de letras y dígitos?
# # isalpha():    ¿La cadena consta solo de letras?
# # islower():    ¿La cadena consta solo de letras minúsculas?
# # isspace():    ¿La cadena consta solo de espacios en blanco?
# # isupper():    ¿La cadena consta solo de letras mayúsculas?
# # startswith(): ¿La cadena comienza por un patrón determinado?


# # Ejercicio 1

# # ¿Cuál es el resultado esperado del siguiente código?

# for ch in "abc123XYX":
#     if ch.isupper():
#         print(ch.lower(), end='')
#     elif ch.islower():
#         print(ch.upper(), end='')
#     else:
#         print(ch, end='')


# # ABC123xyz



# # Ejercicio 2

# # ¿Cuál es el resultado esperado del siguiente código?

# s1 = '¿Dónde están las nevadas de antaño?'
# s2 = s1.split()
# print(s2[-2])


# # de



# # Ejercicio 3

# # ¿Cuál es el resultado esperado del siguiente código?

# the_list = ['¿Dónde', 'están', 'las', 'nevadas?']
# s = '*'.join(the_list)
# print(s)


# # ¿Dónde*están*las*nevadas?



# Ejercicio 4

# ¿Cuál es el resultado esperado del siguiente código?

# s = 'Es fácil o imposible'
# s = s.replace('fácil', 'difícil').replace('im', '')
# print(s)

#############################################################
# s = 'Es fácil o imposible'
# s = s.replace('fácil', 'difícil').replace('im', '').replace('difícil','fácil').replace('p','imp')

# print(s)

#####################################
# Sección 2.3.1.18 - Laboratorio
#####################################

# Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

# Debe aceptar únicamente un argumento: una cadena.
# Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
# Si la cadena está vacía, la función debería devolver una lista vacía.
# Su nombre debe ser mysplit().

# Salida esperada
# ['Ser', 'o', 'no', 'ser', 'esa', 'es,', 'la', 'pregunta']
# ['Ser', 'o', 'no', 'ser,esa', 'es', 'la', 'pregunta']
# []
# ['abc']
# []

# def mysplit(strng):
#     # devolver [] si la cadena está vacía o solo contiene espacios en blanco
#     if strng == '' or strng.isspace():
#         return [ ]
#     # preparar una lista para devolver
#     lst = []
#     # preparar una palabra para construir palabras subsecuentes
#     word = ''
#     # verificar si actualmente estamos dentro de una palabra 
#     # (es decir, si la cadena comienza con una palabra)
#     inword = not strng[0].isspace()
#     # iterar a través de todos los caracteres en cadena
#     for x in strng:
#           # si actualmente estamos dentro de una cadena ...
#         if inword:
#             # ... y el carácter actual no es un espacio ...
#             if not x.isspace():
#                 # ... actualizar palabra actual
#                 word = word + x
#             else:
#                 # ... de lo contrario, llegamos al final de la palabra, 
#                 # por lo que debemos agregarla a la lista ...
#                 lst.append(word)
#                 # ... y señalar que estamos ahora fuera de la palabra
#                 inword = False
#         else:
#             # si estamos fuera de la palabra y llegamos a un carácter no que no es un espacio en blanco
#             if not x.isspace():
#                 # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y ...
#                 inword = True
#                   # ... almacenar la primera letra de la nueva palabra
#                 word = x
#             else:
#                 pass
#         # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
#     if inword:
#         lst.append(word)
#     # devolver la lista a invocador
#     return lst

# print(mysplit("Ser o no ser, esa es la pregunta"))
# print(mysplit("Ser o no ser,esa es la pregunta"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))


# Alternativa 1
#  Albert
# def mysplit(strng):
#     salida = []
    
#     strng = strng.strip()

#     while " " in strng:
#         donde = strng.find(" ")
#         salida.append(strng[0:donde])
#         strng = strng[donde+1:]
#     if strng != "":
#         salida.append(strng)
#     return salida

# Alternativa 2
# # Nuria !!!

# def misplit(string):
#     novaparaula=[]
#     paraula=""
#     for letra in string:
#         if letra != " ":
#             paraula+=letra
#         else:
#             if paraula != "":
#                 novaparaula.append(paraula)
#                 paraula=""
#             else:
#                 continue
    
#     if len(paraula) != 0:
#         novaparaula.append(paraula)
#     return novaparaula



# print(misplit("Ser o no ser, esa es la pregunta"))
# print(misplit("Ser o no ser,esa es la pregunta"))
# print(misplit("   "))
# print(misplit(" abc "))
# print(misplit(""))
##########################
# Solución alternativa
##########################

# def mysplit(cadena):

#     lista_palabras = []

#     palabra = ''

#     for caracter in cadena:
    
#         if caracter != ' ':
#         # if not caracter.isspace():
#             palabra += caracter
#         else:
#             lista_palabras.append(palabra)
#             palabra = ''  
        
#     lista_palabras.append(palabra)
    
#     return lista_palabras

#################################3

# cadena = input("Introduce una cadena de caracteres: ")

# print(mysplit(cadena))

######################
# Sección 2.4.1.1
######################

# Las cadenas en Python pueden ser comparadas usando el mismo 
# conjunto de operadores que se emplean con los números.

# print('alpha' == 'alpha')
# print('alpha' != 'Alpha')

# print('alpha' < 'alphabet')
# print('beta' > 'Beta')

######################
# Sección 2.4.1.2
######################

# print('10' == '010')
# print('10' > '010')
# print('10' > '8')
# print('20' < '8')
# print('20' < '80')

# El comparar cadenas con los números generalmente es una mala idea.

# Las únicas comparaciones que puedes realizar con impunidad son aquellas 
# simbolizadas por los operadores == y !=. 

# print('10' == 10)
# print('10' != 10)
# print('10' == 1)
# print('10' != 1)
# print('10' > 10) # TypeError!!!

######################
# Sección 2.4.1.3
######################

# # Demostración de la función sorted():
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)             # devuelve una nueva lista!!!

# print(first_greek)
# print(first_greek_2)

# print()

# # Demostración del método sort():
    
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()                             # no se crea una nueva lista!!!
# print(second_greek)

######################
# Sección 2.4.1.4
######################

# itg = 13
# flt = 1.3
# si = str(itg)
# sf = str(flt)

# print(si + ' ' + sf)

# La transformación inversa solo es posible cuando la cadena representa un número válido. 
# Si no se cumple la condición, espera una excepción ValueError.

# Emplea la función int() si deseas obtener un entero, y float() si necesitas un valor punto flotante.

# si = '13'
# sf = '1.3'
# itg = int(si)
# flt = float(sf)

# print(itg + flt)

######################
# Sección 2.4.1.5
######################

# cadena == número es siempre False (falso).
# cadena != número es siempre True (verdadero).
# cadena >= número siempre genera una excepción.


# Ejercicio 1

# ¿Cuál de las siguientes líneas describe una condición verdadera?

# 'smith' > 'Smith'
# 'Smiths' < 'Smith'
# 'Smith' > '1000'
# '11' < '8'



# # 1, 3 y 4



# # Ejercicio 2

# # ¿Cuál es el resultado esperado del siguiente código?

# s1 = '¿Dónde están las nevadas de antaño?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3[1])


# # de



# # Ejercicio 3

# # ¿Cuál es el resultado esperado del siguiente código?

# s1 = '12.8'
# i = int(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)


## El código genera una excepción ValueError

#####################################
# Sección 2.4.1.6 - Laboratorio
#####################################

# digits = ['1111110',  	# 0
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
# 		print(ptrn)
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

#######################
## Alternativa
## Sergio

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
######################
# Sección 2.5.1.1
######################

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

# # variante con clave dinámica de cifrado

# strng = input("Mensaje: ")
# codigo = int(input("Código mensaje (número): "))

# if strng.isalpha():
#     strng2 = strng.upper()
#     cifradoCesar = ''
#     for c in strng2:
#         if c < chr(ord('Z')-codigo+1):
#             cifradoCesar += chr(ord(c)+codigo)
#         else:
#             cifradoCesar += chr(ord(c)-26+codigo)

# print(cifradoCesar)

######################
# Sección 2.5.1.2
######################

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


######################
# Sección 2.5.1.3
######################

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
    
######################
# Sección 2.5.1.4
######################

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
        
# # Datos de prueba        
# # Inglés: GB72 HBZU 7006 7212 1253 00
# # Francés: FR76 30003 03620 00020216907 50
# # Alemán: DE02100100100152517108

######################
# Sección 2.6.1.1
######################

# import math

# x = float(input("Ingresa x: "))
# y = math.sqrt(x)

# print("La raíz cuadrada de", x, "es igual a", y)

######################
# Sección 2.6.1.3
######################

# value = 1
# value /= 0

######################
# Sección 2.6.1.4
######################

# my_list = []
# x = my_list[0]

######################
# Sección 2.6.1.5
######################

# first_number = int(input("Ingresa el primer numero: "))
# second_number = int(input("Ingresa el segundo numero: "))

# if second_number != 0:
#     print(first_number / second_number)
# else:
#     print("Esta operación no puede ser realizada.")

# print("FIN.")

######################
# Sección 2.6.1.6
######################

# first_number = int(input("Ingresa el primer numero: "))
# second_number = int(input("Ingresa el segundo numero: "))

# try:
#     print(first_number / second_number)
# except:
#     print("Esta operación no puede ser realizada.")

# print("FIN.")

######################
# Sección 2.6.1.7
######################

# try:
#     print("1")
#     x = 1 / 0
#     print("2")
# except:
#     print("Oh cielos, algo salió mal...")

# print("3")

######################
# Sección 2.6.1.8
######################

# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")

######################
# Sección 2.6.1.9
######################

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

######################
# Sección 2.6.1.10
######################

# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
#     print(y)
# except ValueError:
#     print("Debes ingresar un valor entero.")
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")

######################
# Sección 2.6.1.11
######################

# try:
#     x = int(input("Ingresa un número: "))
#     y = 1 / x
#     print(y)
# except ValueError:
#     print("Debes ingresar un valor entero.")

# print("FIN.")


######################
# Sección 2.6.1.12
######################

# Ejercicio 1

# ¿Cuál es el resultado esperado del siguiente código?

# try:
#     print("Tratemos de hacer esto")
#     print("#"[2])
#     print("¡Tuvimos éxito!")
# except:
#     print("Hemos fallado")
# print("Hemos terminado")


# # Tratemos de hacer esto
# # Hemos fallado
# # Hemos terminado



# # Ejercicio 2

# # ¿Cuál es el resultado esperado del siguiente código?

# try:
#     print("alpha"[1/0])
# except ZeroDivisionError:
#     print("cero")
# except IndexingError:
#     print("índice")
# except:
#     print("algo")


# # cero

######################
# Sección 2.7.1.1
######################

# ZeroDivisionError es un caso especial de una clase de excepción más general llamada ArithmeticError.
# ArithmeticError es un caso especial de una clase de excepción más general llamada solo Exception.
# Exception es un caso especial de una clase más general llamada BaseException.

######################
# Sección 2.7.1.2
######################

# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("Uuupsss...")

# print("FIN.")

######################
# Sección 2.7.1.3
######################

# try:
#     y = 1 / 0

# except ZeroDivisionError:           # Subtipo específico
#     print("¡División entre Cero!")
# except ArithmeticError:             # Supertipo específico
#     print("¡Problema Aritmético!")
# except Exception:
#         print("alguna excepción")

# print("FIN.")

######################
# Sección 2.7.1.4
######################

# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print("¡Problema Aritmético!")
#     return None

# bad_fun(0)

# print("FIN.")

######################
# Sección 2.7.1.5
######################

# def bad_fun(n):
#     raise ZeroDivisionError


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¿Que pasó? ¿Un error?")

# print("FIN.")

######################
# Sección 2.7.1.6
######################

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

######################
# Sección 2.7.1.7
######################

# import math

# x = float(input("Ingresa un número: "))

# assert x >= 0.0

# x = math.sqrt(x)

# print(x)

######################
# Sección 2.7.1.8
######################

# Ejercicio 1

# ¿Cuál es la salida esperada del siguiente código?

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("cero")
# except ArithmeticError:
#     print("arit")
# except:
#     print("algo")


# # cero



# Ejercicio 2

# ¿Cuál es la salida esperada del siguiente código?

# try:
#     print(1/0)
# except ArithmeticError:
#     print("arit")
# except ZeroDivisionError:
#     print("cero")
# except:
#     print("algo")


# # arit



# Ejercicio 3

# ¿Cuál es la salida esperada del siguiente código?

# def foo(x):
#     assert x
#     return 1/x


# try:
#     print(foo(0))
# except ZeroDivisionError:
#     print("cero")
# except:
#     print("algo")


# # algo


