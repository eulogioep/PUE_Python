######################
# Sección 3.3.1.4
######################

# flag_register = 8

# print(format(flag_register, '#032b'))

# # ## Comprobar el estado del bit

# the_mask = 8 # el peso del bit es igual a 2 elevado a 3 (8) - tercer bit

# print(format(the_mask, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")

# # Reiniciar el bit a 0

# flag_register = flag_register & ~the_mask
# # flag_register &= ~the_mask # alternativa

# print("Cambiando tercer bit a cero")
# print(format(flag_register, '#032b'))

# # verificar si el tercer bit está en 0 o 1

# if flag_register & the_mask:
#     # Mi bit se estableció en 1.
#     print("tercer bit igual a 1")
# else:
#     # Mi bit se restableció a 0.
#     print("tercer bit igual a 0")

# # establecer el tercer bit a 1

# flag_register = flag_register | the_mask
# flag_register |= the_mask

# print("Estableciendo tercer bit a 1")
# print(format(flag_register, '#032b'))

# # Negación del tercer bit

# flag_register = flag_register ^ the_mask
# # # flag_register ^= the_mask # CUIDADO!!!, si ejecuto ambas instrucciones niega el bit dos veces!!!!

# print("Negando tercer bit")
# print(format(flag_register, '#032b'))

# flag_register ^= the_mask

# print("Negando de nuevo tercer bit")
# print(format(flag_register, '#032b'))

######################################################################
# import time

# var = 2

# inicio = time.time()



# for i in range(30):

#     var **= 2    
    
# fin1 = time.time()

# print(round(fin1 - inicio, 2), "segundos")


# var = 2

# for i in range(30):

#     var = var << 1
#     print(var)

# fin2 = time.time()
    

# print(round(fin2 - fin1, 2), "segundos")


######################
# Sección 3.3.1.5
######################

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

# 17 >> 1 → 17 // 2 (17 dividido entre 2 elevado a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 elevado a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

# var = 17

# print(var)
# print(format(var, '#032b'))

# var_right = var >> 1

# print(var_right)
# print(format(var_right, '#032b'))

# var_left = var << 2

# print(var_left)
# print(format(var_left, '#032b'))





