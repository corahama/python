from tkinter import *

def pedir():
    label.config(text="Tu cafe tiene {} y {}".format(leche_func(), azucar_func()))

def leche_func():
    if leche.get():
        return "leche"
    else:
        return "agua"

def azucar_func():
    if azucar.get():
        return "azucar"
    else:
        return "no tiene azucar"

root = Tk()

root.title('Cafeteria')
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

image = PhotoImage(file="coffee.gif")
Label(root, image=image).pack(side='left')

frame = Frame(root)
frame.pack(side='right')

Label(frame, text='¿Como quieres el cafe?').pack()
Checkbutton(frame, text='¿Con leche?', variable=leche, onvalue=1, offvalue=0).pack()
Checkbutton(frame, text='¿Con azucar?', variable=azucar, onvalue=1, offvalue=0).pack()
Button(frame, text='Pedir', command=pedir).pack()
label = Label(frame)
label.pack()


#ABAJO DEL TODO
root.mainloop()
