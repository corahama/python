f = open('reales.txt')
o = open("suma.dat",'w')

suma=0

for numero in f:
    x = numero
    suma += int(x)
    o.write(f"{x}")

o.write(f"\n{suma}")

f.close()
o.close()