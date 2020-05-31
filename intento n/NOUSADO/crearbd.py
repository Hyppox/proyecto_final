import sqlite3

def crearbd():

    conexion=sqlite3.connect("pacientes.db")
    try:
        conexion.execute("""create table pacientes(
                                    CI integer,
                                    nombre text,
                                    edad integer,


                                )""")
        print("se creo la tabla pacientes")                        
    except sqlite3.OperationalError:
        print("La base de datos ya existe")                    
    conexion.close()

def creartablapaciente(id):
        conexion=sqlite3.connect(id+'.db')
        try:
            conexion.execute("""create table id (
                                    codigo integer primary key AUTOINCREMENT,
                                    fecha text,
                                    datos real
                                )""")
            print("s ")                        
        except sqlite3.OperationalError:
            print("La  ")                    
        conexion.close()    

crearbd()