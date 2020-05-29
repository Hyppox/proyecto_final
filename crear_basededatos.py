import sqlite3
from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect("bases_de_datos/pacientes.db")

        return con

    except Error:

        print(Error)

def sql_table(con):
    try:
        conexion = con.cursor()

        conexion.execute("""create table pacientes(
                                            CI integer,
                                            nombre text,
                                            edad integer,
                                            sexo text


                                        )""")
        con.commit()
    except:
        pass
con = sql_connection()

sql_table(con)