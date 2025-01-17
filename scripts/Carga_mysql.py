from sqlalchemy import create_engine
import pandas as pd

# Ruta del archivo CSV
file_path = r"C:\Users\esper\Desktop\Docs_Esperanza\github\Proj_data_analysis\03_Netflix\Netflix_project\data\Netflix_cleaned.csv"

# Cargar los datos desde el archivo CSV
df = pd.read_csv(file_path)

# Crear la conexión a MySQL
engine = create_engine('mysql+mysqlconnector://root:Hopemove07*@localhost/netflix')

# Cargar el DataFrame a la tabla MySQL
df.to_sql('netflix', con=engine, if_exists='append', index=False)

print("Datos cargados exitosamente a MySQL.")
