def evaluate_list(list):
    list.sort()
    pairs_list = []
    for i in range(len(list)-1):
        for e in list[i+1::]:
            if abs(list[i] - e) == 2:
                pairs_list.append([list[i], e])

    for pair in pairs_list:
        print("{},{}".format(pair[0], pair[1]))

def main():

    custom_list = []

    try:
        num = int(input('Introduce la cantidad de elementos del arreglo: '))
        for _ in range(num):
            num = int(input('Introduce un numero: '))
            if num not in custom_list:
                custom_list.append(num)
    except:
        raise Exception("Valor introducido no válido.")

    evaluate_list(custom_list)
    
if __name__ == "__main__":
    main()