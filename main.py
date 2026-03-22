from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Es una función que sirbe para conectarnos a tu nuestra base de datos
def get_db_connection():
    conn = sqlite3.connect('mycrypto.db')
    conn.row_factory = sqlite3.Row 
    return conn

# 1. Nuestra ruta de inicio 
@app.route('/')
def index():
    conn = get_db_connection()
    # Leemos lo que nos sale en la tabla de movimientos
    movimientos = conn.execute('SELECT * FROM Movimientos').fetchall()
    conn.close()
    
    # Enviamos los datos al HTML
    return render_template('index.html', movimientos=movimientos)

# 2. RUTA DE COMPRA 
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        pass
    
    return render_template('purchase.html')

@app.route('/status')
def status():
    return render_template('status.html')

if __name__ == '__main__':
    app.run(debug=True)