from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    # color = ColorChooser.askcolor(title="Elige un color")
    # print(color)

    # ruta = FileDialog.askopenfilename(title="Abir un fichero", initialdir="C:",
    #     filetype=(("Fichero de texto", "*.txt"), ("Fichero de texto avanzado", "*.txt2"),
    #     ("Todos los archivos", "*.*")))
    # print(ruta)

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        fichero.write("Hola")
        fichero.close()

Button(root, text="Boton", command=test).pack()


root.mainloop()
