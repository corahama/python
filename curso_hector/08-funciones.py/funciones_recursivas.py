def cuentra_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuentra_atras(num)
    else:
        print("Booom!!!")

cuentra_atras(5)

def factorial(num):
    factorial = 1
    for i in range(num):
        factorial *= i+1
        print(factorial)

factorial(5)

def factorial_recursiva(num):
    if num > 1:
        num = num * factorial_recursiva(num-1)
    return num

print(factorial_recursiva(5))
