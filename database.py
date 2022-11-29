import os
import sqlite3
from sqlite3 import Error


def conexionAjustes():
    try:
        os.mkdir('data')
    except FileExistsError:
        pass
    try:
        conn = sqlite3.connect('data/configuracion.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except Error:
        print(Error)


def conexionInicial(nombreBase):
    # TODO ver que pasa si se sobrescribe la misma base de datos
    try:
        conn = sqlite3.connect('data/{}.db'.format(nombreBase))
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except Error:
        print(Error)


# AJUSTES
def ajustes():
    ''' Creacion de base de datos para las configuraciones '''
    conn = conexionAjustes()
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS [Ajustes] (
        [idAjuste] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        [nombreBase] VARCHAR(55)  NULL,
        [rutaBase] VARCHAR(250)  NULL)
    """)
    conn.commit()
    conn.close()




def activarBase():
    """
    entrega el nombre de la base de datos existente en la tabla ajustes
    :return:
    """
    conn = sqlite3.connect('data/configuracion.db')
    cursor = conn.cursor()
    consulta = "select nombreBase from Ajustes where idAjuste=1"
    try:
        nombreBaseDeDatos = cursor.execute(consulta).fetchall()[0]
        conn.close()
        return nombreBaseDeDatos
    except:
        return "no hay base conectada"


def crearYConectar(dato):
    # agrego letras al inicio del nombre de la base de datos
    dato = "data_" + dato
    # crea la base nueva
    conn = conexionInicial(dato)
    cur = conn.cursor()



# PRODUCTOS
def productos():
    ''' Creacion de base de datos para los productos '''
    nombrebase= activarBase()
    conn = conexionInicial(nombrebase)
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS [Productos] (
            [idProducto] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
            [nombreProducto] VARCHAR(55)  NULL,
            [detalle] VARCHAR(250)  NULL,
            [materialesCosto] VARCHAR(50)  NULL,
            [costoTotal] REAL(50)  NULL,
            [tiempoFabricacion] VARCHAR(50)  NULL,
            [beneficioEsperado] REAL(50)  NULL,
            [precio] REAL(50)  NULL            
            ;)
        """)
    conn.commit()
    conn.close()
