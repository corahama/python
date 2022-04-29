from os.path import exists
from os import mkdir
from datetime import date


def save(**kwargs):
    if not exists('results/'):
        mkdir('results/')

    num = 1
    today = date.today()
    file_path = lambda: f'results/{today.strftime("%m-%d-%y")}{f" ({num})" if num > 1 else ""}.txt'

    while exists(file_path()):
        num += 1

    with open(file_path(), 'w', encoding='utf-8') as f:
        for key, value in kwargs.items():
            f.write(f'{key}: {value}\n\n')

    return


def main():
    name = 'fernando'
    age = 25
    hobbies = ['programming', 'read', 'gym']

    di = {'degree': 'IT', 'languages': ['python', 'js', 'java']}

    save(name=name, age=age, hobbies=hobbies, **di)


if __name__ == '__main__':
    main()
