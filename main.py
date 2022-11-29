import sys

# import per fer delete
from delete import delete
# import per fer insert
from insert import insert
# import per read
from read import read
# import per update
from update import update

exit = False
# -- Input ---
while exit == False:
    seleccio = input("Selecciona una opció indicant el número:\n1. Crear element\n2.Llegir elements\n3.Actualitzar taula\n4.Borrar elements\n5.Sortir")
    if int(seleccio) == 1:
        insert()
        exit = True
    elif int(seleccio) == 2:
        read()
        exit = True
    elif int(seleccio) == 3:
        update()
        exit = True
    elif int(seleccio) == 4:
        delete()
        exit = True
    elif int(seleccio) == 5:
        exit = True
    else:
        print("Escriu algun numero entre el 1-5.")
