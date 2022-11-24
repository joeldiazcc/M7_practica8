import psycopg2
host = "containers-us-west-56.railway.app"
database = "railway"
user = "postgres"
password = "pQSOeO9JaxLbscL1hb4x"
port = 7318

cur = None

try:
    con = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE Series (id SERIAL PRIMARY KEY
                Name VARCHAR(255) NOT NULL,
                Seasons INT NOT NULL,
                Valor DECIMAL(10,0) NOT NULL,
                Rewards INT NOT NULL,
                Director VARCHAR(255) NOT NULL,
                Product VARCHAR(255) NOT NULL
                )
                """)
    con.commit()

    #cur.execute("SELECT 1 + 1")
    #result = cur.fetchone()
    #print(result)


    cur.close()
    con.close()
    print("correct connection")
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()