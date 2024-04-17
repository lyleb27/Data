import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Fichier_fusionne.csv")

data["Annee"] = data["Annee"].astype(int)

# Créer des tranches de 5 ans pour les années où il y a eu des décès
bins = [data["Annee"].min()] + [year for year in range(data["Annee"].min() + 5, data["Annee"].max() + 6, 5) if year in data["Annee"].values]
data["Tranche_5_ans"] = pd.cut(data["Annee"], bins=bins)
deaths_by_mountain_period = data.groupby(["Montagne", "Tranche_5_ans"]).size().unstack(fill_value=0)

mountains = deaths_by_mountain_period.index

# Créer un graphique pour chaque montagne
for mountain in mountains:
    mountain_data = deaths_by_mountain_period.loc[mountain]
    
    # Filtrer les tranches de 5 ans avec au moins un décès
    mountain_data = mountain_data[mountain_data != 0]
    
    if not mountain_data.empty:
        mountain_data.plot(kind='bar')
        plt.title(f"Décès par tranche de 5 ans pour {mountain}")
        plt.ylabel('Nombre de décès')
        plt.xlabel('Tranche de 5 ans')
        plt.ylim(0, 30) # Pour l'Everest, ajuster la limite à 65. 
        plt.show()