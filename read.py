import psycopg2

# Funcio per llegir elements de la taula
def read():
    #conexión
    conexion = psycopg2.connect(user='postgres',
                                password='12345',
                                host='localhost',
                                port='5432',
                                database='postgres')
    # Declarem un cursor per realitzar operacions a la BD
    cursor=conexion.cursor()

    #Senténcia sql
    sqlShow = "SELECT * FROM Series;"
    # Consulta a la base de dades   
    cursor.execute(sqlShow)

    conexion.commit()

    registro = cursor.fetchall()

    print(registro)
    
    # Acabem conexió
    cursor.close()
    conexion.close()


