from tkinter import *
import sqlite3

conexion = sqlite3.connect('ejemplo1.db')
cursor = conexion.cursor()

root = Tk()
root.title("Bar Don Fercho")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="Bar Don Fercho", font=("verdana", 22)).pack()
Label(root, text="Menu del dia", font=("verdana", 18)).pack()

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1]).pack()
    platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id='{categoria[0]}'").fetchall()
    for plato in platos:
        Label(root, text=plato[1]).pack()

Label(root, text="%15 IVA incluido").pack()


root.mainloop()
conexion.commit()
conexion.close()
