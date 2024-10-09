x = int(input('Introduce un numero: '))

for i in range(1, x + 1):
    if i == 1:
        r = i
    else:
        r = r * (i)

print('El factorial es : ', r)
