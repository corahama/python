"""Un profesor desea llevar el registro de las calificaciones de los 3 parciales de
sus 8 alumnos, despues de almacenar las calificaciones el profesor desea la
siguiente informacion:
a)El promedio de calificaciones de cada alumno almacenado en un arrego
b)Saber el alumno con el promedio mas alto
c)Saber el promedio del grupo"""

alumno1 = {"1":7, "2":5, "3":7}
alumno2 = {"1":5, "2":8, "3":4}
alumno3 = {"1":4, "2":5, "3":3}
alumno4 = {"1":9, "2":4, "3":8}
alumno5 = {"1":8, "2":7, "3":9}
alumno6 = {"1":2, "2":9, "3":1}
alumno7 = {"1":8, "2":6, "3":5}
alumno8 = {"1":9, "2":1, "3":8}

calificaciones = [alumno1, alumno2, alumno3, alumno4, alumno5, alumno6, alumno7, alumno8]
N = (len(calificaciones))
list = []
for l in range(0, 8):
    cal1=calificaciones[l]['1']+calificaciones[l]['2']+calificaciones[l]['3']
    cal=cal1/3
    list.append(cal)

n1=0
for l in range(0, 8):
    if l == 0:
        n1 = list[l]
    else:
        if list[l] > n1:
            n1 = list[l]
        else:
            pass

n2 = 0
for l in range(0,8):
    n2 = n2 + list[l]
    n3 = n2/8

print('El promedio de cada alumno es:', list)
print('El alumno con el promedio mas algo es', n1)
print('El promeido grupal es:', n3)
