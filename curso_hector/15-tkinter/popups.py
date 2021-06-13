from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

def test():
    # MessageBox.showinfo("Hola", "Hola mundo")
    # MessageBox.showwarning("Cuidado", "Mensaje de precaucion")
    # MessageBox.shoralert("Alerta". "Mensaje de alerta")
    # resultado = MessageBox.askquestion("Salir", "¿Esta seguro que desea salir sin guardar?")
    # if resultado == "yes":
    #     root.destroy()
    # resultado = MessageBox.askokcancel("Salir", "¿Esta seguro que desea salir sin guardar?")
    # if resultado == True:
    #     root.destroy()
    # resultado = MessageBox.askyesno("Salir", "¿Esta seguro que desea salir sin guardar?")
    # if resultado == True:
    #     root.destroy()
    resultado = MessageBox.askretrycancel("Salir", "¿Esta seguro que desea salir sin guardar?")
    if resultado == True:
        root.destroy()



Button(root, text='Boton', command=test).pack()


root.mainloop()
