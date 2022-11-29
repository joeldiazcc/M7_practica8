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

    cursor.execute(sqlDel, dato)

    conexion.commit()

    registros = cursor.rowcount

    print('registro eliminado')

    cursor.close()
    conexion.close()

