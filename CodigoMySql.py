import pandas as pd
import mysql.connector

# Ruta del archivo CSV
file_path = 'C:/Users/esper/Desktop/Docs_Esperanza/github/Proj_data_analysis/03_Netflix/Netflix_cleaned.csv'

# Cargar los datos desde el archivo CSV
df = pd.read_csv(file_path)

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host='localhost',       # Cambia si tu base de datos está en otro servidor
    user='root',      # Reemplaza con tu usuario de MySQL
    password='Hopemove07', # Reemplaza con tu contraseña
    database='netflix'  # Nombre de la base de datos que creaste
)

cursor = conn.cursor()

# Insertar los datos fila por fila
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO netflix (title, type, genres, releaseYear, imdbId, imdbAverageRating, imdbNumVotes, availableCountries)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos cargados exitosamente a MySQL.")
