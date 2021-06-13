import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)

cursor.execute("UPDATE usuarios SET nombre='Fernando Contreras' WHERE dni='11111111A'")

cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)

# cursor.execute("DELETE usuarios")

conexion.commit()
conexion.close()
