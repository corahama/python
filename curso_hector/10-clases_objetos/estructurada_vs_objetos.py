clientes = [{'Nombre':'Hector', 'Apellidos':'Guzman', 'dni':'1111111B'},
            {'Nombre':'Fernando', 'Apellidos':'Contreras', 'dni':'2222222B'}]

def mostrar_todos(clientes):
    for c in clientes:
        print('{} {}'.format(c['Nombre'], c['Apellidos']))

def mostrar_nombre(clientes, dni):
    for c in clientes:
        if c['dni'] == dni:
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente no encontrado')

def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if c['dni'] == dni:
            del(clientes[i])
            print('cliente: {} {} -> ELIMINADO'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente no encontrado')

mostrar_todos(clientes)
mostrar_nombre(clientes, '1111111B')
borrar_cliente(clientes, '1111111B')
mostrar_todos(clientes)
