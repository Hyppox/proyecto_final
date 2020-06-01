import sqlite3
from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect("bases_de_datos/ejercicios.db")

        return con

    except Error:

        print(Error)

def sql_table(con):
    try:
        conexion = con.cursor()

        conexion.execute("""create table ejercicios(
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            nombre text,
                                            


                                        )""")
        con.commit()
    except:
        pass
con = sql_connection()

sql_table(con)