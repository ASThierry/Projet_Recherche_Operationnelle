import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('../data/velo.xlsx')

# Afficher les premières lignes
print(df.head())