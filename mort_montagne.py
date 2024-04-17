import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Fichier_fusionne.csv")

deaths_by_year = data.groupby('Annee').size().reset_index(name='Total Deaths')

plt.figure(figsize=(12, 8))
plt.plot(deaths_by_year['Annee'], deaths_by_year['Total Deaths'], marker='o', color='skyblue', linestyle='-')
plt.title('Nombre total de décès par année')
plt.xlabel('Année')
plt.ylabel('Nombre total de décès')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
