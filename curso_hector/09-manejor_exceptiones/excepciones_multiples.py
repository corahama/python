# try:
#     n = input("Introduce un numero: ")
#     5/n
# except Exception as e:
#     print(type(e).__name__)

try:
    n = float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede divir un numero entre una cadena")
except ValueError:
    print("Tienes que introducir un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(type(e).__name__)
