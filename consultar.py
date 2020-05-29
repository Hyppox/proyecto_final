import sqlite3
import crear_carpeta as ccbd
import crear_basededatos as cbd

class Consultar:
    def __init__(self):
        pass
    def consulta(datos):
        try:
            ccbd.bases_de_datos
            cbd
            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
        except:

            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            pass
    

        cursor=conexion.cursor()
        sql="select CI, nombre,edad from pacientes where CI=?"
        cursor.execute(sql, datos)
        return cursor.fetchall()
        
        conexion.close()
