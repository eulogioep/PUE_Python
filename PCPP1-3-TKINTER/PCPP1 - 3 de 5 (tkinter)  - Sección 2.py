###################
# Sección 2.1.1.3
###################

# import tkinter as tk
# from tkmacosx import Button

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
# button_1 = Button(window, text="Enabled", bg="red")
# button_1.bind("<Enter>", mouseover)
# button_1.bind("<Leave>", mouseout)
# button_1.pack()
# button_2 = Button(window, text="Enable/Disable", command=switch)
# button_2.pack()
# window.mainloop()

###################
# Sección 2.1.1.4
###################

# import tkinter as tk
# from tkinter import messagebox


# def count():
#     global counter
#     counter += 1

# def show():
#     messagebox.showinfo("","counter=" + str(counter) + ",state=" + ('Active' if switch.get() == 1 else 'Inactive'))

# window = tk.Tk()
# switch = tk.IntVar()
# counter = 0
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
# checkbutton.pack()
# window.mainloop()

###################
# Sección 2.1.1.5
###################

# import tkinter as tk
# from tkinter import messagebox

# def count():
#     global counter
#     counter += 1

# def show():
#     checkbutton.invoke()
#     messagebox.showinfo("", "counter=" + str(counter) + ",state=" + ('Active' if switch.get() == 1 else 'Inactive'))


# window = tk.Tk()
# switch = tk.IntVar()
# counter = 0
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
# checkbutton.pack()
# window.mainloop()

###################
# Sección 2.1.1.6
###################

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

###################
# Sección 2.2.1.1
###################

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

###################
# Sección 2.2.1.2
###################

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

###################
# Sección 2.2.1.3
###################

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

###################
# Sección 2.2.1.4
###################

# import tkinter as tk

# window = tk.Tk()
# label_frame_1 = tk.LabelFrame(window, text="Frame #1",
#                               width=200, height=100, bg='white')
# label_frame_2 = tk.LabelFrame(window, text="Frame #2",
#                               labelanchor='se', width=200, height=100, bg='yellow', relief = tk.RAISED, borderwidth=5)

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

###################
# Sección 2.3.1.1
###################

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
# text.trace_add('write', digits_only)
# entry.pack()
# entry.focus_set()
# window.mainloop()

###################
# Sección 2.3.1.3
###################

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
# sub_menu_file.add_command(label="About...", command=about_app)

# window.mainloop()

###################
# Sección 2.3.1.4
###################

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

###################
# Sección 2.3.1.5
###################

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
# sub_menu_file.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###################
# Sección 2.3.1.6
###################

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

###################
# Sección 2.3.1.7
###################

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
# sub_menu_file.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###################
# Sección 2.3.1.8
###################

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

###################
# Sección 2.3.1.9
###################

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

# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###################
# Sección 2.3.1.10
###################

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
# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

# for i in range(8):
#     number = str(i + 1)
#     sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)

# window.mainloop()

###################
# Sección 2.3.1.11
###################

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

###################
# Sección 2.3.1.12
###################

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

###################
# Sección 2.4.1.1
###################

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

###################
# Sección 2.4.1.2
###################

# import tkinter as tk

# window = tk.Tk()
# window.title('Icon?')
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
# window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
# window.mainloop()

###################
# Sección 2.4.1.3
###################

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

###################
# Sección 2.4.1.4
###################

# import tkinter as tk

# window = tk.Tk()
# window.minsize(width=250, height=200)
# window.geometry("500x500")
# window.mainloop()

###################
# Sección 2.4.1.5
###################

# import tkinter as tk

# window = tk.Tk()
# window.maxsize(width=500, height=300)
# window.geometry("200x200")
# window.mainloop()

###################
# Sección 2.4.1.6
###################

# import tkinter as tk

# window = tk.Tk()
# window.resizable(width=False, height=False)
# window.geometry("400x200")
# window.mainloop()

###################
# Sección 2.4.1.7
###################

# import tkinter as tk
# from tkinter import messagebox


# def really():
#     if messagebox.askyesno("?", "Wilt thou be gone?"):
#         window.destroy()


# window = tk.Tk()
# window.protocol("WM_DELETE_WINDOW", really)
# window.mainloop()

###################
# Sección 2.4.1.8
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askyesno("?", "To be or not to be?", icon='question', default='no')
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="Ask the question!", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.4.1.9
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.4.1.10
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.4.1.11
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.askquestion("?", "I'm going to format your hard drive")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.4.1.12
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.showerror("!", "Your code does nothing!")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="Alarming message", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.4.1.13
###################

# import tkinter as tk
# from tkinter import messagebox


# def question():
#     answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
#     print(answer)


# window = tk.Tk()
# button = tk.Button(window, text="What's going on?", command=question)
# button.pack()
# window.mainloop()

###################
# Sección 2.5.1.2
###################

# import tkinter as tk


# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line((10, 380), (200, 10), (380, 380), (10, 380))
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.3
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line((10, 380), (200, 10), (380, 380), (10, 380),
#                    arrow=tk.BOTH, fill='red', smooth=True, width=1)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.4
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='black')
# canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.5
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='black')
# canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.6
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='blue')
# canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.7
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_arc(120, 50, 300, 300, outline='red', width=5)
# # canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
# #                   style=tk.CHORD, start=90, fill='white')
# # canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
# #                   style=tk.ARC, start=180, extent=180)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

#######################
## Pruebas dinámicas
#######################

# import tkinter as tk

# def dibujar_arco():
#     global arco, dinamico

#     dinamico += 10

#     canvas.delete(arco)
#     canvas.pack()
#     arco = canvas.create_arc(10, 100, 380, 300, start= dinamico % 360, extent= 90,  outline='red', width = 5)
    

# def temporizador():
#     dibujar_arco()
#     canvas.after(100, temporizador)
      

# ventana = tk.Tk()

# dinamico = 0
# canvas = tk.Canvas(ventana, width=400, height=400, bg='yellow')
# canvas.pack()

# arco = canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
# canvas.after(500, temporizador)
# ventana.mainloop()


###################
# Sección 2.5.1.8
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='blue')
# canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
#                    font=("Arial","40","bold"),
#                    justify=tk.CENTER,
#                    fill='white')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.9
###################

# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# image = tk.PhotoImage(file='logo.png')
# canvas.create_image(0, 0, image=image, anchor = tk.NW)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

###################
# Sección 2.5.1.10
###################

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

#################################
# Laboratorio de Sección 3.1.1.2
#################################

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

########################
# Solución personalizando la posición de componentes en frames

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
#     v1 = get_number(campo1)
#     if v1 is None:
#         messagebox.showerror("Error", "Argumento inválido en el primer campo")
#         campo2.focus_set()
#         return
#     v2 = get_number(campo2)
#     if v2 is None:
#         messagebox.showerror("Error", "Argumento inválido en el segundo campo")
#         campo2.focus_set()
#         return
#     op = operador.get()
#     if op == 3 and v2 == 0:
#         messagebox.showerror("Error", "No es posible dividir por cero")
#         campo2.focus_set()
#         return
#     if op == 0:
#         resultado = v1 + v2
#     elif op == 1:
#         resultado = v1 - v2
#     elif op == 2:
#         resultado = v1 * v2
#     else:
#         resultado = v1 / v2
#     messagebox.showinfo("Resultado", "Resultado: " + str(resultado))

# ventana = Tk()
# ventana.title("Calculator")

# operador = IntVar()

# marco_1 = Frame(ventana, width=30, height=100, bg='white')
# marco_2 = Frame(ventana, width=30, height=100, bg='yellow')
# marco_3 = Frame(ventana, width=200, height=100, bg='grey')

# campo1 = Entry(marco_1)
# campo2 = Entry(marco_1)

# suma = Radiobutton(marco_2, text="+", var=operador, val=0)
# resta = Radiobutton(marco_2, text="-", var=operador, val=1)
# multiplicacion = Radiobutton(marco_2, text="*", var=operador, val=2)
# division = Radiobutton(marco_2, text="/", var=operador, val=3)
# boton = Button(marco_3, text="Evaluar", command=doeval)

# #############################
# ## Posición de los elementos

# marco_1.pack(side = 'left')
# marco_2.pack()
# marco_3.pack(side = 'bottom')

# campo1.pack()
# campo1.focus_set()
# campo2.pack()
# suma.grid(row=0, column=1)
# resta.grid(row=0, column=2)
# multiplicacion.grid(row=0, column=3)
# division.grid(row=0, column=4)
# boton.grid(row=2, column = 4, columnspan=3)

# ventana.mainloop()

#################################
# Laboratorio de Sección 3.1.1.3
#################################

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
# bt.bind("<Button-1>", domove)
# x = y = 10
# bt.place(x=x, y=y)
# random.seed()
# wn.mainloop()

#################################
## Mariano
# import tkinter as tk
# import random

# def mouseover(evento):
#     #Escojo un numero random entro 0 y 450 para que este dentro de la ventana 
#     boton.place(x= random.randint(0,450) ,y=random.randint(0,450))

# #Creo la ventana
# window = tk.Tk()
# window.title("Atrapame si puedes")
# window.geometry("500x500")
# #El boton comienza en el margen superior izq
# boton = tk.Button(text="Atrapame")
# boton.bind("<Enter>", mouseover)
# boton.place(x=0, y=0)

# window.mainloop()

#################################
## Traducido y modificado

# from tkinter import *
# import random

# def nuevas_coordenadas(xy):
#     nueva_coordenada = random.randint(1, 420)
#     while abs(xy - nueva_coordenada) < 100:
#         nueva_coordenada = random.randint(1, 420)
#     return nueva_coordenada

# def mover_boton(ev):
#     global coord_x, coord_y
#     nuevo_x = nuevas_coordenadas(coord_x)
#     nuevo_y = nuevas_coordenadas(coord_y)
#     boton.place(x=nuevo_x, y=nuevo_y)

# ventana = Tk()
# ventana.geometry("500x500")
# ventana.title("Atrápame!")
# boton = Button(ventana, text="Atrápame!")
# boton.bind("<Button-1>", mover_boton)
# coord_x = coord_y = 10
# boton.place(x=coord_x, y=coord_y)
# ventana.mainloop()

#################################
# Laboratorio de Sección 3.1.1.4
#################################

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

###########################
## Traducido

# import tkinter as tk
# from tkinter import messagebox
# from random import randint

# def temporizador():
#     global segundos, id_crono
#     if crono_iniciado:
#         segundos += 1
#         etiqueta_crono["text"] = str(segundos)
#         id_crono = etiqueta_crono.after(1000, temporizador)

# def boton_pulsado(evento):
#     global crono_iniciado, id_crono, intentos
#     intentos += 1
#     if not crono_iniciado:
#         crono_iniciado = True
#         etiqueta_crono.after(1000, temporizador)
#     clicked_btn = evento.widget
#     clicked_val = int(clicked_btn["text"])
#     if clicked_val == lista_numeros[0]:
#         clicked_btn["state"] = tk.DISABLED
#         del lista_numeros[0]
#     if len(lista_numeros) == 0:
#         crono_iniciado = False
#         etiqueta_crono.after_cancel(id_crono)
#         messagebox.showinfo("Enhorabuena!", "Enhorabuena!\nNúmero de intentos:" + str(intentos) +  '\n - tiempo: ' + str(segundos) + " segundos")
        
# ###########################################
# ventana = tk.Tk()
# ventana.title("Clicker")
# lista_numeros = []

# # generar 25 números aleatorios
# for contador in range(25):
#     nuevo_numero = randint(1, 999)
#     # Si el número ya ha sido seleccionado
#     while nuevo_numero in lista_numeros:
#         nuevo_numero = randint(1, 999)
#     lista_numeros.append(nuevo_numero)

# # Crear los botones y posicionarlos en el grid
# for indice in range(25):
#     nuevo_boton = tk.Button(ventana, text=str(lista_numeros[indice]), width=10)
#     nuevo_boton.grid(column=indice // 5, row=indice % 5)
#     nuevo_boton.bind("<Button-1>", boton_pulsado)

# # Y después ordenar los números de menor a mayor
# lista_numeros.sort()

# id_crono = ''
# intentos = 0
# segundos = 0
# etiqueta_crono = tk.Label(ventana, text=str(segundos))
# etiqueta_crono.grid(column=2, row=5)
# crono_iniciado = False
# ventana.mainloop()

#################################
## José Antonio
## Solución con clases
#################################

# #El tablero del Clicker consta de 25 botones y cada uno de los botones contiene un número aleatorio 
# # del rango 1..999. Nota: ¡cada número es diferente!
# #Debajo del tablero hay un temporizador que inicialmente muestra 0. El temporizador comienza 
# # cuando el usuario hace clic en el tablero por primera vez

# #Esperamos que el jugador haga clic en todos los botones en el orden impuesto por los números, 
# # del más bajo al más alto

# #   el botón en el que se hace clic correctamente cambia el estado del botón a DESACTIVADO
# #   el botón presionado incorrectamente no muestra actividad
# #   el temporizador aumenta su valor cada segundo
# #   cuando todos los botones están atenuados (es decir, el jugador ha completado su tarea),
# #        el cronómetro se detiene inmediatamente

# from os import name
# from tkinter import Tk, Label, Frame, IntVar, StringVar

# from random import randint
# if name =='posix':
#     from tkmacosx import Button  
# else:
#     from tkinter import Button

# class Tablero(Frame):
#     def __init__(self, master=None, filas=5, columnas=5):
#         super().__init__(master)
#         self.__master = master
#         self.__filas = filas
#         self.__columnas = columnas
#         self.__valores_btns = []
#         self.__botones = []
#         self.__crear_valores_btns()
#         self.__crear_tablero()
        
#     @property
#     def obtener_valores(self):
#         return self.__valores_btns

#     def __crear_valores_btns(self):
#         while len(self.__valores_btns) < self.__filas * self.__columnas:
#             self.__valores_btns.append(self.__azar())

#     def __azar(self) -> str:
#         valor = randint(1, 999)
#         while valor in self.__valores_btns:
#             valor = randint(1, 999)
#         return valor

#     def __crear_tablero(self):
#         cont = 0
#         for fila in range(self.__filas):
#             for columna in range(self.__columnas):
#                 boton = Button(self)
#                 boton.grid(row=fila, column=columna)
#                 boton['text']= self.__valores_btns[cont]
#                 self.__botones.append(boton)
#                 cont += 1
        

# class Temporizador(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.segundos = IntVar(value=0)
#         self.__continuar = False
#         self.etq_reloj = Label(self, textvariable= self.segundos, width=30)
#         self.etq_reloj.pack()
#         self.etq_reloj.bind("<Button-1>", self.__activar_reloj)
        
#     def __activar_reloj(self, event=None):
#         self.__continuar = True
#         self.etq_reloj.unbind("<Button-1>")
#         #self.etq_reloj.bind("<Button-2>", self.parar)
#         self.__contar_segundos()
        
#     def __contar_segundos(self):
#         if self.__continuar:
#             self.segundos.set(value=self.segundos.get()+1)
#             self.etq_reloj.after(1000, self.__contar_segundos)
    
#     #def parar(self, event=None):
#     def parar(self):
#         self.__continuar = False

# class Clicker(Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title('Cricker')
#         self.fr_tablero = Tablero(self)
#         self.fr_tablero.pack()
#         self.fr_crono = Temporizador(self)
#         self.fr_crono.pack()
    

# juego = Clicker()
# juego.mainloop()
# '''
# fr_tablero = Tablero(ventana)
# fr_tablero.pack()

# fr_crono = Temporizador(ventana)
# fr_crono.pack()
# ventana.mainloop()
# '''
#################################
# Laboratorio de Sección 3.1.1.5
#################################

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
#     print(phase)
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

#################################
# Laboratorio de Sección 3.1.1.6
#################################

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

#################################
# Laboratorio de Sección 3.1.1.6
#################################

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