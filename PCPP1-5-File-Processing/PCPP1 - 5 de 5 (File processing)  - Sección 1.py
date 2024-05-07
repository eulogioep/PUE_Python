###################
# Sección 1.1.1.3
###################

# import sqlite3

###################
# Sección 1.1.1.4
###################

# import sqlite3

# conn = sqlite3.connect('hello.db')

###########################

# import sqlite3

# conn = sqlite3.connect('C:\sqlite\hello.db')

###########################

# import sqlite3

# conn = sqlite3.connect(':memory:')

###################
# Sección 1.1.1.6
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')

#########################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')

###################
# Sección 1.1.1.8
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')

# result = c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))

###################
# Sección 1.1.1.9
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')
# c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
# conn.commit()
# conn.close()

###################
# Sección 1.1.1.10
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')
# tasks = [
#     ('My first task', 1),
#     ('My second task', 5),
#     ('My third task', 10),
# ]
# c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
# conn.commit()
# conn.close()

###################
# Sección 1.1.1.11
###################

# import sqlite3

# class Todo:
#     def __init__(self):
#         self.conn = sqlite3.connect('todo.db')
#         self.c = self.conn.cursor()
#         self.create_task_table()
        
#     def create_task_table(self):
#         self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                      id INTEGER PRIMARY KEY,
#                      name TEXT NOT NULL,
#                      priority INTEGER NOT NULL
#                      );''')
    
#     def add_task(self):
#         name = input('Enter task name: ')
#         priority = int(input('Enter priority: '))
        
#         self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
#         self.conn.commit()

# app = Todo()
# app.add_task()

###################
# Sección 1.1.1.13
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# for row in c.execute('SELECT * FROM tasks'):
#     print(row)
# conn.close()

###################
# Sección 1.1.1.14
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# rows = c.fetchall()

# for row in rows:
#     print(row)
# conn.close()

###################
# Sección 1.1.1.15
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)
# conn.close()

#######################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# row = c.fetchone()
# while row:
#     print(row)
#     row = c.fetchone()
# print(row)
# conn.close()

#######################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')

# while True:
#     row = c.fetchone()
#     if row is None: 
#         break
#     print(row)
# conn.close()

#################################
# Laboratorio de Sección 1.2.1.1
#################################

# import sqlite3

# class Todo:
#     def __init__(self):
#         self.conn = sqlite3.connect('todo.db')
#         self.c = self.conn.cursor()
#         self.create_tasks_table()

#     def create_tasks_table(self):
#         self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                      id INTEGER PRIMARY KEY,
#                      name TEXT NOT NULL,
#                      priority INTEGER NOT NULL
#                      );''')

#     def add_task(self):
#         name = input('Enter task name: ')
#         priority = int(input('Enter priority: '))

#         if len(name) == 0 or priority < 1:
#             return

#         if self.find_task(name) is not None:
#             return

#         self.c.execute(
#             'INSERT INTO tasks (name, priority) VALUES (?,?)',
#             (name, priority))
#         self.conn.commit()

#     def find_task(self, name):
#         for row in self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,)):
#             if row[1] == name:
#                 return row

#         return None

#     def show_tasks(self):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             print(row)

# app = Todo()
# app.add_task()
# app.show_tasks()

#################################
## José Antonio
#################################

# # '''
# # Cree un find_taskmétodo que tome el nombre de la tarea como argumento. El método debe devolver el registro encontrado o Noneno.
# # Bloquea la posibilidad de ingresar una tarea vacía (el nombre no puede ser una cadena vacía).
# # Bloquea la capacidad de ingresar una prioridad de tarea menor que 1.
# # Utilice el find_task método para bloquear la capacidad de ingresar una tarea con el mismo nombre.
# # Cree un método llamado show_tasks, responsable de mostrar todas las tareas guardadas en la base de datos.
# # '''

# import sqlite3
# ruta_ddbb = 'todo.db'
# def validar_cnx(fx):
#     def cnx_validada(*args, **kwargs):
#         try:
#             return fx(*args, **kwargs)
#         except Exception as e:
#             print(e)
#             return None
#     return cnx_validada

# def nombre():
#     nombre = ''
#     while not nombre:
#         nombre = input('Introduce el nombre de la tarea: ')
#     return nombre

# def prioridad():
#     valor = 0
#     while valor < 1:
#         try:
#             valor = int(input('Introduce prioridad: '))
#         except Exception as e:
#             print(e)
#             valor = 0
#     return valor

# def find_task(cnx, tarea):
#     registros =cnx.execute('SELECT 1 FROM tasks WHERE name = ?',  (tarea,))
#     resultado = registros.fetchone()
#     return resultado

# # validar la conexión a la bbdd
# @validar_cnx
# def show_task():
#     conexion = sqlite3.connect(ruta_ddbb)
#     conexion.cursor()
#     print('id  \ttarea     \tprioridad')
#     for registro in  conexion.execute('SELECT * FROM tasks'):
#         print(registro[0], '\t', registro[1], '\t', registro[2])
#     conexion.close()

# # validar la conexión a la bbdd
# @validar_cnx
# def insertar(tarea, preferencia):
#     conexion = sqlite3.connect(ruta_ddbb)
#     if find_task(conexion, tarea) is None:
#         conexion.cursor()
#         conexion.execute('INSERT INTO tasks(name, priority) values(?, ?)', (tarea, preferencia))
#         conexion.commit()#validación de la transación
#         print('Regsitro añadido....')
#     else: 
#         print('el registro ya existe...')
#     conexion.close()

# def enter_tarea():
#     nb = nombre()
#     pr = prioridad()
#     insertar(nb, pr)


# enter_tarea()
# show_task()

###################
# Sección 1.3.1.1
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
# conn.commit()
# conn.close()

###################
# Sección 1.3.1.2
###################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('DELETE FROM tasks WHERE id = ?', (1,))
# conn.commit()
# conn.close()

#################################
# Laboratorio de Sección 1.4.1.1
#################################

# import sqlite3

# class Todo:
#     def __init__(self):
#         self.conn = sqlite3.connect('todo.db')
#         self.c = self.conn.cursor()
#         self.create_tasks_table()

#     def create_tasks_table(self):
#         self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                      id INTEGER PRIMARY KEY,
#                      name TEXT NOT NULL,
#                      priority INTEGER NOT NULL
#                      );''')

#     def add_task(self):
#         name = input('Enter task name: ')
#         priority = int(input('Enter priority: '))

#         if len(name) == 0 or priority < 1:
#             return

#         self.find_task("name",name)
#         if self.c.fetchone() is None:
#             print('\nCan´t add new row - A task with this name already exists\n')
#             return

#         self.c.execute(
#             'INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
#         self.conn.commit()

#     def find_task(self, column, value):
#         self.c.execute('SELECT 1 FROM tasks WHERE ? = ?', (column, value))
#         return self.c.fetchone()

#     def show_tasks(self):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             print(row)

#     def change_priority(self):
#         task_id = int(input('Enter task id: '))
#         new_priority = int(input('Enter new priority: '))

#         if new_priority < 1:
#             return

#         self.find_task("id",task_id)
#         if self.c.fetchone() is None:
#             print("\nCan´t update row - Task id does not exist in the database\n")
#             return
#         self.c.execute(
#             'UPDATE tasks SET priority = ? WHERE id = ?',
#             (new_priority, task_id))
#         self.conn.commit()

#     def delete_task(self):
#         task_id = int(input('Enter task id: '))

#         self.find_task("id",task_id)
#         if self.c.fetchone() is None:
#             print("\nCan´t delete row - Task id does not exist in the database\n")
#             return
#         self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id, ))
#         self.conn.commit()


# class Menu:
#     def __init__(self):
#         self.app = Todo()

#     def open(self):
#         self.open = True
#         while self.open:
#             self.draw()
#             option = int(input('Choose an option [1-5]: '))

#             if option == 1:
#                 self.app.show_tasks()
#             elif option == 2:
#                 self.app.add_task()
#             elif option == 3:
#                 self.app.change_priority()
#             elif option == 4:
#                 self.app.delete_task()
#             elif option == 5:
#                 self.close()
#             else:
#                 input('Option not found. Please choose an option again...')

#     def draw(self):
#         print('1. Show Tasks')
#         print('2. Add Task')
#         print('3. Change Priority')
#         print('4. Delete Task')
#         print('5. Exit')

#     def close(self):
#         self.open = False

# menu = Menu()
# menu.open()


#############################
## Jose Antonio
## Este ejemplo actualiza o elimina por nombre, no por id

# '''
# Cree un find_taskmétodo que tome el nombre de la tarea como argumento. El método debe devolver el registro encontrado o Noneno.
# Bloquea la posibilidad de ingresar una tarea vacía (el nombre no puede ser una cadena vacía).
# Bloquea la capacidad de ingresar una prioridad de tarea menor que 1.
# Utilice el find_task método para bloquear la capacidad de ingresar una tarea con el mismo nombre.
# Cree un método llamado show_tasks, responsable de mostrar todas las tareas guardadas en la base de datos.
# '''

# import sqlite3
# ruta_ddbb = 'todo.db'
# def validar_cnx(fx):
#     def cnx_validada(*args, **kwargs):
#         try:
#             return fx(*args, **kwargs)
#         except Exception as e:
#             print(e)
#             return None
#     return cnx_validada

# def nombre():
#     nombre = ''
#     while not nombre:
#         nombre = input('Introduce el nombre de la tarea: ')
#     return nombre

# def prioridad():
#     valor = 0
#     while valor < 1:
#         try:
#             valor = int(input('Introduce prioridad: '))
#         except Exception as e:
#             print(e)
#             valor = 0
#     return valor

# def find_task(cnx, tarea):
#     registros =cnx.execute('SELECT 1 FROM tasks where name = ?',  (tarea,))
#     resultado = registros.fetchone()
#     return resultado

# @validar_cnx
# def show_task():
#     conexion = sqlite3.connect(ruta_ddbb)
#     conexion.cursor()
#     print('id  \ttarea     \tprioridad')
#     for registro in  conexion.execute('SELECT * FROM tasks'):
#         print(registro[0], '\t', registro[1], '\t', registro[2])
#     conexion.close()

# @validar_cnx
# def insertar(tarea, preferencia):
#     conexion = sqlite3.connect(ruta_ddbb)
#     if find_task(conexion, tarea) is None:
#         conexion.cursor()
#         conexion.execute('INSERT INTO tasks(name, priority) values(?, ?)', (tarea, preferencia))
#         conexion.commit()#validación de la transación
#         print('Registro añadido....')
#     else: 
#         print('el registro ya existe...')
#     conexion.close()

# @validar_cnx
# def change_priority(tarea, prioridad):
#     conexion = sqlite3.connect(ruta_ddbb)
#     conexion.cursor()
#     if find_task(conexion, tarea):
#         conexion.execute('UPDATE tasks SET priority = ? WHERE name = ?', (prioridad, tarea))
#         conexion.commit()
#         conexion.close()
#         print('Registro modificado....')
#     else: 
#         print('el registro no existe...')

# @validar_cnx
# def  delete_task(tarea):
#     conexion = sqlite3.connect(ruta_ddbb)
#     conexion.cursor()
#     if find_task(conexion, tarea):
#         conexion.execute('DELETE FROM tasks WHERE name = ?', (tarea, ))
#         conexion.commit()
#         conexion.close()
#         print('Registro borrado....')
#     else: 
#         print('el registro no existe...')

# def borrar():
#     print('Borrar')
#     nb = nombre()
#     delete_task(nb)

# def actualizar():
#     print('Actulizar')
#     nb = nombre()
#     pr = prioridad()
#     change_priority(nb, pr)

# def enter_tarea():
#     print('Insertar')
#     nb = nombre()
#     pr = prioridad()
#     insertar(nb, pr)

# show_task()
# #enter_tarea()
# #actualizar()
# borrar()
# show_task()


###################
# Sección 2.1.1.3
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()

# print(root.tag)

# #########################

# import xml.etree.ElementTree as ET

# root = ET.fromstring('<data>value</data>')

# print(root.tag,'-', root.text)

###################
# Sección 2.1.1.4
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print('The root tag is:', root.tag)
# print('The root has the following children:')
# for child in root:
#     print(child.tag, child.attrib)

###################
# Sección 2.1.1.5
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print("My books:\n")
# for book in root:
#     print('Title: ', book.attrib['title'])
#     print('Author:', book[0].text)
#     print('Year:  ', book[1].text, '\n')

###################
# Sección 2.1.1.6
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for author in root.iter('author'):
#     print(author.text)

###################
# Sección 2.1.1.7
###################
# # The example doesn't return any results, because the findall method can only iterate 
# # over the book elements that are the closest children of the root element. 

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for author in root.findall('author'):
#     print(author.text)

# # The correct code looks like this:

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for book in root.findall('book'):
#     print(book.get('title'))

###################
# Sección 2.1.1.8
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print(root.find('book').get('title'))

##################################
# Laboratorio de Sección 2.2.1.1
##################################

# import xml.etree.ElementTree as ET


# class TemperatureConverter:
#     def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
#         return 9.0/5.0 * temperature_in_celsius + 32


# class ForecastXmlParser:
#     def __init__(self, temperature_converter):
#         self.temperature_converter = temperature_converter

#     def parse(self, file):
#         tree = ET.parse(file)
#         root = tree.getroot()
#         for child in root:
#             day = child.find('day').text
#             temperature_in_celsius = int(child.find(
#                 'temperature_in_celsius').text)
#             temperature_in_fahrenheit = round(
#                 self.temperature_converter.convert_celsius_to_fahrenheit(
#                     temperature_in_celsius), 1)
#             print('{0}: {1} Celsius, {2} Fahrenheit'.format(
#                 day, temperature_in_celsius, temperature_in_fahrenheit))

# temperature_converter = TemperatureConverter()
# forecast_xml_parser = ForecastXmlParser(temperature_converter)
# forecast_xml_parser.parse('forecast.xml')

########################
## Jose Antonio
## método estático

# import xml.etree.ElementTree as ET

# class TemperatureConvertery:
#     @staticmethod
#     def convert_celsius_to_fahrenheit(celsius):
#         return 9/5 * celsius+ 32

# class ForecastXmlParsery:
#     def __init__(self,ruta_xml) -> None:
#         self.ruta_xml = ruta_xml
#         self.__leer_xml()
    
#     def __leer_xml(self):
#         arbol = ET.parse(self.ruta_xml)
#         raiz = arbol.getroot()
#         for dia in raiz:
#             dia_semana = dia.find('day').text
#             temp_Celsius = dia.find('temperature_in_celsius').text
#             temp_Fahr = round(TemperatureConvertery.convert_celsius_to_fahrenheit(float(temp_Celsius)), 2)
#             print(dia_semana, ':', temp_Celsius, 'Celsius,', temp_Fahr, 'Fahrenheit')   

# obj_forecat = ForecastXmlParsery('forecast.xml')

#######################################
## Mariano

# import xml.etree.ElementTree as ET

# class TemperatureConverter():
    
#     def convert_celsius_to_fahrenheit(self, grados_celcius):
#         grados_fahrenheit = 9/5 * float(grados_celcius) + 32
#         return grados_fahrenheit

# class ForecastXmlParser():
#     def __init__(self,xml_file) -> None:
#         self.xml_file = xml_file
    
#     def parse(self):
#         #Monday: 28 Celsius, 82.4 Fahrenheit
#         #Tuesday: 27 Celsius, 80.6 Fahrenheit
#         #<item>
#         #   <day>Monday</day>
#         #   <temperature_in_celsius>28</temperature_in_celsius>
#         #</item>
#         tree = ET.parse(self.xml_file)
#         root = tree.getroot()
#         converter = TemperatureConverter()
#         for item in root:
#             print(item[0].text+':', item[1].text,'Celsius,',round(converter.convert_celsius_to_fahrenheit(item[1].text),2),'Fahrenheit\n' )
#             #print('temperature_in_celsius:  ', item[1].text, '\n')
            
# xml = ForecastXmlParser("forecast.xml")
# xml.parse()

#########################
## Alba
## Método estático

# import xml.etree.ElementTree as ET

# class TemperatureConverter:
#     @staticmethod
#     def convert_celsius_to_fahrenheit(cel):
#         fah = 9/5 * int(cel) + 32
#         return fah

# class ForecastXmlParser:
#     @staticmethod
#     def parse_xml(xml):
#         try:
#             tree = ET.parse(xml)
#             root = tree.getroot()
#             for child in root:
#                 day = child.find('day').text
#                 temperature_in_celsius = child.find('temperature_in_celsius').text
#                 temperature_in_farenheit = str(round(TemperatureConverter.convert_celsius_to_fahrenheit(temperature_in_celsius),1))
#                 print(day+": "+temperature_in_celsius+" Celsius, "+temperature_in_farenheit+" Fahrenheit")
#         except FileNotFoundError:
#             print("The document does not exist.")
#         except ET.ParseError:
#             print("The document contains invalid data")

# ForecastXmlParser.parse_xml('forecast.xml')

###################
# Sección 2.3.1.1
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

###################
# Sección 2.3.1.2
###################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

###################
# Sección 2.3.1.3
###################
        
# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

###################
# Sección 2.3.1.4
###################
        
# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

# tree.write('movies.xml', 'UTF-8', True)

###################
# Sección 2.3.1.5
###################
        
# import xml.etree.ElementTree as ET

# root = ET.Element('data')
# ET.dump(root)

###################
# Sección 2.3.1.6
###################

# import xml.etree.ElementTree as ET

# root = ET.Element('data')
# movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
# movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
# ET.dump(root)

#################################
# Laboratorio de Sección 2.4.1.1
#################################

# import xml.etree.ElementTree as ET

# class XmlTreeHelper:
#     def add_tags_with_text(self, parent, tags):
#         elements = []
#         for tag in tags:
#             element = ET.SubElement(parent, tag)
#             element.text = tags[tag]
#             elements.append(element)
#         return elements

# root = ET.Element('shop')

# category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

# product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
# product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
# product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})

# xml_tree_helper = XmlTreeHelper()

# xml_tree_helper.add_tags_with_text(product_1, {
#     'type': 'cereals',
#     'producer': 'OpenEDG Foods Limited',
#     'price': '9.90',
#     'currency': 'USD'
# })

# xml_tree_helper.add_tags_with_text(product_2, {
#     'type': 'pasta',
#     'producer': 'Programmers Eat Pasta Gmbh',
#     'price': '14.49',
#     'currency': 'EUR'
# })

# xml_tree_helper.add_tags_with_text(product_3, {
#     'type': 'beverages',
#     'producer': 'Drinks4Coders Inc.',
#     'price': '19.75',
#     'currency': 'USD'
# })

# # ET.dump(root)

# tree = ET.ElementTree(root)
# tree.write('shop.xml', 'UTF-8', True)

############################
## José Antonio
## estandarizado en forma de función

# import xml.etree.ElementTree as ET

# raiz = ET.Element('shop')

# categoria = ET.SubElement(raiz, 'category', {'name': 'Vegan Products'})
# def crear_producto(nombre_producto, producto_, productor_, precio_, moneda_):

#     producto = ET.SubElement(categoria, 'product', {'name': nombre_producto})
#     tipo = ET.SubElement(categoria, 'type')
#     tipo.text=producto_

#     productor = ET.SubElement(categoria, 'producer')
#     productor.text=productor_

#     precio = ET.SubElement(categoria, 'price')
#     precio.text =precio_

#     moneda = ET.SubElement(categoria, 'currency')
#     precio.text = moneda_

# crear_producto('Good Morning Sunshine', 'cereals', ' OpenEDG Testing Service', ' 9.90', 'USD')
# crear_producto('Spaghetti Veganietto', 'pasta', ' Programmers Eat Pasta', '15.49', 'EUR')

# ET.dump(raiz)

###################
# Sección 3.1.1.2
###################

# import csv

# with open('contacts.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         print(row)

###################
# Sección 3.1.1.3
###################

# import csv

# with open('contacts.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         print(','.join(row))

###################
# Sección 3.1.1.4
###################

# import csv

# with open('contacts.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Name'], ':', row['Phone'])

###################
# Sección 3.1.1.5
###################

# import csv

# with open('contacts.csv', newline='') as csvfile:
#     fieldnames = ['Name', 'Phone']
#     reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#     for row in reader:
#         print(row['Name'], row['Phone'])

#################################
# Laboratorio de Sección 3.2.1.1
#################################

# import csv

# class PhoneContact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone


# class Phone:
#     def __init__(self):
#         self.contacts = []

#     def load_contacts_from_csv(self, file):
#         with open(file, newline='') as csvfile:
#             fieldnames = ['Name', 'Phone']
#             reader = csv.DictReader(csvfile, fieldnames)
#             for row in reader:
#                 self.contacts.append(PhoneContact(row['Name'], row['Phone']))

#     def search_contacts(self, phrase):
#         count = 0
#         for contact in self.contacts:
#             if phrase.lower() in contact.name.lower() \
# 			or phrase in contact.phone:
#                 print('{0} ({1})'.format(contact.name, contact.phone))
#                 count += 1
#         if count == 0:
#             print("No contacts found")

# phone = Phone()
# phone.load_contacts_from_csv('contacts.csv')
# phrase = input("Search contacts: ")
# phone.search_contacts(phrase)

###################
# Sección 3.3.1.1
###################

# import csv

# with open('exported_contacts.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
    
#     writer.writerow(['Name', 'Phone'])
#     writer.writerow(['mother', '222-555-101'])
#     writer.writerow(['father', '222-555-102'])
#     writer.writerow(['wife', '222-555-103'])
#     writer.writerow(['mother-in-law', '222-555-104'])

###################
# Sección 3.3.1.2
###################

# import csv

# with open('exported_contacts.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#     writer.writerow(['Name', 'Phone'])
#     writer.writerow(['mother', '222-555-101'])
#     writer.writerow(['father', '222-555-102'])
#     writer.writerow(['wife', '222-555-103'])
#     writer.writerow(['mother-in-law', '222-555-104'])
#     writer.writerow(['grandmother, grandfather', '222-555-105'])

#########################################
## Ejemplo reader y writer con quotechar
#########################################

# import csv

# datos = [
#     ['Nombre', 'Edad'],
#     ['Carlos Pérez', 30],
#     ['Marta López', 25],
#     ['Jorge, Martín', 35]  
# ]

# with open('ejemplo.csv', 'w', newline='') as ficherocsv:
#     escritorcsv = csv.writer(ficherocsv, quotechar='*', quoting=csv.QUOTE_MINIMAL)
#     escritorcsv.writerows(datos)
#     print("Datos escritos en el fichero ejemplo.csv")

# with open('ejemplo.csv', 'r', newline='') as ficherocsv:
#     lectorcsv = csv.reader(ficherocsv, quotechar='*')
#     for row in lectorcsv:
#         print(', '.join(row))

###################
# Sección 3.3.1.3
###################

# import csv

# with open('exported_contacts.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Name', 'Phone']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='*')
    
#     writer.writeheader()
#     writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
#     writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
#     writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
#     writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
#     writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})

#################################
# Laboratorio de Sección 3.4.1.1
#################################

# import csv

# class ExamData:
#     def __init__(self, exam_name):
#         self.exam_name = exam_name
#         self.candidates = []
#         self.number_of_passed_exams = 0
#         self.number_of_failed_exams = 0
#         self.best_score = 0
#         self.worst_score = 100

#     def get_number_of_cadidates(self):
#         return len(set(self.candidates))


# class ExamResultReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = {}

#     def prepare_data(self):
#         with open(self.filename, newline='') as csvfile:
#             fieldnames = ['Exam Name', 'Candidate ID', 'Score', 'Grade']
#             reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#             row_count = 0
#             for row in reader:
#                 row_count += 1
#                 if row_count == 1:
#                     continue
#                 exam_data = self.get_exam_data(row['Exam Name'])
#                 exam_data.candidates.append(row['Candidate ID'])
#                 if row['Grade'] == 'Pass':
#                     exam_data.number_of_passed_exams += 1
#                 else:
#                     exam_data.number_of_failed_exams += 1
#                 exam_data.best_score = max(
#                     exam_data.best_score,
#                     int(row['Score'])
#                 )
#                 exam_data.worst_score = min(
#                     exam_data.worst_score,
#                     int(row['Score'])
#                 )
#         return self.data

#     def get_exam_data(self, exam_name):
#         if exam_name not in self.data:
#             exam_data = ExamData(exam_name)
#             self.data[exam_name] = exam_data
#         return self.data[exam_name]


# class ExamReport:
#     def __init__(self, data):
#         self.data = data

#     def generate(self, filename):
#         with open(filename, 'w', newline='') as csvfile:
#             fieldnames = [
#                 'Exam Name',
#                 'Number of Candidates',
#                 'Number of Passed Exams',
#                 'Number of Failed Exams',
#                 'Best Score',
#                 'Worst Score'
#             ]
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for key, exam_data in self.data.items():
#                 number_of_cadidates = exam_data.get_number_of_cadidates()
#                 writer.writerow({
#                     'Exam Name': exam_data.exam_name,
#                     'Number of Candidates': number_of_cadidates,
#                     'Number of Passed Exams': exam_data.number_of_passed_exams,
#                     'Number of Failed Exams': exam_data.number_of_failed_exams,
#                     'Best Score': exam_data.best_score,
#                     'Worst Score': exam_data.worst_score
#                 })

# exam_result_reader = ExamResultReader('exam_results.csv')
# data = exam_result_reader.prepare_data()
# exam_report = ExamReport(data)
# exam_report.generate('exam_report.csv')

#############################
## jennyfer

# import csv
# from collections import defaultdict

# # Definimos una clase para representar el informe de los exámenes.
# class ExamReport:
#     def __init__(self):
#         # Diccionario para almacenar los datos de los exámenes.
#         self.exam_data = defaultdict(lambda: {"candidates": set(), "scores": []})

#     def load_data(self, filepath):
#         """Carga los datos de los exámenes desde un archivo CSV."""
#         with open(filepath, 'r', encoding='utf-8') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 # Actualizamos el conjunto de candidatos únicos y las puntuaciones para cada examen.
#                 self.exam_data[row["Exam Name"]]["candidates"].add(row["Candidate ID"])
#                 self.exam_data[row["Exam Name"]]["scores"].append(int(row["Score"]))

#     def generate_summary(self):
#         """Genera un resumen de los datos de los exámenes."""
#         report = []
#         for exam, data in self.exam_data.items():
#             passed_exams = sum(score >= 50 for score in data["scores"])
#             failed_exams = sum(score < 50 for score in data["scores"])
#             best_score = max(data["scores"])
#             worst_score = min(data["scores"])
#             report.append({
#                 "Exam Name": exam,
#                 "Number of Candidates": len(data["candidates"]),
#                 "Number of Passed Exams": passed_exams,
#                 "Number of Failed Exams": failed_exams,
#                 "Best Score": best_score,
#                 "Worst Score": worst_score
#             })
#         return report

#     def export_report(self, report_data, filepath):
#         """Exporta el resumen de los exámenes a un archivo CSV."""
#         with open(filepath, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.DictWriter(file, fieldnames=["Exam Name", "Number of Candidates", "Number of Passed Exams", "Number of Failed Exams", "Best Score", "Worst Score"])
#             writer.writeheader()
#             for row in report_data:
#                 writer.writerow(row)
#         print("El informe ha sido exportado a", filepath)

# # Creamos una instancia de ExamReport.
# report = ExamReport()

# # Cargamos los datos desde el archivo CSV. 
# report.load_data('exam_results.csv')

# # Generamos el resumen de los datos.
# summary = report.generate_summary()

# # Exportamos el resumen a un nuevo archivo CSV llamado 'report.csv'.
# report.export_report(summary, 'report.csv')


###################
# Sección 4.1.1.2
###################

# import logging

# logger = logging.getLogger()
# hello_logger = logging.getLogger('hello')
# hello_world_logger = logging.getLogger('hello.world')
# recommended_logger = logging.getLogger(__name__)

###################
# Sección 4.1.1.3
###################

# import logging

# logging.basicConfig()

# logger = logging.getLogger()

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

###################
# Sección 4.1.1.4
###################

# import logging

# logging.basicConfig()

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

###################
# Sección 4.1.1.5
###################

# import logging

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')

# logger = logging.getLogger()

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

###################
# Sección 4.1.1.6
###################

# import logging

# FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

# logger = logging.getLogger()

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')

###################
# Sección 4.1.1.7
###################

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

###################
# Sección 4.1.1.8
###################

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

#################################
# Laboratorio de Sección 4.2.1.1
#################################

# import logging
# import random

# FORMAT = '%(levelname)s - %(message)s'


# class BatterySimulation:
#     def __init__(self, logger):
#         self.logger = logger

#     def simulate_last_hour(self):
#         for minute in range(1, 60 + 1):
#             temperature = random.randint(20, 40)

#             if temperature < 30:
#                 self.logger.debug('{0} C'.format(temperature))
#             elif temperature >= 30 and temperature <= 35:
#                 self.logger.warning('{0} C'.format(temperature))
#             elif temperature > 35:
#                 self.logger.critical('{0} C'.format(temperature))
#             else:
#                 raise Exception('Temperature out of range.')

# logger = logging.getLogger('battery.temperature')
# logger.setLevel(logging.DEBUG)

# handler = logging.FileHandler('battery_temperature.log', mode='w')
# handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter(FORMAT)
# handler.setFormatter(formatter)

# logger.addHandler(handler)

# battery_simulation = BatterySimulation(logger)
# battery_simulation.simulate_last_hour()

###################
# Sección 5.1.1.3
###################

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

# # Uso de método get()
# print('Host:', config.get('mariadb', 'host'))

###################
# Sección 5.1.1.4
###################

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

###################
# Sección 5.1.1.5
###################

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

# # A configuration loaded using the read method can also be modified. 
# # To change a single option, simply set the new value to the appropriate key, 
# # and then save the file using the write method:

# import configparser

# config = configparser.ConfigParser()
# config.read('config.ini')

# config['redis']['db'] = '1'

# with open('config.ini', 'w') as configfile:
#     config.write(configfile)

#################################
# Laboratorio de sección 5.2.1.1
#################################

## Recreación de mess.ini (necesario para el laboratorio en local)

# import configparser

# config = configparser.ConfigParser()
# print(config.read('mess.ini'))

# print('Sections:', config.sections(),'\n')


# for seccion in config.sections():
#     print('[',seccion,']',sep='')
    
#     for entrada in config[seccion]:
#         print(entrada,':',config[seccion][entrada])

#     print()

#############################################

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
