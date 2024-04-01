import os
import pandas as pd
from datetime import datetime
import dateparser

# Variable
dossier = "CSV"
fichiers_a_inclure = ["annapurna-I.csv", "broad-peak.csv", "cho-oyu.csv", "dhaulagiri-I.csv", "everest.csv", "gasherbrum-I.csv", "gasherbrum-II.csv", "k2.csv", "kangchenjunga.csv", "lhotse.csv", "makalu.csv", "manaslu.csv", "nanga-parbat.csv", "shishapangma.csv"]
Nom_du_fichier = "1_Mountain_death.csv"
donnees_totales = []

# Formater le nom des montagnes
def formater_nom_montagne(nom):
    return '-'.join([mot.capitalize() for mot in nom.split('-')])

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier):
    if fichier.endswith(".csv") and fichier in fichiers_a_inclure:
        chemin_fichier = os.path.join(dossier, fichier)
        df = pd.read_csv(chemin_fichier)
        # Formater le nom de la montagne
        nom_montagne = formater_nom_montagne(fichier.replace('.csv', ''))
        df['Montagne'] = nom_montagne
        donnees_totales.append(df)

# Enregistrer
donnees_combinees = pd.concat(donnees_totales, ignore_index=True)
donnees_combinees.to_csv(Nom_du_fichier, index=False)

# suprétion de donné 
donnees = pd.read_csv(Nom_du_fichier)
donnees = donnees.replace(to_replace=r'(\s*)\[(.*?)\]', value='', regex=True)
donnees['Nationality'] = donnees['Nationality'].str.replace('Nazi ', '')

# date
def convertir_date(date_str):
    parsed_date = dateparser.parse(date_str, languages=['en'])
    if parsed_date:
        if parsed_date.day == 1:
            return parsed_date.strftime('%m/%Y')
        else:
            return parsed_date.strftime('%d/%m/%Y')
    return date_str

donnees['Date'] = donnees['Date'].replace({"Summer 1990": "05/07/1990", "Winter 1999": "16/01/1999", "mid July 1982": "15/07/1982", "late June 1975": "28/06/1975", "19 May 1996 or May 1997": "19/05/1997"})
donnees['Date'] = donnees['Date'].apply(convertir_date)

colonnes = ['Montagne', 'Date', 'Name', 'Nationality', 'Cause of death']
donnees = donnees[colonnes]

# Enregistrer final
donnees.to_csv(os.path.join(dossier, Nom_du_fichier), index=False)
os.remove(Nom_du_fichier)