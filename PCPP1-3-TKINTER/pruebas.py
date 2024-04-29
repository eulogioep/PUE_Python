# import tkinter
# from tkinter import messagebox


# def Click():
#     replay = messagebox.askquestion("¿Cerrar?", "¿Estás seguro?")
#     if replay == 'yes':
#         ventana.destroy()


# ventana = tkinter.Tk()
# ventana.title("Título de la Ventana")
# button = tkinter.Button(ventana, text="¡Adiós!", command=Click)
# button.place(x=10, y=10)
# ventana.mainloop()


##################################################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.place(x=10, y=10)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70)
# window.mainloop()


##### Posición de los componentes ##################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.place(x=10, y=10, width=150)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70, height=50)
# window.mainloop()


# ######################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=2)
# window.mainloop()


# #####################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=0, columnspan=2)
# window.mainloop()


# ######################

# import tkinter as tk


# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack()
# button_2.pack()
# button_3.pack()
# window.mainloop()


# #########################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT)
# button_2.pack()
# button_3.pack()
# window.mainloop()


# #########################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT, fill=tk.Y)
# button_2.pack()
# button_3.pack()
# window.mainloop()


# ### Añadir Color #######################

# import tkinter as tk

# window = tk.Tk()
# button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
# button.pack()
# window.mainloop()

##########################

# import tkinter as tk


# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="MediumPurple",
#                    fg="LightSalmon",
#                    activeforeground="LavenderBlush",
#                    activebackground="HotPink")
# button.pack()
# window.mainloop()

###########################

# import tkinter as tk

# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="#9370DB",
#                    fg="#FFA07A",
#                    activeforeground="#FFF0F5",
#                    activebackground="#FF69B4")
# button.pack()
# window.mainloop()


################################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(window, text ="Button")
# button.pack(fill=tk.X)

# switch = tk.IntVar()
# switch.set(1)

# checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
# checkbutton.pack()

# entry = tk.Entry(window, width=30)
# entry.pack()

# radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
# radiobutton_1.pack()
# radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
# radiobutton_2.pack()

# window.mainloop()

############################################

# import platform
# import tkinter as tk


# if platform.system() == 'Darwin':
#     from tkmacosx import Button
# else:
#     from tkinter import Button


# window = tk.Tk()
# button_1 = Button(window, text="Button #1")
# button_2 = Button(window, text="Button #2")
# button_3 = Button(window, text="Button #3")
# button_1.pack(side ='right', fill = 'y')
# button_2.pack(fill = 'x')
# button_3.pack(fill = 'y')
# window.mainloop()

############################

# import platform
# import tkinter as tk

# if platform.system() == 'Darwin':
#     from tkmacosx import Button
# else:
#     from tkinter import Button

# window = tk.Tk()
# button_1 = Button(window, text="Norte")
# button_2 = Button(window, text="Este")
# button_3 = Button(window, text="Oeste")
# button_4 = Button(window, text="Sur")
# button_5 = Button(window, text="central")

# button_1.pack(side ='top', fill = 'x')
# button_4.pack(side ='bottom', fill = 'x')
# button_2.pack(side = 'left', fill = 'y')
# button_3.pack(side ='right', fill = 'y')

# button_5.pack(expand = True, fill = 'both')


# window.mainloop()

#########################################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(window, text="Button")
# button.pack(fill=tk.X)

# window.mainloop()


#############################################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(window, text="Button")
# button.pack(fill=tk.X)

# switch = tk.IntVar()
# switch.set(1)

# window.mainloop()

##############################################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(window, text ="Button")
# button.pack(fill=tk.X)

# switch = tk.IntVar()
# switch.set(1)

# checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
# checkbutton.pack()

# entry = tk.Entry(window, width=30)
# entry.pack()

# radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
# radiobutton_1.pack()
# radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
# radiobutton_2.pack()

# window.mainloop()

####### Mensajes informativos #######################################################

# import tkinter
# from tkinter import messagebox


# def clicked():
#     messagebox.showinfo("info", "some\ninfo")


# window = tkinter.Tk()
# button_1 = tkinter.Button(window, text="Show info", command=clicked)
# button_1.pack()
# button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
# button_2.pack()
# window.mainloop()

####### Propiedad command para widgets clicables ##########################################

# import tkinter as tk
# from tkinter import messagebox


# def click():
#     tk.messagebox.showinfo("Click!","I love clicks!")


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.pack()

# window.mainloop()

######################################################################

# import tkinter as tk
# from tkinter import messagebox


# def click(event=None):
#     tk.messagebox.showinfo("Click!", "I love clicks!")


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)   # Line I
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)   # Line II
# frame.pack()

# window.mainloop()

######### Eventos ######################################

# import tkinter as tk
# from tkinter import messagebox


# def click(event=None):
#     if event is None:
#         tk.messagebox.showinfo("Click!", "I love clicks!")
#     else:
#         string = "Widget: " + event.widget.winfo_name()[1:] + ",x=" + str(event.x) + ",y=" + str(event.y) + \
#                  ",num=" + str(event.num) + ",type=" + event.type
#         tk.messagebox.showinfo("Click!", string)        


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)
# frame.pack()

# window.mainloop()

############################################################

# import tkinter as tk
# from tkinter import messagebox


# def on_off():
#     global switch
#     if switch:
#         button_2.config(command=lambda: None)
#         button_2.config(text="Gee!")
#     else:
#         button_2.config(command=peekaboo)
#         button_2.config(text="Peekaboo!")
#     switch = not switch


# def peekaboo():
#     messagebox.showinfo("", "PEEKABOO!")


# def do_nothing():
#     pass


# switch = True
# window = tk.Tk()
# buton_1 = tk.Button(window, text="On/Off", command=on_off)
# buton_1.pack()
# button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
# button_2.pack()
# window.mainloop()

##############

# import tkinter as tk
# from tkinter import messagebox


# def on_off():
#     global switch
#     if switch:
#         button_2.config(command=lambda: None)
#         button_2.config(text="Ahora no puedes mostrar la ventana emergente", state="disabled")
#         buton_1.config(text="Activar el botón inferior")
#     else:
#         button_2.config(command=lambda: messagebox.showinfo("", "Esta ventana emergente se muestra solo cuando el botón está activado!"))
#         button_2.config(text="Púlsame para mostrar la ventana emergente", state="normal")

#         buton_1.config(text="Desactivar el botón inferior")

#     switch = not switch

# switch = True
# window = tk.Tk()
# window.geometry('300x200')
# buton_1 = tk.Button(window, text="Desactivar botón inferior", command=on_off)
# buton_1.pack()
# button_2 = tk.Button(window, text="Púlsame para mostrar la ventana emergente", command=lambda: messagebox.showinfo("", "Esta ventana emergente se muestra solo cuando el botón está activado!"))
# button_2.pack()
# window.mainloop()


################################

# import tkinter as tk

# def on_off():
#     global switch
#     if switch:
#         label.unbind("<Button-1>")
#         label.config(state="disabled")
#         button.config(text="Activar evento en el frame")
#     else:
#         label.bind("<Button-1>", rhyme)
#         label.config(state="active")
#         button.config(text="Desactivar evento en el frame")

#     switch = not switch


# def rhyme(dummy):
#     global word_no, words
#     word_no += 1
#     label.config(text=words[word_no % len(words)])


# switch = True
# words = ["Old", "McDonald", "Had", "A", "Farm"]
# word_no = 0
# window = tk.Tk()
# button = tk.Button(window, width = 30, text="Desactivar evento en el frame", command=on_off)
# button.pack()
# label = tk.Label(window, text=words[0])
# label.bind("<Button-1>", rhyme)
# label.pack()
# window.mainloop()


##################################################

# import tkinter as tk
# from tkinter import messagebox


# def hello(dummy):
#     messagebox.showinfo("", "Hello!")


# window = tk.Tk()
# button = tk.Button(window, text="On/Off")
# button.pack()
# label = tk.Label(window, text="Label")
# label.pack()
# frame = tk.Frame(window, bg="yellow", width=100, height=20)
# frame.pack()
# window.bind_all("<Button-1>", hello) # Todos los componentes de la ventana respoden al evento
# window.mainloop()

##############################################

# import tkinter as tk


# def on_off():
#     global button
#     state = button["text"]
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     button["text"] = state


# window = tk.Tk()
# button = tk.Button(window, text="OFF", command=on_off)
# button.place(x=50, y=100, width=100)
# window.mainloop()

############################################

# import tkinter as tk


# def on_off():
#     global button
#     state = button.cget("text")
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     button.config(text=state)


# window = tk.Tk()
# button = tk.Button(window, text="OFF", command=on_off)
# button.place(x=50, y=100, width=100)
# window.mainloop()

############ Modificacion Labels #########################################

# import tkinter as tk


# window = tk.Tk()
# label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
# label_1.grid(column=0, row=0)
# label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
# label_3.grid(column=0, row=2)
# window.mainloop()

############ Modificación Botones ################################################

# import tkinter as tk


# window = tk.Tk()
# button_1 = tk.Button(window, text="Ordinary button")
# button_1.pack()
# button_2 = tk.Button(window, text="Exceptional button")
# button_2.pack()
# button_2["borderwidth"] = 10
# button_2["highlightthickness"] = 10
# button_2["padx"] = 10
# button_2["pady"] = 5
# button_2["underline"] = 1
# window.mainloop()

###############################################################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Ordinary button");
# button_1.pack()
# button_2 = tk.Button(window, text="Colorful button")
# button_2.pack()
# button_2.config(bg ="#000000")
# button_2.config(fg ="yellow")
# button_2.config(activeforeground ="#FF0000")
# button_2.config(activebackground ="green")
# window.mainloop()

#################################################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Regular button");
# button_1["anchor"] = tk.E
# button_1["width"] = 20  # pixels!
# button_1.pack()
# button_2 = tk.Button(window, text="Another button")
# button_2["anchor"] = tk.SW
# button_2["width"] = 20
# button_2["height"] = 3  # rows
# button_2.pack()
# window.mainloop()

########################################################

# import tkinter as tk


# def blink():
#     global is_white
#     if is_white:
#         color = 'black'
#     else:
#         color = 'white'
#     is_white = not is_white
#     frame.config(bg=color)
#     frame.after(500, blink)


# is_white = True
# window = tk.Tk()
# frame = tk.Frame(window, width=200, height=100, bg='white')
# frame.after(500, blink)
# frame.pack()
# window.mainloop()

################ Cursores ######################################

# https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm

# import tkinter as tk

# window = tk.Tk()
# label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
# label_1.pack()
# label_2 = tk.Label(window, height=3, text="watch", cursor="watch")
# label_2.pack()
# label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
# label_3.pack()
# window.mainloop()

####################################################################

# import tkinter as tk

# def blink():
#     global indice
#     indice += 1

#     color = '#' + colores[indice % len(colores)] * 2 + '0000'

#     frame.config(bg=color)
#     frame.after(200, blink)

# colores = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# indice = 0

# window = tk.Tk()
# frame = tk.Frame(window, width=100, height=100, bg='#'+ colores[indice] * 2 + '0000')
# frame.after(100, blink)
# frame.pack()
# window.mainloop()

########################################################################

# import tkinter as tk


# def r_observer(*args):
#     print("Reading")


# def w_observer(*args):
#     print("Writing")


# dummy = tk.Tk()    # we need this although we won't display any windows
# variable = tk.StringVar()
# variable.set("abc")
# r_obsid = variable.trace("r", r_observer)
# w_obsid = variable.trace("w", w_observer)
# variable.set(variable.get() + 'd')  # read followed by write
# variable.trace_vdelete("r", r_obsid)
# variable.set(variable.get() + 'e')
# variable.trace_vdelete("w", w_obsid)
# variable.set(variable.get() + 'f')
# print(variable.get())

###############################################################

# import tkinter as tk


# def switch():
#     if button_1.cget('state') == tk.DISABLED:
#         button_1.config(state=tk.NORMAL)
#         button_1.flash()
#     else:
#         button_1.flash()
#         button_1.config(state=tk.DISABLED)


# def mouseover(ev):
#     button_1['bg'] = 'green'


# def mouseout(ev):
#     button_1['bg'] = 'red'


# window = tk.Tk()
# button_1 = tk.Button(window, text="Enabled", bg="red")
# button_1.bind("<Enter>", mouseover)
# button_1.bind("<Leave>", mouseout)
# button_1.pack()
# button_2 = tk.Button(window, text="Enable/Disable", command=switch)
# button_2.pack()
# window.mainloop()


#####################################################

# import tkinter as tk
# from tkinter import messagebox


# def count():
#     global counter
#     counter += 1

# def show():
#     messagebox.showinfo("","counter=" + str(counter) + ",state=" + str(switch.get()))


# window = tk.Tk()
# switch = tk.IntVar()
# counter = 0
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
# checkbutton.pack()
# window.mainloop()


################################################

# import tkinter as tk
# from tkinter import messagebox


# def show():
#     messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
#                         ",radio_2=" + str(radio_2_var.get()))


# def command_1():
#     radio_2_var.set(radio_1_var.get())


# def command_2():
#     radio_1_var.set(radio_2_var.get())


# window = tk.Tk()
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# radio_1_var = tk.IntVar()
# radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
# radio_1_1.select()
# radio_1_1.pack()
# radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
# radio_1_2.pack()
# radio_2_var = tk.IntVar()
# radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
# radio_2_1.pack()
# radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
# radio_2_2.select()
# radio_2_2.pack()
# window.mainloop()


#####################################################








