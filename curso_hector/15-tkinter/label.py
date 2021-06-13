from tkinter import *

root = Tk()

# frame = Frame(root, width=480, height=320)
# frame.pack()

# label = Label(frame, text = 'Hola mundo')
# label = Label(root, text = 'Hola mundo')
# label.place(x=0, y=0)

"""texto = StringVar()
texto.set('Un nuevo texto')

Label(root,text = 'Hola mundo').pack(anchor='nw')
label = Label(root,text = 'Otra etiqueta')
label.pack(anchor='center')
Label(root,text = 'Ultima etiqeta').pack(anchor='se')

label.config(bg='green', fg='blue', font=('verdana',24))
label.config(textvariable=texto)
"""

imagen = PhotoImage(file='giphy.gif')
Label(root, image=imagen, bd=0).pack()

#ABAJO DEL TODO
root.mainloop()
