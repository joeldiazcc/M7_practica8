import sys

from M7_practica8.read import read
from M7_practica8.delete import delete
from M7_practica8.insert import insert
from M7_practica8.update import update


def main():

    print("1 - Insertar série")
    print("2 - Eliminar série")
    print("3 - Modificar série")
    print("4 - Mostrar lista de séries")
    print("5 - Salir")
    print("-------------------------------------------")
    valor = int(input("Que quiere hacer: "))

    if(valor == 1):
        insert()
        print("-------------------------------------------")
        main()
    elif(valor == 2):
        delete()
        print("-------------------------------------------")
        main()
    elif(valor == 3):
        update()
        print("-------------------------------------------")
        main()
    elif(valor == 4):
        read()
        print("-------------------------------------------")
        main()
    elif(valor == 5):
        sys.exit()
    else:
        print("-----------------------------------------------")
        print("Porfavor inserte un dato numérico entre 1 y 5")
        main()

main()