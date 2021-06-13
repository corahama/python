from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def borrar():
    n1.set('')
    n2.set('')

root = Tk()

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text='Numero 1:').grid(row=0,column=0, sticky='e')
Entry(root, justify='center', textvariable=n1).grid(row=0,column=1)
Label(root, text='Numero 2:').grid(row=1,column=0, sticky='e')
Entry(root, justify='center', textvariable=n2).grid(row=1,column=1)
Label(root, text='Resultado:').grid(row=2,column=0, sticky='e')
resultado = Entry(root, justify='center', textvariable=r, state='disabled').grid(row=2,column=1)


Button(root, text='Sumar', command=sumar).grid(row=4)



#ABAJO DEL TODO
root.mainloop()
