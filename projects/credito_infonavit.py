total = 500000
total_original = total
ingreso = total/(10*12)

años = 0
interes_total = 0

while total > 0:
    intereses = total * .11 - total * .05
    ingreso_neto = ingreso*12-intereses
    total -= ingreso_neto
    años += 1
    interes_total += intereses

print(años)
print(total_original/interes_total)