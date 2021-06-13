import sqlite3

conexion = sqlite3.connect('ejemplo1.db')
cursor = conexion.cursor()

try:
    cursor.execute("""CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)""")

    cursor.execute("""CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL,
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))""")
    print("Las tablas han sido creadas")

except:
    print("Las tablas ya existen")


def agregar_categoria():
    categoria = input('Introduce una nueva categoria: ')
    try:
        cursor.execute("INSERT INTO categoria VALUES (NULL, ?)", (categoria,))
        print('Categoria creada\n')
    except:
        print('Categoria ya existente\n')


def agregar_plato():
    print("Tienes que introducir una categoria.")
    print("Las categorias disponibles son: ")
    cursor.execute("SELECT * FROM categoria")
    query = cursor.fetchall()
    if query == []:
        print("No hay categorias existentes")
        return

    for categoria in query:
        print(f"- {categoria[1]}({categoria[0]})")

    try:
        categoria_id = int(input("Introduce el id la categoria: "))
    except:
        print("Tienes que introducir un entero.")
        return

    if categoria_id in list(plato[0] for plato in query):
        nombre = input("Introduce el nombre del plato: ")
        cursor.execute("INSERT INTO plato VALUES (NULL, ?, ?)", (nombre, categoria_id))
        print("Platillo creado\n")
    else:
        print("El id introducido no corresponde a ninguna categoria.")
        return


def mostrar_menu():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    cursor.execute("Select * FROM plato")
    platos = cursor.fetchall()
    for categoria in categorias:
        menu = f"{categoria[1]} - "
        i = 0
        for plato in platos:
            if plato[2] == categoria[0]:
                if i == 0:
                    menu += plato[1]
                else:
                    menu += " // " + plato[1]
                i += 1
        print(menu)


print("*****Bienvenido al programa*****")
print("-Para agregar una nueva categoria introduce (1).")
print("-Para agregar un nuevo plato introduce (2).")
print("-Para mostrar el menu introduce (3).")
print("-Para salir del programa introduce (0).")
select = int(input())
while (select != 0):
    if select == 1:
        agregar_categoria()
    elif select == 2:
        agregar_plato()
    elif select ==3:
        mostrar_menu()

    conexion.commit()
    select = int(input("Introduce otra instruccion: "))

conexion.close()
