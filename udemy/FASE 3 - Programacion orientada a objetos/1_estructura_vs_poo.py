# Ejemplo de implementacion con Programacion Estructurada
clientes= [
    {'Nombre':'Ever','Apellidos':'Ruiz Diaz','dni':'94479660'},
    {'Nombre':'Valentina','Apellidos':'dAndria','dni':'94479661'}
]

def mostrar_cliente(clientes, dni):
    for i in clientes:
        if (dni == i['dni']):
            print("{} {}".format(i['Nombre'],i['Apellidos']))
            return
        
    print("Cliente no encontrado.")
mostrar_cliente(clientes,'94479661')


def borrar_cliente(clientes,dni): # Enumerate= POSICION de indice + ELEMENTO
    for i,c in enumerate(clientes):
        if (dni == c['dni']): # c == ELEMENTO
            del(clientes[i]) # Aca se elimina la posicion
            print(str(c),"> BORRADO")
            return
    print("Cliente no encontrado, no se borrado nada.")
borrar_cliente(clientes,'94479668')
print(clientes)