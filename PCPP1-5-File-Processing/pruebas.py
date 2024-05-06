### Trabajo con Base de Datos

# Select para recuperar datos

# Data Manipulation Language (DML) 
# insert, update, delete

# Data Definition Language (DDl)
# create, alter, drop, rename, truncate, comment

# Data Control Language
# grant, revoke


# SQLite

# import sqlite3

# conn = sqlite3.connect('hello.db') # Crea un archivo sqlite en disco

# conn = sqlite3.connect(':memory:') # Crea una base de datos sqlite en memoria

### Laboratorio: TO-DO

# import sqlite3

# conn = sqlite3.connect('todo.db') # Creo el archivo sqlite

# c = conn.cursor() # Objeto para gestionar las sentencias a SQLite

# Creo la tabla 'tasks'
# c.execute('''CREATE TABLE tasks (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     priority INTEGER NOT NULL
# );''')

# # INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);

# # Usar (?,?) evita que el código sea vulnerable por inyección por código.

# c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))

# conn.commit() # valido las transiciones vigentes

# conn.close() # cierro la conexión

### Laboratorio tasks

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


### Laboratorio final

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
#         name = input('Nombre de la tarea: ')
#         priority = int(input('Prioridad: '))
        
#         self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
#         self.conn.commit()

# app = Todo()
# app.add_task()

### Laboratorio: Lectura de la base de datos

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# for row in c.execute('SELECT * FROM tasks'):
#     print(row)
# conn.close()

### Lectura cargando todos los registros con fetchall() (Consume más memoria)

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# rows = c.fetchall() # Recupera todos los registros
# for row in rows:
#     print(row)
# conn.close()

### Lectura cargando una por una con fetchone()

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)

# conn.close()

###### Laboratorio Completo

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
#         name = input('Nombre de la Tarea: ')
#         priority = int(input('Prioridad: '))

#         if len(name) == 0 or priority < 1:
#             return

#         if self.find_task(name) is not None:
#             return

#         self.c.execute(
#             'INSERT INTO tasks (name, priority) VALUES (?,?)',
#             (name, priority))
#         self.conn.commit()

#     def find_task(self, name):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             if row[1] == name:
#                 return row

#         return None

#     def show_tasks(self):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             print(row)

# app = Todo()
# app.add_task()
# app.show_tasks()


##### Versión del laboratorio más eficiente

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
#             print("No puedes crear una tarea con el mismo nombre de una ya existente")
#             return

#         self.c.execute(
#             'INSERT INTO tasks (name, priority) VALUES (?,?)',
#             (name, priority))
#         self.conn.commit()
#     def find_task(self, name):
#         self.c.execute('SELECT count(*) FROM tasks WHERE name = ?', (name,))
#         recuento = self.c.fetchone()[0]

#         if recuento:
#             print('Ya existe una tarea con ese nombre')
#             return True

#         return None

#     def show_tasks(self):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             print(row)

# app = Todo()
# app.add_task()
# app.show_tasks()

# ######### Actualizar Datos ########

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
# conn.commit()
# conn.close()


########## Borrar Datos ######################

# import sqlite3

# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('DELETE FROM tasks WHERE id = ?', (1,))
# conn.commit()
# conn.close()

######### Laboratorio comlpementario de TO-DO ###########

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
#         self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,))
#         return self.c.fetchone()

#     def show_tasks(self):
#         for row in self.c.execute('SELECT * FROM tasks'):
#             print(row)

#     def change_priority(self):
#         task_id = int(input('Enter task id: '))
#         new_priority = int(input('Enter new priority: '))

#         if new_priority < 1:
#             return

#         self.c.execute(
#             'UPDATE tasks SET priority = ? WHERE id = ?',
#             (new_priority, task_id))
#         self.conn.commit()

#     def delete_task(self):
#         task_id = int(input('Enter task id: '))

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

############# 



