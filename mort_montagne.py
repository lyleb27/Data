import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv("Fichier_fusionne.csv")

# Agréger les données pour compter le nombre total de décès par année
deaths_by_year = data.groupby('Annee').size().reset_index(name='Total Deaths')

# Créer le graphique à courbe
plt.figure(figsize=(12, 8))
plt.plot(deaths_by_year['Annee'], deaths_by_year['Total Deaths'], marker='o', color='skyblue', linestyle='-')

# Ajouter des titres et des étiquettes
plt.title('Nombre total de décès par année')
plt.xlabel('Année')
plt.ylabel('Nombre total de décès')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Afficher le graphique
plt.tight_layout()
plt.show()
