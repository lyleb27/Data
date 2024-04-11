import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Text, Scrollbar, mainloop

data = pd.read_csv("Fichier_fusionne.csv")

# Compter les occurrences de chaque cause de décès
causes_counts = data["Cause of death"].value_counts()

# Calculer le pourcentage total
total_deces = causes_counts.sum()

# Filtrer les causes avec un pourcentage inférieur à 3%
autre_seuil = 3
causes_principales = causes_counts[causes_counts / total_deces * 100 >= autre_seuil]
causes_autres = causes_counts[causes_counts / total_deces * 100 < autre_seuil]

# Regrouper les causes "Autres"
autres_sum = causes_autres.sum()
causes_principales["Autres"] = autres_sum

# Créer le graphique en secteurs (camembert)
plt.figure(figsize=(20, 12))

# Graphique principal
plt.subplot(1, 2, 1)
counts_principaux = causes_principales.tolist()
causes_principales = causes_principales.index.tolist()
plt.pie(counts_principaux, labels=causes_principales, autopct='%1.1f%%')
plt.title('Répartition des causes de décès')

# Afficher la liste triée des causes de décès
print("Répartition des causes de décès :")
for i in range(len(causes_principales)):
    cause = causes_principales[i]
    count = counts_principaux[i]
    pourcentage = (count / total_deces) * 100
    print(f"{cause}: {count} décès ({pourcentage:.1f}%)")

plt.tight_layout()
plt.show()

# Afficher les détails de la catégorie "Autres" dans une fenêtre texte
plt.subplot(1, 2, 2)
root = Tk()
root.title('Détails des autres causes de décès')

text = Text(root, wrap='word', height=20, width=40)
scrollbar = Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

for cause, count in causes_autres.items():
    text.insert('end', f"{cause}: {count} décès\n")

root.mainloop() # Pour arreter le programme, fermer la fenêtre tkinter puis "Ctrl + c" dans le terminal.