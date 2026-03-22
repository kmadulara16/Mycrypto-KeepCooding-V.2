import sqlite3

def inicializar_bd():
    # Esto crea el archivo mycrypto.db si no existe, o se conecta a él si ya existe
    conexion = sqlite3.connect('mycrypto.db')
    cursor = conexion.cursor()

    # Aquí definimos la tabla exactamente con las columnas que pide el documento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            moneda_from TEXT NOT NULL,
            cantidad_from REAL NOT NULL,
            moneda_to TEXT NOT NULL,
            cantidad_to REAL NOT NULL
        )
    ''')

    # Guardamos los cambios y cerramos la conexión
    conexion.commit()
    conexion.close()
    
    print("¡Base de datos 'mycrypto.db' y tabla 'Movimientos' creadas con éxito!")

if __name__ == '__main__':
    inicializar_bd()