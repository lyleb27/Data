# Data

## Rendu de projet de Data analyse

L'objectif du projet est l'étude d'un jeu de données concernant les causes de décès en montagne, le nettoyage des données et la visualisation de celles-ci grâce à Python.

- Le fichier harmonisation.py va regrouper l'ensemble des données, les trier et les rendre utilisables dans un fichier CSV qui sera créé à la racine du projet et qui s'appellera Fichier_fusionne.

- Le fichier camembert.py sert à faire une représentation graphique sous forme de camembert représentant la répartition des causes de décès en pourcentage.

- Le fichier carte.py va nous permettre de représenter de manière graphique une carte montrant la localisation des montagnes sur lesquelles nous travaillons.

- Le fichier graphique_barre.py sert à nous montrer le nombre de morts par année par montagne.

- Le fichier mort_montagne.py nous montre la courbe représentant le nombre de mort total par année en prenant en compte toutes les montagnes.

- Le fichier mois.py nous montre un graphique représentant le nombre de mort de toutes les montagnes par mois.


Pour pouvoir lancer les fichiers de création de graphiques, il faut d'abord exécuter harmonisation.py qui créera le fichier "Fichier_fusionne.csv" nécessaire à la création des graphiques.


```shell
git clone https://github.com/lyleb27/Data.git

python .\harmonisation.py
python .\camembert.py
python .\carte.py
python .\graphique_barre.py
python .\mort_montagne.py
python .\mois.py
```


Lebourcq Lyse, <br>
Lanfroid-Nazac Guillaume, <br>
Cassaigne Quentin.
