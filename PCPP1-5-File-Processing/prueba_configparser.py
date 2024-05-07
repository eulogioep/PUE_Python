# El módulo configparser en Python es una biblioteca incorporada que proporciona una forma de 
# leer y escribir archivos de configuración. Permite a los programadores definir opciones de 
# configuración y valores predeterminados en un archivo de configuración y luego usar esos 
# valores en su programa1. Aquí tienes más detalles:

# Estructura similar a archivos INI: El módulo configparser implementa un lenguaje básico de 
# configuración que se asemeja a la estructura encontrada en los archivos INI de Microsoft Windows. 
# Esto facilita la personalización de programas Python por parte de los usuarios finales.
# Clase ConfigParser: La clase ConfigParser proporcionada por este módulo permite leer y escribir 
# archivos de configuración. Puedes tratarla como un diccionario, lo que significa que puedes 
# agregar secciones, claves y valores de manera programática2.

########## Ejemplo ##########

# import configparser

# config = configparser.ConfigParser()
# print(config.read('config.ini'))

# print('Sections:', config.sections(),'\n')

# print('mariadb section:')
# print('Host:', config['mariadb']['host'])
# print('Database:', config['mariadb']['name'])
# print('Username:', config['mariadb']['user'])
# print('Password:', config['mariadb']['password'], '\n')

# print('redis section:')
# print('Host:', config['redis']['host'])
# print('Port:', int(config['redis']['port']))
# print('Database number:', int(config['redis']['db']))

####### Lectura de configuraciones ##################

# import configparser

# config = configparser.ConfigParser()

# dict = {
#     'DEFAULT': {
#         'host': 'localhost'
#     },
#     'mariadb': {
#         'name': 'hello',
#         'user': 'root',
#         'password': 'password'
#     },
#     'redis': {
#         'port': 6379,
#         'db': 0
#     }
# }

# config.read_dict(dict)

# print('Sections:', config.sections(),'\n')

# print('mariadb section:')
# print('Host:', config['mariadb']['host'])
# print('Database:', config['mariadb']['name'])
# print('Username:', config['mariadb']['user'])
# print('Password:', config['mariadb']['password'], '\n')

# print('redis section:')
# print('Host:', config['redis']['host'])
# print('Port:', int(config['redis']['port']))
# print('Database number:', int(config['redis']['db']))


###### Creación de un archivo de configuración #################################

# import configparser

# config = configparser.ConfigParser()

# config['DEFAULT'] = {'host': 'localhost'}
# config['mariadb'] = {'name': 'hello',
#                      'user': 'root',
#                      'password': 'password'}
# config['redis'] = {'port': 6379,
#                    'db': 0}

# with open('config.ini', 'w') as configfile:
#     config.write(configfile)

####### Laboratorio #################################

# import configparser


# class MessConfigParser:
#     def __init__(self):
#         self.prod_sections = {}
#         self.dev_sections = {}

#     def parse(self, filename):
#         config = configparser.ConfigParser()
#         config.read(filename)

#         for section in config.sections():
#             for key in config[section]:
#                 if key == 'env':
#                     continue
#                 else:
#                     dict = {key: config[section][key]}

#                     if config[section]['env'] == 'prod':
#                         if section not in self.prod_sections:
#                             self.prod_sections[section] = {}
#                         self.prod_sections[section].update(dict)
#                     else:
#                         if section not in self.dev_sections:
#                             self.dev_sections[section] = {}
#                         self.dev_sections[section].update(dict)


# class ConfigParserHelper:
#     def write_from_dict(self, filename, dict):
#         config = configparser.ConfigParser()
#         config.read_dict(dict)

#         with open(filename, 'w') as configfile:
#             config.write(configfile)

# mess_config_parser = MessConfigParser()
# mess_config_parser.parse('mess.ini')

# helper = ConfigParserHelper()
# helper.write_from_dict('prod_config.ini', mess_config_parser.prod_sections)
# helper.write_from_dict('dev_config.ini', mess_config_parser.dev_sections)


##############################