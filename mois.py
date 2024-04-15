import pandas as pd
import matplotlib.pyplot as plt

try:
    data = pd.read_csv("Fichier_fusionne.csv")
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
except ValueError as e:
    print("Une erreur est survenue lors de la conversion de la colonne 'Date':", e)

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month

deaths_by_month = data.groupby('Month').size().reset_index(name='Total Deaths')

deaths_by_month = deaths_by_month.sort_values(by='Month', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(deaths_by_month['Month'], deaths_by_month['Total Deaths'], color='skyblue')
plt.title('Nombre total de décès par mois')
plt.xlabel('Mois')
plt.ylabel('Nombre total de décès')
plt.xticks(deaths_by_month['Month'], ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Déc'])
plt.tight_layout()
plt.show()
