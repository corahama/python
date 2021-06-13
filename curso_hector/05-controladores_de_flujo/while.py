c = 0
while c <= 5:
    c += 1
    if (c == 4):
        print("Rompemos el buble cuando c vale", c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c)

c = 0
while c <= 5:
    c += 1
    if (c == 4):
        print("Continuamos con la siguiente iteracion", c)
        continue
    print("c vale", c)
else:
    print("Se ha completado la iteracion y c vale", c)
