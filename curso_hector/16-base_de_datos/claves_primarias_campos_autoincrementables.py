import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuarios1(
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
#     ''')

# usuarios = [
#     ('11111111A', 'Fernando', 22, 'fer@hotmail.com'),
#     ('22222222B', 'Laura', 21, 'lau@hotmail.com'),
#     ('33333333C', 'Andy', 21, 'andy@hotmail.com'),
#     ('44444444D', 'Cynthia', 22, 'cynthia@hotmail.com'),
# ]

# cursor.executemany("INSERT INTO usuarios1 VALUES (?,?,?,?)", usuarios)

# cursor.execute('''
#     CREATE TABLE productos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio float NOT NULL
#     )''')

# productos = [
#     ('teclado', 'logitech', 19.99),
#     ('pantalla', 'lg', 80.99),
# ]

# cursor.executemany('INSERT INTO  productos VALUES (NULL,?,?,?)', productos)

# cursor.execute('SELECT * FROM productos')
# productos = cursor.fetchall()
# for producto in productos:
#     print(producto)

# cursor.execute('''
#     CREATE TABLE usuarios(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')
#
# usuarios = [
#     ('11111111A', 'Fernando', 22, 'fer@hotmail.com'),
#     ('22222222B', 'Laura', 21, 'lau@hotmail.com'),
#     ('33333333C', 'Andy', 21, 'andy@hotmail.com'),
#     ('44444444D', 'Cynthia', 22, 'cynthia@hotmail.com'),
# ]
#
# cursor.executemany('INSERT INTO usuarios VALUES (NULL,?,?,?,?)', usuarios)

cursor.execute('SELECT * FROM usuarios')
print_usuarios = cursor.fetchall()
for usuario in print_usuarios:
    print(usuario)


conexion.commit()
conexion.close()
