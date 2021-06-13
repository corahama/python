import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
# cursor.execute("CREATE TABLE usuarios (nombre VARCAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios VALUES ('Fernando', 22, 'fer@hotmail.com')")
# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()

usuarios = [
    ('Fernando', 22, 'fer@hotmail.com'),
    ('Laura', 21, 'lau@hotmail.com'),
    ('Andy', 21, 'andy@hotmail.com')
]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuarios")
usuario = cursor.fetchall()
print(usuario)


conexion.commit()
conexion.close()
