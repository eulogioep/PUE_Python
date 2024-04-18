# import module

# # Imprimo accediendo a una variable del modulo "module"
# print(module.__counter)

from sys import path

path.append('..\\modules') # Windows
#path.append('../modules')    # MacOS - Unix - Linux

# for entrada in path:
#     print(entrada)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
print('Numero de llamadas a las funciones del modulo:', module.__counter)