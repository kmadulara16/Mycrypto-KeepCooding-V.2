# Simulador de compra y venta de cryptomonedas

Aplicación web para el registro de inversiones y trading de criptomonedas utilizando la API de CoinMarketCap.

## Instalación y Configuración

1. **Instalar dependencias:**
   Ejecuta en la terminal:
   `pip install -r requirements.txt`

2. **Inicializar la Base de Datos:**
   Para crear la base de datos SQLite y la tabla de Movimientos, ejecuta:
   `python init_db.py`

3. **Arrancar el servidor:**
   Ejecutamos:
   `python main.py`
   Luego abrimos nuestro navegador en `http://127.0.0.1:5000/`