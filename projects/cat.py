n = int(input('Introduce la cantidad de meses: '))
c = int(input('Introduce el total del credito: '))
cat = float(input('Introduce el valor del CAT en porcentaje: '))/100
a = int(input('Introduce la anualidad: '))

p = sum([1/((1+cat)**(i/12)) for i in range(1,n+1)])
mensualidad = (c-a)/p

print(f'Las mensualidades serían de: {mensualidad}')
print(f'Total a pagar: {mensualidad*n}')