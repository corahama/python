from tkinter import *

root = Tk()

def action():
    monitor.config(text="{}".format(option.get()))

def reset():
    option.set(None)
    monitor.config(text="")

option = IntVar()

Radiobutton(root, text='Opcion 1', variable=option, value=1, command=action).pack()
Radiobutton(root, text='Opcion 2', variable=option, value=2, command=action).pack()
Radiobutton(root, text='Opcion 3', variable=option, value=3, command=action).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Button", command=reset).pack()


#ABAJO DEL TODO
root.mainloop()
