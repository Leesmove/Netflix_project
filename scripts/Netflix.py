import pandas as pd

# 1️⃣ Cargar el dataset
file_path = r"C:\Github\Data\netflix.csv"  # Asegúrate de usar la ruta correcta
df = pd.read_csv(file_path)

# 2️⃣ Mostrar información básica
print("📌 Información del DataFrame:")
print(df.info())

# 3️⃣ Mostrar 5 registros para entender la estructura
print("\n📌 Primeras 5 filas:")
print(df.head())

# 4️⃣ Eliminar valores nulos
df.dropna(subset=['releaseYear', 'genres'], inplace=True)

# 5️⃣ Verificar valores únicos en la columna 'releaseYear'
print("\n📌 Valores únicos en 'releaseYear':")
print(df['releaseYear'].unique())

# 6️⃣ Asegurar que 'releaseYear' sea numérica y manejar valores erróneos
df['releaseYear'] = pd.to_numeric(df['releaseYear'], errors='coerce')

# 7️⃣ Filtrar años razonables (1900-2025)
df = df[(df['releaseYear'] >= 1900) & (df['releaseYear'] <= 2025)]

# 8️⃣ Convertir 'releaseYear' a datetime (solo año)
df['releaseYear'] = pd.to_datetime(df['releaseYear'], format='%Y', errors='coerce')

# 9️⃣ Eliminar filas donde 'releaseYear' siga siendo nulo
df.dropna(subset=['releaseYear'], inplace=True)

# 🔟 Eliminar duplicados
df.drop_duplicates(inplace=True)

# 1️⃣1️⃣ Expandir filas para que haya una por cada país disponible
df['availableCountries'] = df['availableCountries'].fillna('Unknown')  # Llenar NaN con "Unknown"
df = df.assign(availableCountries=df['availableCountries'].str.split(',')).explode('availableCountries')

# 1️⃣2️⃣ Expandir filas para que haya una por cada categoría/género
df = df.assign(genres=df['genres'].str.split(',')).explode('genres')

# 1️⃣3️⃣ Identificar categorías más populares en Netflix
print("\n📌 Categorías más populares en Netflix:")
print(df['genres'].value_counts().head(10))

# 1️⃣4️⃣ Países con más contenido en Netflix
print("\n📌 Países con más contenido en Netflix:")
print(df['availableCountries'].value_counts().head(10))

# 1️⃣5️⃣ Guardar dataset limpio
df.to_csv("Netflix_dataset_cleaned.csv", index=False)

print("\n✅ Limpieza y análisis completados. Archivo guardado como 'Netflix_dataset_cleaned.csv'.")