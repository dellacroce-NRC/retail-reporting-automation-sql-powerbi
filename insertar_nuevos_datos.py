
import pandas as pd
import mysql.connector

# Configuración de conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambia si usas otro usuario
    password="Matnicolan1&",
    database="ventas_costos"
)
cursor = conn.cursor()

# Función para insertar datos desde CSV sin sobrescribir las PK
def insert_csv_to_mysql(csv_file, table_name, columns):
    df = pd.read_csv(csv_file)
    
    # Crear la consulta SQL de inserción ignorando duplicados
    placeholders = ", ".join(["%s"] * len(columns))
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {', '.join([f'{col}=VALUES({col})' for col in columns if col != 'id'])}"  
    
    # Convertir los valores a tuplas e insertarlos
    values = [tuple(row) for row in df.values]
    cursor.executemany(sql, values)
    conn.commit()
    print(f"Datos insertados en {table_name}: {len(values)} filas")

# Insertar nuevos datos en cada tabla
insert_csv_to_mysql("nuevas_sucursales.csv", "sucursales", ["id_sucursal", "nombre_sucursal", "ciudad", "region", "gerente"])
insert_csv_to_mysql("nuevos_productos.csv", "productos", ["id_producto", "nombre_producto", "categoria", "precio_venta", "costo_unitario"])
insert_csv_to_mysql("nuevas_ventas.csv", "ventas", ["id_venta", "id_sucursal", "id_producto", "fecha_venta", "cantidad_vendida", "total_venta"])
insert_csv_to_mysql("nuevos_costos.csv", "costos", ["id_costo", "id_sucursal", "id_producto", "fecha_costo", "cantidad_comprada", "total_costo"])

# Cerrar conexión
cursor.close()
conn.close()
print("Inserción de nuevos datos finalizada con éxito.")