
## Javier Arozamena

# c0=-1
# # si el valor introducido no es superior a 1
# while c0 <= 0:  
#     print("Has introducido un valor incorrecto, vuelve a intentarlo...")
#     # volvemos a pedir el numero hasta que sea superior a 1
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


################
## Eulogio

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

# Pablo

# c0 = int(input("Ingrese un número natural: "))
# steps = 0

# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     steps += 1
#     print(c0)

# print("Se necesitaron", steps, "pasos para alcanzar c0 = 1.")


# David

# # Pedir al usuario que ingrese un numero natural
# c0 = int(input("Ingrese un numero natural: "))

# # Verificar si el numero ingresado es positivo
# if c0 <= 0:
#     print("El numero debe ser un numero natural positivo.")
# else:
#     pasos = 0  # Inicializar el contador de pasos
#     while c0 != 1:
#         print(c0, end=' ')  # Imprimir el valor actual de c0
#         if c0 % 2 == 0:  # Si c0 es par
#             c0 //= 2
#         else:  # Si c0 es impar
#             c0 = 3 * c0 + 1
#         pasos += 1  # Incrementar el contador de pasos
#     print(1)  # Imprimir el ultimo valor que siempre será 1
#     print("Se necesitaron", pasos, "pasos para alcanzar el valor 1.")

# Jose Puga

# c0 = int(input("Ingresa c0: "))
# if c0 > 1:
#     steps = 0
#     while c0>1:
#         if c0 %2 != 0:
#             c0=c0*3+1
#             print(c0)
#         else:
#             c0 //= 2
#             print(c0)
#         steps +=1
# else:
#     print("Valor de c0 incorrecto")
# print("pasos =",steps)

# Pepe

# c0 = -1
# contador = 0
# while c0 <=0:
#     c0 = int(input("introduce un numero positivo: "))
# else:    
#     print("has introducido el ", c0)
#     #c0 = numero
#     while c0 !=1:
#         if c0 % 2 == 0:
#             c0 = c0 //2 #división entera
#         else:
#             c0 = c0*3 + 1     
#         contador +=1
#         print(c0)
#     print("veces ", contador)