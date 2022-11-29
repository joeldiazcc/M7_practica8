import psycopg2

def read():
    #conexión
    conexion = psycopg2.connect(user='postgres',
                                password='12345',
                                host='localhost',
                                port='5432',
                                database='postgres')

    cursor=conexion.cursor()

    #Senténcia sql
    sqlShow = "SELECT * FROM Series;"

    cursor.execute(sqlShow)

    conexion.commit()

    registro = cursor.fetchall()

    print(registro)

    cursor.close()
    conexion.close()


