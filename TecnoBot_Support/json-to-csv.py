import pandas as pd

# Cargar datos JSON desde un archivo externo
df = pd.read_json('history.json')

# Guardar el archivo CSV
df.to_csv('output.csv', index=False)