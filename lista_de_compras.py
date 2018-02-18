objects_list = list()
def add_objects():
    articles = str(input('Ingresa un articulo: '))
    objects_list.append(articles)
    print('Articulo agregado')


def show_objects():
    cont = 0
    for article in objects_list:

        print("articulo {} {}".format(cont+1, article))
        cont = cont + 1


if __name__=='__main__':
    while True:
        user_opcion = str(input('''
                                Que quieres hacer?
                                Agregar articulo   [a]
                                Remover Arituculo  [r]
                                Ver los articulos  [v]
                                Salir              [e]
                                '''))
        if user_opcion == 'a' or user_opcion == 'A':
            add_objects()
        elif user_opcion == 'r' or user_opcion == 'R':
            del_objects()
        elif user_opcion == 'v' or user_opcion == 'V':
            show_objects()
        elif user_opcion == 'e' or user_opcion == 'E':
            print('Hasta Pronto')
            break