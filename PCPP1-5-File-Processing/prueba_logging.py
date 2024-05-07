# El logging en Python es una herramienta útil para rastrear eventos que ocurren durante la 
# ejecución de un programa. Aquí tienes algunos detalles sobre cómo funciona:

# Logger: Los loggers registran las acciones durante la ejecución de un programa. 
# El desarrollador agrega llamadas de registro a su código para indicar que ciertos 
# eventos han ocurrido1. Por ejemplo, puedes usar los métodos debug(), info(), warning(),
# error() y critical() para registrar diferentes niveles de información.

# Handler: Los handlers recopilan la información del logger y la reenvían a un destino específico.
#  Puedes configurar un handler para enviar los registros a un archivo, la consola o incluso
# a un servidor remoto2.

# Formatter: Los formatters especifican el diseño de los registros en el resultado final.
# Puedes personalizar cómo se muestra la información en los registros, como agregar la hora,
# el nivel de registro y el mensaje3.

# Filter: Los filters permiten crear definiciones aún más precisas para los mensajes de salida.
# Puedes usarlos para filtrar registros específicos según ciertos criterios4.

#############

# import logging

# logger = logging.getLogger()
# hello_logger = logging.getLogger('hello')
# hello_world_logger = logging.getLogger('hello.world')
# recommended_logger = logging.getLogger(__name__)

#### Nivel de Logger ####################################

# Level Name             Valor

# CRITICAL                50
# ERROR                   40
# WARNING                 30
# INFO                    20
# DEBUG                   10
# NOTSET                   0


# import logging

# logging.basicConfig()

# logger = logging.getLogger()

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

##### Método setLevel #######################################

# import logging

# logging.basicConfig()

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

######### Configuración básica ################################

# import logging

# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

# logger = logging.getLogger()

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')


######## Ejemplo de primer handler (log) #################

# import logging

# logger = logging.getLogger(__name__)

# handler = logging.FileHandler('prod.log', mode='w')
# handler.setLevel(logging.CRITICAL)

# logger.addHandler(handler)

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

###### Ejemplo del primer formateador #####################################

# import logging

# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# logger = logging.getLogger(__name__)

# handler = logging.FileHandler('prod.log', mode='w')
# handler.setLevel(logging.CRITICAL)

# formatter = logging.Formatter(FORMAT)
# handler.setFormatter(formatter)

# logger.addHandler(handler)

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

####### Laboratorio Logger ###################################

import logging
import random

FORMAT = '%(levelname)s - %(message)s'


class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()


##########################################################

