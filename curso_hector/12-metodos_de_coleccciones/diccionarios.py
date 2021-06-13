colores = {"amarillo":"yellow", "azul":"blue", "verde":"green"}
print(colores['amarillo'])
print(colores.get("negro","no se encuentra"))
print('amarillo' in colores)

print(colores.keys())
print(colores.values())
print(colores.items())

for c,v in colores.items():
    print(c,v)

print(colores.pop("amarillo", "no se ha encontrado"))
print(colores)
print(colores.pop("amarillo", "no se ha encontrado"))
colores.clear()
print(colores)
