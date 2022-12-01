import psycopg2

def delete():
    #conexión
    conexion = psycopg2.connect(user='postgres',
                                password='12345',
                                host='localhost',
                                port='5432',
                                database='postgres')
    cursor=conexion.cursor()

    #sentencia sql
    sqlDel = 'DELETE FROM Series WHERE idSerie=%s'

    idSerie = input("Inserte el id de la serie que quiere eliminar: ")

    dato = (idSerie)

    #Ejecutamos la sentencia sql con sus respectivos valores
    cursor.execute(sqlDel, dato)

    #Esto hace que los cambios en la BD sean coherentes
    conexion.commit()

    #cuando se haya llegado al número exacto de columnas, detiene el proceso
    registros = cursor.rowcount

    print('registro eliminado')

    cursor.close()
    conexion.close()
