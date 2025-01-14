# Importar librerías necesarias
import pandas as pd
import numpy as np

# Cargar el archivo CSV original
input_file = r"C:\Users\esper\Desktop\Docs_Esperanza\github\Proj_data_analysis\Netflix.csv"
output_file = r"C:\Users\esper\Desktop\Docs_Esperanza\github\Proj_data_analysis\03_Netflix\Netflix_cleaned.csv"

df = pd.read_csv(input_file)

# Mostrar información básica del DataFrame original
print(df.info())

# Mostrar los primeros 5 registros para entender la estructura de los datos
print(df.head())

# Eliminar filas con todos los valores nulos
df_clean = df.dropna(how='all')

# Verificar valores únicos en la columna 'releaseYear'
print("Valores únicos en 'releaseYear':")
print(df_clean['releaseYear'].unique())

# Asegurarse de que 'releaseYear' sea numérica y manejar valores erróneos
df_clean['releaseYear'] = pd.to_numeric(df_clean['releaseYear'], errors='coerce')

# Filtrar años razonables (por ejemplo, 1900-2025)
df_clean = df_clean[(df_clean['releaseYear'] >= 1900) & (df_clean['releaseYear'] <= 2025)]

# Convertir 'releaseYear' a datetime, considerando solo el año
df_clean['releaseYear'] = pd.to_datetime(
    df_clean['releaseYear'].apply(lambda x: f"{int(x):.0f}" if pd.notnull(x) else np.nan), 
    format='%Y', 
    errors='coerce'
)

# Eliminar filas donde 'releaseYear' siga siendo nulo después de la conversión
df_clean.dropna(subset=['releaseYear'], inplace=True)

# Eliminar duplicados si existen
df_clean.drop_duplicates(inplace=True)

# Revisar el DataFrame limpio
print("DataFrame limpio:")
print(df_clean.info())
print(df_clean.head())

# Guardar el archivo limpio
df_clean.to_csv(output_file, index=False)

print(f"Archivo limpio guardado en: {output_file}")
