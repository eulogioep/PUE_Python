from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.FunI())

#from extra.iota import FunI
#print(FunI())

##################################

# from sys import path

# path.append('..\\packages')

# import extra.good.best.sigma
# from extra.good.best.tau import FunT

# print(extra.good.best.sigma.FunS())
# print(FunT())


######################################

# from sys import path

# path.append('..\\packages')

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp

# print(sig.FunS())
# print(alp.FunA())

#####################################
# Python puede también acceder a una estructura de paquetes dentro de un archivo .zip

# from sys import path

# path.append('..\\packages\\extrapack.zip')

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp
# from extra.iota import FunI
# from extra.good.beta import FunB

# print(sig.FunS())
# print(alp.FunA())
# print(FunI())
# print(FunB())

#########################################

# # Importar un modulo y no ejecutarlo directamente

# import sys

# if __name__ == "__main__":
#     print("¡No hagas eso!")
#     sys.exit()
    
# #####################################

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

########################################

