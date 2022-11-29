import os
import sqlite3
from sqlite3 import Error


def conexionAjustes():
    try:
        os.mkdir('data')
        conn = sqlite3.connect('data/configuracion.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except FileExistsError:
        pass
    except Error:
        print(Error)


def conexion():
    try:
        # conn = sqlite3.connect('data/database.db')
        conn = sqlite3.connect('data/configuracion.db')
        cursor = conn.cursor()
        consulta = "select nombreBase from Ajustes"
        nombreBaseDeDatos = cursor.execute(consulta).fetchall()[0]
        if nombreBaseDeDatos != '':
            print("no hay base")
        else:
            print(nombreBaseDeDatos)
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except Error:
        print(Error)


def ajustes():
    ''' Creacion de base de datos para las configuraciones '''
    conn = conexionAjustes()
    cur = conn.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS [Ajustes] (
        [idAjuste] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        [nombreBase] VARCHAR(55)  NULL,
        [rutaBase] VARCHAR(250)  NULL;)
    """)
    conn.commit()
    conn.close()


def productos():
    ''' Creacion de base de datos para los productos '''
    conn = conexion()
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
