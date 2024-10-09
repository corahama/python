# ********* With nested functions *********
def decorator_function(func):
    def inner_function(*args, **kwargs):
        print('Functionality added to the function')
        return func(*args, **kwargs)
    return inner_function

def print_args(*args, **kwargs):
    print('The recieved args were')
    for arg in args:
        print(arg)

    print('The recieved kwargs were')
    for k,arg in kwargs.items():
        print(f'{k}={arg}')
    
    return 1
print_args = decorator_function(print_args)

# print(print_args(1,2,3, uno=1, dos=2))


# ********* With decorators *********
def decorator(func):
    def inner_func(*args, **kwargs):
        print(f'Funcionality added to the function.')
        return func(*args, **kwargs)
    return inner_func

@decorator
def print_args_new(*args, **kwargs):
    print('The recieved args were')
    for arg in args:
        print(arg)

    print('The recieved kwargs were')
    for k,arg in kwargs.items():
        print(f'{k}={arg}')
    
    return 1

# print(print_args_new('uno', 'dos', uno='one', dos='two'))


# ********* Decorators with args *********
def decorator(*dec_args):
    def outer_func(func):
        def inner_func(*args, **kwargs):
            # print(f'Funcionality with the message \'{message}\' added to the function.')
            print('Funcionality added to the function.')
            print('The args given to the decorator were:')
            print(', '.join(map(str, dec_args)))
            print()
            return func(*args, **kwargs)
        return inner_func
    return outer_func

@decorator('Hi every one', 'My name is Fernando')
def print_args_new(*args, **kwargs):
    print('The recieved args were')
    for arg in args:
        print(arg)

    print('The recieved kwargs were')
    for k,arg in kwargs.items():
        print(f'{k}={arg}')
    
    return 1

# print(print_args_new('uno', uno='one'))


# ********* Decorators with kwargs *********
def decorator(_func=None, **dec_kwargs):
    def outer_func(func):
        def inner_func(*args, **kwargs):
            print('Funcionality added to the function.')
            print('The kwargs given to the decorator were:')
            print(', '.join(map(lambda k,v: f'{k}: {v}', *dec_kwargs.items())))
            print()
            return func(*args, **kwargs)
        return inner_func
    
    if _func is None:
        return outer_func
    else:
        return outer_func(_func)

@decorator(message_one='hi', message_two='every one')
def print_args_new(*args, **kwargs):
    print('The recieved args were')
    for arg in args:
        print(arg)

    print('The recieved kwargs were')
    for k,arg in kwargs.items():
        print(f'{k}={arg}')
    
    return 1

# print(print_args_new('uno', uno='one'))
