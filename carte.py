import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

data = {
    "Nom": ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", "Annapurna-I", "Broad-peak", "Cho-oyu", "Dhaulagiri-i", "Gasherbrum-i", "Gasherbrum-ii", "Manaslu", "Nanga-parbat", "Shishapangma"],
    "Pays": ["Chine/Népal", "Chine/Pakistan", "Inde/Népal", "Népal/CHine", "Népal/Chine", "Népal", "Chine/Pakistan", "Chine/Népal", "Népal", "Pakistan/Chine", "Pakistan/Chine", "Népal", "Pakistan", "Chine"],
    "Longitude": ["86.9250° E", "76.5133° E", "88.1467° E", "86.9336° E", "87.0913° E", "83.8203° E", "76.5683° E", "86.6600° E", "83.4936° E", "76.6925° E", "76.6558° E", "84.5594° E", "74.5896° E", "85.7786° E"],
    "Latitude": ["27.9881° N", "35.8804° N", "27.7022° N", "27.9619° N", "27.8842° N", "28.5958° N", "35.8144° N", "28.0940° N", "28.6961° N", "35.7225° N", "35.7594° N", "28.5497° N", "35.2372° N", "28.3536° N"],
    "Altitude": [8849, 8611, 8586, 8516, 8485, 8091, 8051, 8188, 8167, 8080, 8035, 8163, 8126, 8027]
}

df = pd.DataFrame(data)

df["Longitude"] = df["Longitude"].str.replace('° E', '').astype(float)
df["Latitude"] = df["Latitude"].str.replace('° N', '').astype(float)

# Convertir les coordonnées en points géographiques
geometry = [Point(lon, lat) for lon, lat in zip(df["Longitude"], df["Latitude"])]

# Créer un GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# Définir les couleurs pour chaque pays
colors = {
    "Chine": "red",
    "Népal": "green",
    "Inde": "purple",
    "Pakistan": "blue"
}
gdf["Color"] = gdf["Pays"].apply(lambda x: colors.get(x.split("/")[0], "gray"))

# Afficher la carte
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(color='lightgray', edgecolor='black')
gdf.plot(ax=ax, color=gdf["Color"], marker='o', markersize=20)
plt.title("Carte des montagnes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
