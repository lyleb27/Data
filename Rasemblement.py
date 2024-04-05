import os
import pandas as pd
from datetime import datetime
import dateparser

# Code pour le fichier 1
dossier_base = "CSV"
fichier_entree = "Mountain_ranges.csv"
Nom_du_fichier_1 = "2_Mountain_ranges_modified.csv"

chemin_fichier_entree = os.path.join(dossier_base, fichier_entree)
donnees = pd.read_csv(chemin_fichier_entree, delimiter=';')
donnees.drop(columns=['Rang'], inplace=True)

donnees['Nom'] = donnees['Nom'].str.replace(' ', '-')
donnees.rename(columns=lambda x: x.strip(), inplace=True)
donnees['Chaîne'] = donnees['Chaîne'].str.replace(' ', '')

donnees['Nom'] = donnees['Nom'].str.lower()  # Mettre tous les noms en minuscules
donnees['Nom'] = donnees['Nom'].apply(lambda x: x.capitalize())  # Mettre la première lettre en majuscule

chemin_fichier_sortie = os.path.join(dossier_base, Nom_du_fichier_1)
donnees.to_csv(chemin_fichier_sortie, index=False)

# Code pour le fichier 2
dossier = "CSV"
fichiers_a_inclure = ["annapurna-I.csv", "broad-peak.csv", "cho-oyu.csv", "dhaulagiri-I.csv", "everest.csv", "gasherbrum-I.csv", "gasherbrum-II.csv", "k2.csv", "kangchenjunga.csv", "lhotse.csv", "makalu.csv", "manaslu.csv", "nanga-parbat.csv", "shishapangma.csv"]
Nom_du_fichier_2 = "1_Mountain_death.csv"
donnees_totales = []

# Formater le nom des montagnes
def formater_nom_montagne(nom):
    # Ignorer la modification des noms de montagne spécifiques
    montagnes_speciales = ["gasherbrum-ii"]
    if nom in montagnes_speciales:
        return nom[:1].upper() + nom[1:].lower().replace("ii", "II")
    else:
        mots = nom.split('-')
        mots_formates = []
        for mot in mots:
            mots_formates.append(mot[:1].upper() + mot[1:].lower())
        return '-'.join(mots_formates)


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
donnees_combinees.to_csv(Nom_du_fichier_2, index=False)

# Suppression de données
donnees = pd.read_csv(Nom_du_fichier_2)
donnees = donnees.replace(to_replace=r'(\s*)\[(.*?)\]', value='', regex=True)
donnees['Nationality'] = donnees['Nationality'].str.replace('Nazi ', '')

# Conversion de date
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

# Mettre tous les noms de montagnes en minuscules
donnees['Montagne'] = donnees['Montagne'].str.lower()
donnees['Montagne'] = donnees['Montagne'].apply(lambda x: x.capitalize())  # Mettre la première lettre en majuscule

# Enregistrer final
donnees.to_csv(os.path.join(dossier, Nom_du_fichier_2), index=False)
os.remove(Nom_du_fichier_2)

# Fusion des fichiers
Nom_du_fichier_fusionne = "Fichier_fusionne.csv"

f1 = pd.read_csv(os.path.join("CSV", "1_Mountain_death.csv"))
f2 = pd.read_csv(os.path.join("CSV", "2_Mountain_ranges_modified.csv"))

merged_df = pd.merge(f1, f2, how='left', left_on='Montagne', right_on='Nom')

merged_df.drop('Nom', axis=1, inplace=True)

merged_df = merged_df[['Montagne', 'Altitude (m)', 'Chaîne', 'Pays', 'Date', 'Name', 'Nationality', 'Cause of death']]

chemin_repertoire = os.getcwd()
chemin_fichier_fusionne = os.path.join(chemin_repertoire, Nom_du_fichier_fusionne)
merged_df.to_csv(chemin_fichier_fusionne, index=False)
