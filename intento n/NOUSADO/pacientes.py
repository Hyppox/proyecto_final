import sqlite3

class Pacientes:

    def abrir(self):
        conexion=sqlite3.connect("pacientes.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into pacientes(nombre,CI,edad) values (?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad from pacientes where CI=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad, CI from pacientes"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from pacientes where CI=?"
            cursor.execute(sql, datos)
            cone.commit()
            return  cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update pacientes set  CI=? , nombre=? , edad=? where CI=?"
            cursor.execute(sql, datos)
            cone.commit()
            return 1 # retornamos la cantidad de filas modificadas            
        except:
            cone.close()
