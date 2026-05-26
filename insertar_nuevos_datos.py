import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE", "ventas_costos"),
)
cursor = conn.cursor()


def insert_csv_to_mysql(csv_file, table_name, columns):
    df = pd.read_csv(csv_file)

    placeholders = ", ".join(["%s"] * len(columns))
    updates = ", ".join([f"{col}=VALUES({col})" for col in columns if not col.startswith("id_")])
    sql = (
        f"INSERT INTO {table_name} ({', '.join(columns)}) "
        f"VALUES ({placeholders}) "
        f"ON DUPLICATE KEY UPDATE {updates}"
    )

    values = [tuple(row) for row in df.values]
    cursor.executemany(sql, values)
    conn.commit()
    print(f"Rows inserted or updated in {table_name}: {len(values)}")


insert_csv_to_mysql("nuevas_sucursales.csv", "sucursales", ["id_sucursal", "nombre_sucursal", "ciudad", "region", "gerente"])
insert_csv_to_mysql("nuevos_productos.csv", "productos", ["id_producto", "nombre_producto", "categoria", "precio_venta", "costo_unitario"])
insert_csv_to_mysql("nuevas_ventas.csv", "ventas", ["id_venta", "id_sucursal", "id_producto", "fecha_venta", "cantidad_vendida", "total_venta"])
insert_csv_to_mysql("nuevos_costos.csv", "costos", ["id_costo", "id_sucursal", "id_producto", "fecha_costo", "cantidad_comprada", "total_costo"])

cursor.close()
conn.close()
print("New data insertion test completed successfully.")
