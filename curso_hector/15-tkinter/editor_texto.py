from tkinter import *
from tkinter import filedialog as FileDialog

ruta = ''

def nuevo():
    mensaje.set("Nuevo archivo")
    texto.delete(1.0, END)
    global ruta
    ruta = ''
    root.title('Mi editor')

def abrir():
    mensaje.set("Abri un archivo")
    global ruta
    ruta = FileDialog.askopenfilename(title='Abrir un archivo', initialdir='.', filetypes=(("Archivos de texto", "*.txt"),))
    if ruta is not "":
        fichero = open(ruta, 'r')
        texto_lectura = fichero.read()
        texto.delete(1.0, END)
        texto.insert(INSERT, texto_lectura)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar un archivo")
    texto_guardar = texto.get(1.0,  "end-1c")
    try:
        global ruta
        fichero = open(ruta, 'w')
        fichero.write(texto_guardar)
        fichero.close()
        mensaje.set("Archivo guardado exitosamente")
    except:
        guardar_como()

def guardar_como():
    mensaje.set("Guardar un archivo como")
    texto_guardar = texto.get(1.0, "end-1c")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        fichero.write(texto_guardar)
        global ruta
        ruta = fichero.name
        fichero.close()
        root.title(ruta + " - Mi editor")
        mensaje.set("Archivo guardado exitosamente")
    else:
        mensaje.set("Archivo no guardado")


root = Tk()
root.title("Mi editor")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=0)
texto.config(bd=0, padx=6, pady=6, font=("consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
root.mainloop()
