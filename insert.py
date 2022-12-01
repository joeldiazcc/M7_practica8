import psycopg2

def insert():
    #conexión
    conexion = psycopg2.connect(user='postgres',
                                password='12345',
                                host='localhost',
                                port='5432',
                                database='postgres')

    cursor=conexion.cursor()

    #Senténcia sql
    sqlIns = "INSERT INTO Series(nombre, temporadas, valoracion, premios, director, productora) values(%s, %s, %s, %s, %s, %s);"

    #Pedimos los datos
    nombre=input("Ingrese el nombre de la serie: ")
    temporadas=input("Números de temporadas: ")
    valoracion=input("Media de valoraciones: ")
    premios=input("Premios ganados: ")
    director=input("Director: ")
    productora=input("Productora: ")

    #Los almacenamos en una lista
    datos = (nombre, temporadas, valoracion, premios, director, productora)

    #ejecutamos el sql
    cursor.execute(sqlIns, datos)

    conexion.commit()

    #Cuando llegue al número de columnas especificado deja de ejecutarse
    registros = cursor.rowcount

    print('registro insertado')

    #Cerramos la conexion
    cursor.close()
    conexion.close()

