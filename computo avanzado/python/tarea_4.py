def main():

    num = int(input('Introduce un numero: '))

    total_sum = 0
    for i in range(1, int((num/2)+1)):
        temp = []
        for e in bin(i)[2::]:
            temp.append(int(e))
        total_sum += sum(temp)
    
    print(total_sum)

if __name__ == "__main__":
    main()