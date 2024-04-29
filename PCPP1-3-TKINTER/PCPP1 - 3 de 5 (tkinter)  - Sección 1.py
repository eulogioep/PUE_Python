###################
# Sección 1.2.1.2
###################

# import tkinter

# skylight = tkinter.Tk()
# skylight.mainloop()

###################
# Sección 1.2.1.3
###################

# import tkinter

# skylight = tkinter.Tk()
# skylight.title("Skylight")
# skylight.mainloop()

###################
# Sección 1.2.1.4
###################

# import tkinter

# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!")
# button.place(x=10, y=10)
# skylight.mainloop()

###################
# Sección 1.2.1.5
###################

# import tkinter

# def Click():
#     skylight.destroy();
    
# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!", command=Click)
# button.place(x=10, y=10)
# skylight.mainloop()

###################
# Sección 1.2.1.6
###################

# import tkinter
# from tkinter import messagebox

# def Click():
#     replay = messagebox.askquestion("Quit?", "Are you sure?")
#     if replay == 'yes':
#         skylight.destroy();


# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!", command=Click)
# button.place(x=10, y=10)
# skylight.mainloop()

###################
# Sección 1.3.1.2
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.place(x=10, y=10)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70)
# window.mainloop()

###################
# Sección 1.3.1.3
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.place(x=10, y=10, width=150)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70, height=50)
# window.mainloop()

###################
# Sección 1.3.1.4
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=2)
# window.mainloop()

###################
# Sección 1.3.1.5
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=0, columnspan=2)
# window.mainloop()

###################
# Sección 1.3.1.6
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack()
# button_2.pack()
# button_3.pack()
# window.mainloop()

###################
# Sección 1.3.1.7
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT)
# button_2.pack()
# button_3.pack()
# window.mainloop()

###################
# Sección 1.3.1.8
###################

# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT, fill=tk.Y)
# button_2.pack()
# button_3.pack()
# window.mainloop()

###################
# Sección 1.4.1.2
###################

# import tkinter as tk

# window = tk.Tk()
# button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
# button.pack()
# window.mainloop()

#########################################
## Cambios para color de fondo en  MacOS
#########################################

# import tkinter as tk
# from tkmacosx import Button

# window = tk.Tk()
# button = Button(window, text="Button #1", bg="red", fg="yellow")
# button.pack()
# window.mainloop()

###################
# Sección 1.4.1.3
###################

# import tkinter as tk


# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="MediumPurple",
#                    fg="LightSalmon",
#                    activeforeground="LavenderBlush",
#                    activebackground="HotPink")
# button.pack()
# window.mainloop()

#########################################
## Cambios para color de fondo en  MacOS
#########################################

# import tkinter as tk
# from tkmacosx import Button

# window = tk.Tk()
# button = Button(window, text="Button #1",
#                    bg="MediumPurple",
#                    fg="LightSalmon",
#                    activeforeground="LavenderBlush",
#                    activebackground="HotPink")
# button.pack()
# window.mainloop()

###################
# Sección 1.4.1.6
###################

# import tkinter as tk

# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="#9370DB",
#                    fg="#FFA07A",
#                    activeforeground="#FFF0F5",
#                    activebackground="#FF69B4")
# button.pack()
# window.mainloop()

#########################################
## Cambios para color de fondo en  MacOS
#########################################

# import tkinter as tk
# from tkmacosx import Button

# window = tk.Tk()

# lista = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

# for valor in lista:

#     button = Button(window, text="Button #1",
#                        bg="#" + str(valor) + str(valor) + "0000",
#                        fg="#000000",
#                        activeforeground="#FFF0F5",
#                        activebackground="#FF69B4")
#     button.pack()

# window.mainloop()

###################
# Sección 1.5.1.1
###################

# import tkinter as tk

# window = tk.Tk()
# window.mainloop()

###################
# Sección 1.5.1.2
###################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text = "Little label:")
# label.pack()

# window.mainloop()

###################
# Sección 1.5.1.3
###################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# window.mainloop()

###################
# Sección 1.5.1.4
###################

# import tkinter as tk

# window = tk.Tk()

# label = tk.Label(window, text="Little label:")
# label.pack()

# frame = tk.Frame(window, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(window, text="Button")
# button.pack(fill=tk.X)

# window.mainloop()

###################
# Sección 1.5.1.5
###################

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

###################
# Sección 1.5.1.6
###################

# import tkinter as tk

# win = tk.Tk()

# label = tk.Label(win, text="Little label:")
# label.pack()

# frame = tk.Frame(win, height=30, width=100, bg="#000099")
# frame.pack()

# button = tk.Button(win, text="Button")
# button.pack(fill=tk.X)

# switch = tk.IntVar()
# switch.set(1)

# checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
# checkbutton.pack()

# win.mainloop()

###################
# Sección 1.5.1.7
###################

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

# checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
# checkbutton.pack()

# entry = tk.Entry(window, width=30)
# entry.pack()


# window.mainloop()

###################
# Sección 1.5.1.8
###################

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

###################
# Sección 1.6.1.2
###################

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

###################
# Sección 1.6.1.3
###################

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
# frame.pack();

# window.mainloop()

###################
# Sección 1.6.1.6
###################

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

###################
# Sección 1.6.1.8
###################

# import tkinter as tk
# from tkinter import messagebox


# def click(event=None):
#     if event is None:
#         tk.messagebox.showinfo("Click!", "I love clicks!")
#     else:
#         string = "x=" + str(event.x) + ",y=" + str(event.y) + \
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

###################
# Sección 1.6.1.9
###################

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

###################
# Sección 1.6.1.10
###################

# import tkinter as tk

# def on_off():
#     global switch
#     if switch:
#         label.unbind("<Button-1>")
#     else:
#         label.bind("<Button-1>", rhyme)
#     switch = not switch


# def rhyme(dummy):
#     global word_no, words
#     word_no += 1
#     label.config(text=words[word_no % len(words)])


# switch = True
# words = ["Old", "McDonald", "Had", "A", "Farm"]
# word_no = 0
# window = tk.Tk()
# window.geometry('300x200')
# button = tk.Button(window, text="On/Off", command=on_off)
# button.pack()
# label = tk.Label(window, text=words[0])
# label.bind("<Button-1>", rhyme)
# label.pack()
# window.mainloop()

###################
# Sección 1.6.1.11
###################

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
# window.bind_all("<Button-1>", hello)
# window.mainloop()

###################
# Sección 1.7.1.2
###################

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

##############################
## Cambio de color dinámico
##############################

# import tkinter as tk

# def click():

#     global indice
#     indice += 1

#     color_actual = '#'+ lista_hexa[indice % len(lista_hexa)]* 2  + '0000'
    
#     frame['bg'] = color_actual
#     etiqueta['text'] =  "Color actual: #" + color_actual

# lista_hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# indice = 0


# window = tk.Tk()
# window.geometry('300x200')
# etiqueta = tk.Label(window, text='Color actual: #' +'000000')
# frame = tk.Frame(window, width=200, height=100, bg='#000000', borderwidth=2, relief=tk.FLAT)
# boton = tk.Button(window, text="Cambiar color", command=click)
# etiqueta.pack()
# frame.pack()
# boton.pack()
# window.mainloop()

###################
# Sección 1.7.1.3
###################

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

###################
# Sección 1.7.1.4
###################

# import tkinter as tk

# window = tk.Tk()
# label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
# label_1.grid(column=0, row=0)
# label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
# label_3.grid(column=0, row=2)
# window.mainloop()

###################
# Sección 1.7.1.5
###################

# import tkinter as tk


# window = tk.Tk()
# button_1 = tk.Button(window, text="Ordinary button");
# button_1.pack()
# button_2 = tk.Button(window, text="Exceptional button")
# button_2.pack()
# button_2["borderwidth"] = 10
# button_2["highlightthickness"] = 10
# button_2["padx"] = 10
# button_2["pady"] = 5
# button_2["underline"] = 1
# window.mainloop()

###################
# Sección 1.7.1.6
###################

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

###################
# Sección 1.7.1.7
###################

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

###################
# Sección 1.7.1.8
###################

# import tkinter as tk

# window = tk.Tk()
# label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
# label_1.pack()
# label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
# label_2.pack()
# label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
# label_3.pack()
# window.mainloop()

###################
# Sección 1.8.1.1
###################

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
# id = frame.after(500, blink)
# frame.pack()
# window.mainloop()

###################
# Sección 1.8.1.2
###################

# import tkinter as tk


# def suicide():
#     frame.destroy()


# window = tk.Tk()
# frame = tk.Frame(window, width=200, height=100, bg='green')
# button = tk.Button(frame, text="I'm a frame's child")
# button.place(x=10, y=10)
# frame.after(5000, suicide)
# frame.pack()
# window.mainloop()

###################
# Sección 1.8.1.3
###################

# import tkinter as tk


# def flip_focus():
#     if window.focus_get() is button_1:
#         button_2.focus_set()
#     else:
#         button_1.focus_set()
#     window.after(1000, flip_focus)


# window = tk.Tk()
# button_1 = tk.Button(window, text="First")
# button_1.pack()
# button_2 = tk.Button(window, text="Second")
# button_2.pack()
# window.after(1000, flip_focus)
# window.mainloop()

###################
# Sección 1.9.1.4
###################

# import tkinter as tk

# def r_observer(*args):
#     print("Reading")

# def w_observer(*args):
#     print("Writing")

# dummy = tk.Tk()    # we need this although we won't display any windows
# variable = tk.StringVar()

# variable.set("abc")

# r_obsid = variable.trace_add("read", r_observer)
# w_obsid = variable.trace_add("write", w_observer)

# variable.set(variable.get() + 'd')  # read followed by write
# variable.trace_remove("read", r_obsid)
# variable.set(variable.get() + 'e')
# variable.trace_remove("write", w_obsid)
# variable.set(variable.get() + 'f')
# print(variable.get())

##################
## Corregido
##################

# def w_observer(*args):
#     print("Writing")


# dummy = tk.Tk()    # we need this although we won't display any windows
# variable = tk.StringVar()
# variable.set("abc")

# r_obsid = variable.trace_add("read", r_observer)
# w_obsid = variable.trace_add("write", w_observer)


# variable.set(variable.get() + 'd')  # read followed by write
# variable.trace_remove("read", r_obsid)
# variable.set(variable.get() + 'e')
# variable.trace_remove("write", w_obsid)
# variable.set(variable.get() + 'f')
# print(variable.get())