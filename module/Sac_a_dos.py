import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('../data/Tableau données sac à dos Vélo.xlsx')

# Afficher les premières lignes
print(df.head())