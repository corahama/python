def check_alphabet(list):
    tester = ord(list[0])
    for letter in list[1::]:
        if ord(letter)-1 != tester:
            print(chr(tester+1))
            break
        else:
            tester = ord(letter)
        

def main():
    alphabet = []

    try:
        size = int(input('Introduce la cantidad de letras que entrarán: '))
        if size < 2:
            raise Exception('La longitud del arreglo debe ser mínimo 2.')
        for _ in range(size):
            letter = input('Introduce una letra: ')
            alphabet.append(letter)
    except ValueError:
        raise Exception("Valor introducido no válido.")

    check_alphabet(alphabet)
    
if __name__ == "__main__":
    main()