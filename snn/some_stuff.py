import pandas as pd


def main():
    dataset = pd.read_csv('datasets/iris.data', header=None).values
    divs = [0,50,100,150]

    # for i in range(len(divs)-1):
    #     print(f'Results for class \'{dataset[divs[i], -1]}\': ', end='')
    #     print('-'.join(f'{dataset[divs[i]:divs[i+1], j].mean():.2f}' for j in range(dataset.shape[1]-1)))


    for i in range(len(divs)-1):
        summation = 0
        print(f'Results for class \'{dataset[divs[i], -1]}\': ', end='')
        for j in range(dataset.shape[1]-1):
            mean = dataset[divs[i]:divs[i+1], j].mean()
            summation += mean
            print(f'{mean:.2f}-', end='')
        print(f'{summation:.2f}')



if __name__ == '__main__':
    main()
