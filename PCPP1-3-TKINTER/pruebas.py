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


##################################################

# import tkinter as tk


# def to_string(x):
#     return "Current counter\nvalue is:\n" + str(x)


# def plus():
#     global counter
#     counter += 1
#     text.set(to_string(counter))


# counter = 0
# window = tk.Tk()
# button = tk.Button(window, text="Go on!", command=plus)
# button.pack()
# text = tk.StringVar()
# label = tk.Label(window, textvariable=text, height=4)
# text.set(to_string(counter))
# label.pack()
# window.mainloop()

########## Menú ########################################

# import tkinter as tk
# from tkinter import messagebox

# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")

# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu)
# # setting the hotkey to "Alt-F"
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_help = tk.Menu(main_menu)
# # setting the hotkey to "Alt-B"
# sub_menu_file.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###############################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# window = tk.Tk()

# # main menu creation
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)

# # 1st main menu item: an empty (as far) submenu
# sub_menu_file = tk.Menu(main_menu)
# main_menu.add_cascade(label="File", menu=sub_menu_file)

# # 2nd main menu item: a simple callback
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app)

# window.mainloop()

#####################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu)
# # setting the hotkey to "Alt-F"
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_help = tk.Menu(main_menu)
# # setting the hotkey to "Alt-B"
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

######################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# # add the QUIT action to the submenu
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

#################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# # we don't want the tear-off here  
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()


# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# # a new submenu item is here!
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

########################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()


# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# # separator is here!
# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

#####################################################

# import tkinter as tk
# from tkinter import messagebox


# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")


# def are_you_sure(event=None):
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()


# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")


# window = tk.Tk()

# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

# for i in range(8):
#     number = str(i + 1)
#     sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
#                           underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.bind_all("<Control-q>", are_you_sure)
# window.mainloop()

##########################################################

# import tkinter as tk


# def on_off():
#     global accessible
#     if accessible == tk.DISABLED:
#         accessible = tk.ACTIVE
#     else:
#         accessible = tk.DISABLED
#     sub_menu.entryconfigure(1, state=accessible)


# accessible = tk.DISABLED
# window = tk.Tk()
# menu = tk.Menu(window)
# window.config(menu=menu)
# sub_menu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Menu", menu=sub_menu)
# sub_menu.add_command(label="On/Off", command=on_off)
# sub_menu.add_command(label="Switch", state=tk.DISABLED)
# window.mainloop()

##################################################

# import tkinter as tk


# def click(*args):
#     global counter
#     if counter > 0:
#         counter -= 1
#     window.title(str(counter))


# counter = 10
# window = tk.Tk()
# window.title(str(counter))
# window.bind("<Button-1>", click)
# window.mainloop()

######################################################

# import tkinter as tk

# window = tk.Tk()
# window.title('Icon?')
# window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
# window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
# window.mainloop()


########################################################

# import tkinter as tk

# window = tk.Tk()

# frame_1 = tk.Frame(window, width=200, height=100, bg='white')
# frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

# button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
# button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
# button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
# button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

# button_1_1.place(x=10, y=10)
# button_1_2.place(x=10, y=50)
# button_2_1.grid(column=0, row=0)
# button_2_2.grid(column=1, row=1)

# frame_1.pack()
# frame_2.pack()

# window.mainloop()

#########################################################

# import tkinter as tk


# def do_it_again():
#     text.set(text.get() + "and again...")


# window = tk.Tk()
# button = tk.Button(window, text="Go ahead!", command=do_it_again)
# button.pack()
# text = tk.StringVar()
# message = tk.Message(window, textvariable=text, width=400)
# text.set("You did it again... ")
# message.pack()
# window.mainloop()

##############################################################

# import tkinter as tk

# window = tk.Tk()
# label_frame_1 = tk.LabelFrame(window, text="Frame #1",
#                               width=200, height=100, bg='white')
# label_frame_2 = tk.LabelFrame(window, text="Frame #2",
#                               labelanchor='se', width=200, height=100, bg='yellow')

# button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
# button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
# button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
# button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

# button_1_1.place(x=10, y=10)
# button_1_2.place(x=10, y=50)
# button_2_1.grid(column=0, row=0)
# button_2_2.grid(column=1, row=1)

# label_frame_1.pack()
# label_frame_2.pack()
# window.mainloop()

############################################################

# import tkinter as tk


# def digits_only(*args):
#     global last_string
#     string = text.get()
#     if string == '' or string.isdigit():  # Field's content is valid.
#         last_string = string
#     else:
#         text.set(last_string)


# last_string = ''
# window = tk.Tk()
# text = tk.StringVar()
# entry = tk.Entry(window, textvariable=text)
# text.set(last_string)
# text.trace('w', digits_only)
# entry.pack()
# entry.focus_set()
# window.mainloop()

#####################################################

# import tkinter as tk


# def click(*args):
#     global size, grows
#     if grows:
#         size += 50
#         if size >= 500:
#             grows = False
#     else:
#         size -= 50
#         if size <= 100:
#             grows = True
#     window.geometry(str(size) + "x" + str(size))


# size = 100
# grows = True
# window = tk.Tk()
# window.geometry("100x100")
# window.bind("<Button-1>", click)
# window.mainloop()

###########################################################

# import tkinter as tk

# window = tk.Tk()
# window.minsize(width=250, height=200)
# window.geometry("500x500")
# window.mainloop()

###################################################################

# import tkinter as tk
# from tkinter import messagebox


# def really():
#     if messagebox.askyesno("?", "Wilt thou be gone?"):
#         window.destroy()


# window = tk.Tk()
# window.protocol("WM_DELETE_WINDOW", really)
# window.mainloop()


###########################################################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askyesno("?", "To be or not to be?")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="Ask the question!", command=question)
# button.pack()
# window.mainloop()

#############################################################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()


###### Canvas ##########################################################

# import tkinter as tk


# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

####################################################################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,
#                    arrow=tk.BOTH, fill='red', smooth=True, width=3)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()


######### Laboratorios #######################################################

# 1 - Rellenar una lista con 25 números aleatorios entre 1 y 1000 (que no se repita ninguno)

# 2 - En un bucle for crear 25 botons (la etiqueta de cada botón se corresponde con cada 
#     número de la lista)

# Posicionar los botones en el grid con ésta fórmula:
# nuevo_boton.grid(column=indice // 5, row=indice % 5)

# 3 - Ahora ordenamos los elementos de la lista de menor a mayor

# 4 - Por cada botón pulsado, comprobar si su etiqueta se corresponde con el elemento de la lista en índice cero, si es así el botçón pasa a state=DISABLED y se elimina ese elemento de la lista

# 5 - Finalmente introducir contador de clicks (variable contador) y temporizador con el método after()

# 6 - Mostrar una ventana emergente con el resultado al acabar el juego


# import tkinter as tk
# from random import randint


# def tick():
#     global clock_val, after_id
#     if clock_started:
#         clock_val += 1
#         clock_lab["text"] = str(clock_val)
#         after_id = clock_lab.after(1000, tick)


# def button_clicked(event):
#     global clock_started
#     if not clock_started:
#         clock_started = True
#         clock_lab.after(1000, tick)
#     clicked_btn = event.widget
#     clicked_val = int(clicked_btn["text"])
#     if clicked_val == numbers[0]:
#         clicked_btn["state"] = tk.DISABLED
#         del numbers[0]
#     if len(numbers) == 0:
#         clock_started = False
#         clock_lab.after_cancel(after_id)


# window = tk.Tk()
# window.title("Clicker")
# numbers = []
# for i in range(25):
#     new_num = randint(1, 999)
#     while new_num in numbers:
#         new_num = randint(1, 999)
#     numbers.append(new_num)

# for i in range(25):
#     new_bt = tk.Button(window, text=str(numbers[i]), width=10)
#     new_bt.grid(column=i // 5, row=i % 5)
#     new_bt.bind("<Button-1>", button_clicked)

# numbers.sort()
# clock_val = 0
# clock_lab = tk.Label(window, text=str(clock_val))
# clock_lab.grid(column=2, row=5)
# clock_started = False
# window.mainloop()

##################

# from tkinter import *
# import random


# def newxy(xy):
#     nw = random.randint(1, 440)
#     while abs(xy - nw) < 50:
#         nw = random.randint(1, 440)
#     return nw


# def domove(ev):
#     global x, y
#     x = newxy(x)
#     y = newxy(y)
#     bt.place(x=x, y=y)

# wn = Tk()
# wn.geometry("500x500")
# wn.title("Catch me!")
# bt = Button(wn, text="Catch me!")
# bt.bind("<enter>", domove)
# x = y = 10
# bt.place(x=x, y=y)
# random.seed()
# wn.mainloop()

#######################

# from tkinter import *
# from tkinter import messagebox


# def get_number(en):
#     s = en.get()
#     try:
#         v = float(s)
#     except ValueError:
#         return None
#     return v


# def doeval():
#     v1 = get_number(e1)
#     if v1 is None:
#         messagebox.showerror("Error", "Invalid argument in the first field")
#         e1.focus_set()
#         return
#     v2 = get_number(e2)
#     if v2 is None:
#         messagebox.showerror("Error", "Invalid argument in the second field")
#         e2.focus_set()
#         return
#     o = op.get()
#     if o == 3 and v2 == 0:
#         messagebox.showerror("Error", "Cannot divide by zero")
#         e2.focus_set()
#         return
#     if o == 0:
#         r = v1 + v2
#     elif o == 1:
#         r = v1 - v2
#     elif o == 2:
#         r = v1 * v2
#     else:
#         r = v1 / v2
#     messagebox.showinfo("Result", str(r))

# wnd = Tk()
# wnd.title("Calculator")
# e1 = Entry(wnd)
# op = IntVar()
# opa = Radiobutton(wnd, text="+", var=op, val=0)
# ops = Radiobutton(wnd, text="-", var=op, val=1)
# opm = Radiobutton(wnd, text="*", var=op, val=2)
# opd = Radiobutton(wnd, text="/", var=op, val=3)
# e2 = Entry(wnd)
# bt = Button(wnd, text="Evaluate", command=doeval)
# e1.grid(row=0, rowspan=4, column=0)
# e1.focus_set()
# opa.grid(row=0, column=1)
# ops.grid(row=1, column=1)
# opm.grid(row=2, column=1)
# opd.grid(row=3, column=1)
# e2.grid(row=0, rowspan=4, column=2)
# bt.grid(row=4, columnspan=3)
# wnd.mainloop()

################

# from tkinter import Tk, Button, Canvas


# phases = ((True, False, False),
#           (True, True, False),
#           (False, False, True),
#           (False, True, False))

# def draw_light(y,color):
#     canvas.create_oval(15,y+5,105,y+95,outline='black',fill=color,width=3)


# def red_light(on):
#     draw_light(0, 'red' if on else 'gray')


# def yellow_light(on):
#     draw_light(100, 'yellow' if on else 'gray')


# def green_light(on):
#     draw_light(200, 'green' if on else 'gray')


# def next_phase():
#     global phase
#     phase = (phase + 1) % len(phases)
#     red_light(phases[phase][0])
#     yellow_light(phases[phase][1])
#     green_light(phases[phase][2])


# window = Tk()
# window.title("Traffic Lights")
# canvas = Canvas(window, width=120, height=300, bg='#555555')
# canvas.grid(row=0, column=0)
# next_btn = Button(window, text="Next", command=next_phase)
# next_btn.grid(row=1,column=0)
# quit_btn = Button(window, text="Quit", command=window.destroy)
# quit_btn.grid(row=2,column=0)
# phase = -1
# next_phase()
# window.mainloop()

############ Tic Tac Toe #############

# import tkinter as tk
# from tkinter import messagebox
# from random import randrange


# wnd = tk.Tk()
# wnd.title("TicTacToe")


# def set_ox(btn, sign):
#     btn["fg"] = btn["activeforeground"] = "red" if sign == 'X' else "green"
#     btn["text"] = sign


# def winner():
#     for sign in ("X", "O"):
#         for x in range(3):
#             if sign == board[x][0]["text"] == board[x][1]["text"] == board[x][2]["text"]:
#                 return sign
#             if sign == board[0][x]["text"] == board[1][x]["text"] == board[2][x]["text"]:
#                 return sign
#         if sign == board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]:
#             return sign
#         if sign == board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]:
#             return sign
#     return None


# def free_cells():
#     list = []
#     for row in range(3):
#         for col in range(3):
#             if board[row][col]["text"] == "":
#                 list.append( (row, col) )
#     return list


# def announce(win):
#     messagebox.showinfo("Game Over!", ("I" if win == "X" else "You") + " won!")
#     wnd.destroy()
#     exit(0)

# def clicked(event):
#     btn = event.widget
#     if btn["text"] != "":
#         return
#     set_ox(btn, "O")
#     if not winner() is None:
#         announce("O")
#     free = free_cells()
#     this = free[randrange(0, len(free))]
#     set_ox(board[this[0]][this[1]], "X")
#     if not winner() is None:
#         announce("X")


# board = [[None for c in range(3)] for r in range(3)]
# for col in range(3):
#     for row in range(3):
#         btn = tk.Button(wnd, width=4, height=1, font=("Arial", 30, "bold"), text="")
#         btn.bind("<Button-1>", clicked)
#         btn.grid(column=col, row=row)
#         board[row][col] = btn
# set_ox(board[1][1], "X")
# wnd.mainloop()

####### Calculadora ##############################

# import tkinter as tk

# ERROR = "Error!"

# def string_to_double(s):
#     try:
#         val = float(s);
#         return val;
#     except ValueError:
#         return None

# def clear_if_error():
#     s = display_str.get()
#     if s == ERROR:
#         display_str.set("0")

# def double_to_string(v):
#     s = str(v)
#     if 'e' in s:
#         return ERROR
#     if '.' in s:
#         while s[-1] == '0':
#             s = s[0:-1]
#     while len(s) > 10 and s[-1] != '.':
#         s = s[0:-1]
#     if s[-1] == '.':
#         s = s[0:-1]
#     if len(s) > 10:
#         return ERROR
#     return s

# def do_clear():
#     global accumulator, last_operation
#     display_str.set("0")
#     accumulator = 0.
#     last_operation = ""


# def do_digit_0():
#     clear_if_error()
#     s = display_str.get()
#     if len(s) < 10 and s != "0":
#         display_str.set(s + '0')


# def do_digit_x(dig):
#     clear_if_error()
#     s = display_str.get()
#     if len(s) < 10:
#         if s == "0":
#             display_str.set(dig)
#         else:
#             display_str.set(s + dig)


# def do_dot():
#     clear_if_error()
#     s = display_str.get()
#     if len(s) < 10 and "." not in s:
#         display_str.set(s + ".")


# def do_plus():
#     global last_operation, accumulator
#     clear_if_error()
#     last_operation = "+"
#     accumulator = string_to_double(display_str.get())
#     display_str.set("0")


# def do_minus():
#     global last_operation, accumulator
#     clear_if_error()
#     last_operation = "-"
#     accumulator = string_to_double(display_str.get())
#     display_str.set("0")


# def do_mult():
#     global last_operation, accumulator
#     clear_if_error()
#     last_operation = "*"
#     accumulator = string_to_double(display_str.get())
#     display_str.set("0")


# def do_divd():
#     global last_operation, accumulator
#     clear_if_error()
#     last_operation = "/"
#     accumulator = string_to_double(display_str.get())
#     display_str.set("0")


# def do_equal():
#     global last_operation, accumulator
#     clear_if_error()
#     value = string_to_double(display_str.get())
#     if last_operation == "+":
#         accumulator += value
#     elif last_operation == "-":
#         accumulator -= value
#     elif last_operation == "*":
#         accumulator *= value
#     elif last_operation == "/":
#         if value != 0:
#             accumulator /= value
#         else:
#             display_str.set(ERROR);
#             return;
#     display_str.set(double_to_string(accumulator))


# def do_plusminus():
#     clear_if_error()
#     display_str.set(double_to_string(-string_to_double(display_str.get())))


# window = tk.Tk()
# window.title('Calc')
# display_str = tk.StringVar()
# display_str.set("0")
# stick = tk.N + tk.S + tk.E + tk.W
# display = tk.Entry(window, width=10, font=("Courier New", "15", "bold"), textvariable=display_str, justify=tk.RIGHT)
# display.grid(row=0, columnspan=5, sticky=stick)
# digit7 = tk.Button(window, text="7", command=lambda: do_digit_x("7"))
# digit7.grid(row=1, column=0, sticky=stick)
# digit8 = tk.Button(window, text="8", command=lambda: do_digit_x("8"))
# digit8.grid(row=1, column=1, sticky=stick)
# digit9 = tk.Button(window, text="9", command=lambda: do_digit_x("9"))
# digit9.grid(row=1, column=2, sticky=stick)
# plus = tk.Button(window, text="+", command=do_plus)
# plus.grid(row=1, column=4, sticky=stick)
# digit4 = tk.Button(window, text="4", command=lambda: do_digit_x("4"))
# digit4.grid(row=2, column=0, sticky=stick)
# digit5 = tk.Button(window, text="5", command=lambda: do_digit_x("5"))
# digit5.grid(row=2, column=1, sticky=stick)
# digit6 = tk.Button(window, text="6", command=lambda: do_digit_x("6"))
# digit6.grid(row=2, column=2, sticky=stick)
# minus = tk.Button(window, text="-", command=do_minus)
# minus.grid(row=2, column=4, sticky=stick)
# digit1 = tk.Button(window, text="1", command=lambda: do_digit_x("1"))
# digit1.grid(row=3, column=0, sticky=stick)
# digit2 = tk.Button(window, text="2", command=lambda: do_digit_x("2"))
# digit2.grid(row=3, column=1, sticky=stick)
# digit3 = tk.Button(window, text="3", command=lambda: do_digit_x("3"))
# digit3.grid(row=3, column=2, sticky=stick)
# equal = tk.Button(window, text=" = ", command=do_equal)
# equal.grid(row=3, column=3, sticky=stick)
# mult = tk.Button(window, text="*", command=do_mult)
# mult.grid(row=3, column=4, sticky=stick)
# digit0 = tk.Button(window, text="0", command=do_digit_0)
# digit0.grid(row=4, column=0, sticky=stick)
# dot = tk.Button(window, text=" . ", command=do_dot)
# dot.grid(row=4, column=2, sticky=stick)
# clear = tk.Button(window, text="C", command=do_clear)
# clear.grid(row=4, column=1, sticky=stick)
# plusminus = tk.Button(window, text="+/-", command=do_plusminus)
# plusminus.grid(row=4, column=3, sticky=stick)
# divd = tk.Button(window, text="/", command=do_divd)
# divd.grid(row=4, column=4, sticky=stick)
# accumulator = 0.
# last_operation = ""
# window.mainloop()


###### Mostrar icono ####################
# import tkinter as tk

# window = tk.Tk()
# window.title('Icon?')
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
# window.bind("<Button-1>", lambda e: window.destroy())
# window.mainloop()


######## Cargar imágenes jpg #############################################
# pip3 install Pillow

# import tkinter as tk

# from PIL import Image, ImageTk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='red')
# jpg = Image.open('logo.jpg')
# image = ImageTk.PhotoImage(jpg)
# canvas.create_image(200, 200, image=image)  
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

######################################################

