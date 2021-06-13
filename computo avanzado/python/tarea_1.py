def main():

    try:
        num = int(input('Introduce un numero: '))
    except:
        raise Exception("Valor introducido invalido.")

    count = 0
    # divisor_list = []
    for i in range(1, num+1):
        if num % i == 0:
            count +=1
            # divisor_list.append(i)

    print(count)
    
if __name__ == "__main__":
    main()