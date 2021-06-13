def main():
    custom_list = []

    try:
        num = int(input('Introduce un numero: '))
        custom_list.append(num)
        while (type(num) == int):
            num = int(input('Introduce un numero: '))
            custom_list.append(num)
    except:
        pass

    sum = 0
    toggle = False
    for i in custom_list[::-1]:
        if toggle:
            i_double = i*2
            if i_double > 9:
                i_double -= 9
            sum += i_double
            toggle = False
        else:
            sum += i
            toggle = True

    if sum % 10 == 0 or sum == 0:
        print('Valido')
    else:
        print('No Valido')
    
if __name__ == "__main__":
    main()