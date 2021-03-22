# ===================installation des bibliothèques =============================

# sur le terminal, écrire (sans le #) : 
# si pip ne fonctionne pas, remplacer par pip3
# pip install holoviz
# pip install geopandas
# pip install geoviews
# pip install leaflet
# pip install folium
# pip install pandas
# jupyter notebook

# si vous n'avez pas de jupyter notebook : 
# pip install --user jupyter
# python3 -m notebook

# Autre méthode : dans jupyter notebook : 
# vérifier que les modules suivants ont été téléchargés dans jupyter notebook, sans le # devant : 
# !pip install holoviz
# !pip install geopandas
# !pip install geoviews
# !pip install holoviews
# !pip install leaflet
# !pip install folium


# ==================== 1.affichage du fond de carte ===============================

import folium
coords = (46.539758, 2.430331)
map1 = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=4)
# on télécharge un fond de carte centré sur les coordonnées (46.539758, 2.43033) et avec un zoom de 6
# on appelle ce fond de carte "map1"

map1
# affichage du fond de carte.




# ============= 2. je réalise une carte avec quelques données ==========

# on rentre les données : chaque lieu de naissance d'un artiste (ici "lieunaiss") 
# est associé à sa latitude et sa longitude, écrite avec des points et non des virgules !
# et au salaire de l'artiste, une variable quantitative.

lieunaiss = ['Sarlat', 
'Alger', 
'Bordeaux', 
'Le Puy', 
'Pontivy', 
'Nérac']

latitudes = [44.879395, 
36.7753606, 
44.864586, 
45.045694, 
48.053784, 
44.130119]

longitudes = [1.210272, 
3.0601882, 
-0.551486, 
3.883203, 
-2.976056, 
0.333947]

salaire = [40, 
200, 
87, 
450, 
300, 
100] 

# pour chaque lieunaiss, je demande à mettre un point dont la latitude et la longitude rentrées plus tôt
# et dont le rayon est proportionnel au salaire divisé par 1000.
# comme couleur de marqueur, on a ‘red’, ‘blue’, ‘green’, ‘purple’, ‘orange’, ‘darkred’,
# ’lightred’, ‘beige’, ‘darkblue’, ‘darkgreen’, ‘cadetblue’, ‘darkpurple’, ‘white’, ‘pink’, 
# ‘lightblue’, ‘lightgreen’, ‘gray’, ‘black’, ‘lightgray’. 
# Je demande de l'ajouter au fond de carte "map"

for i in range(len(lieunaiss)):
    folium.CircleMarker(
        location = (latitudes[i], longitudes[i]),
        radius = salaire[i]/20,
        color = 'crimson',
        fill = True,
        fill_color = 'crimson'
    ).add_to(map1)


# je rajoute une autre couche

lieuvie = ['Strasbourg', 
'Orleans']
latitudes = [48.544698, 47.886479]
longitudes = [7.774603, 1.900981]
revenu = [250, 250] 

for i in range(len(lieuvie)):
    folium.CircleMarker(
        location = (latitudes[i], longitudes[i]),
        radius = revenu[i]/20,
        color = 'cadetblue',
        fill = True,
        fill_color = 'cadetblue'
    ).add_to(map1)
map1







# =============== 3. je réalise une carte avec un csv comme input ==========================


# nouveau fond de carte : 

import folium
coords = (46.539758, 2.430331)
map2 = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

# j'ouvre la bibliothèque permettant d'importer et analyser le csv

import pandas 

# je dis à python d'ouvrir tel csv (j'ai copié le chemin), je lui dis quel est la délimitation, ici ";"
# (le fichier csv est joint dans le répertoire Github, pour le télécharger)
# je mentionne les colonnes du csv que Python devra utiliser, ici "id_oe", "id_a", "nom", "xadresse", "yadresse", "xtitre" et "ytitre"
# j'appelle ce corpus "bdx"

bdx = pandas.read_csv('/Users/leasaint-raymond/Desktop/python/lieutitre.csv', delimiter=";",
                         usecols = ["id_oe", "id_a", "nom", "xadresse", "yadresse", "xtitre", "ytitre"])
        
        
# pour chaque ligne de bdx, Python me place un point 
# dont les coordonnées correspondent à xadresse et à yadresse (l'adresse de l'artiste)
# et dont le diamètre vaut 2
# le popup correspond à la colonne "nom" de l'artiste. 
# attention, toutes les adresses doivent être géolocalisées ! 

for i in range(len(bdx["id_oe"])):
    folium.CircleMarker(
        location = (bdx["xadresse"][i], bdx["yadresse"][i]),
        radius = 2,
        color = 'purple',
        fill = True,
        fill_color = 'purple', 
        popup=str(bdx["nom"][i])
            ).add_to(map2)

map2

# Je peux rajouter une autre série de points, ici le lieu représenté par l'artiste: 
# sa couleur sera bleue et le point sera assez transparent (opacity=0.4)

for i in range(len(bdx["id_oe"])):
    folium.CircleMarker(
        location = (bdx["xtitre"][i], bdx["ytitre"][i]),
        radius = 2,
        color = 'blue',
        fill = True,
        fill_color = 'blue',
        opacity = 0.4 
            ).add_to(map2)
map2

# enfin, je peux relier l'adresse de l'artiste au lieu représenté

for i in range(len(bdx["id_oe"])):
    folium.PolyLine([[bdx["xtitre"][i], bdx["ytitre"][i]], 
                     [bdx["xadresse"][i], bdx["yadresse"][i]]],
                       color='blue', weight=1.5, opacity=0.5).add_to(map2)
map2







# ======================== 4. carte choroplèthe, avec des surfaces ===================

# il faut télécharger un fichier json, avec des surfaces. 

# les arrondissements parisiens en geojson sont disponibles ici : 
# https://opendata.paris.fr/explore/dataset/arrondissements/export/?disjunctive.c_ar&disjunctive.c_arinsee&disjunctive.l_ar&location=13,48.85156,2.32327 

import json
geo = json.load(open("/Users/leasaint-raymond/Desktop/python/arrondissements.geojson.json"))

import folium
paris = folium.Map(location = [48.856578, 2.351828], zoom_start = 12)

folium.GeoJson(geo).add_to(paris)
paris


# autre échelle : la France. 
# les départements, la France sont disponibles ici en geojson : 
# https://github.com/gregoiredavid/france-geojson 

# pour un maillage plus fin, celui des communes : 
# https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/ 

import json
geo2 = json.load(open("/Users/leasaint-raymond/Desktop/python/France_geojson/departements-version-simplifiee.geojson"))

geo2["features"][0]['properties'] # pour savoir ce que le json a dans le ventre

import folium
france = folium.Map(location = [48.856578, 2.351828], zoom_start = 5)
folium.GeoJson(geo2).add_to(france)
france


# pour pimper les contours et le remplissage, par exemple en Maya l'Abeille : 
# et le bord en aquarelle 
import folium
france = folium.Map(location = [48.856578, 2.351828], zoom_start = 5, tiles='stamenwatercolor')
folium.GeoJson(
    geo2,
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5",
    },
).add_to(france)
france


# en vert, tous les départements dont le nom contient la lettre 2
# le nom du département est dans le champ "nom" de mon fichier geojson 
import folium
france = folium.Map([48.856578, 2.351828], zoom_start=4)
folium.GeoJson(
    geo2,
    style_function=lambda feature: {
        "fillColor": "green"
        if "e" in feature["properties"]["nom"].lower()
        else "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5",
    },
).add_to(france)

france


# On peut faire la jointure entre ce fichier geojson et un csv : 
# ici, chaque département est associé à son "nombre d'artistes"
# et le nom du département (colonne "nom" du csv) correspond au "nom" du geojson
# mon fichier s'appelle dttartiste2.csv (disponible dans le répertoire github)

import pandas as pd
df = pd.read_csv('/Users/leasaint-raymond/Desktop/python/dptartiste2.csv', sep=';')

# je regarde mon csv : 
df.head()


import folium

# on importe la couche geojson : 
geo2 = json.load(open("/Users/leasaint-raymond/Desktop/python/France_geojson/departements-version-simplifiee.geojson"))

# on importe le fond de carte, qu'on appelle "france"
france = folium.Map([48.856578, 2.351828], zoom_start=5)

# on crée la carte chroroplèthe, qu'on colle sur "france" : 
folium.Choropleth(
    geo_data=geo2, # le nom de l'environnement du geojson
    data=df, # le nom de l'environnement csv
    columns=['nom', 'nbartistes'], # dans le csv, [le champ d'appariement, la valeur à cartographier]
    key_on='properties.nom', # le nom du département, dans le fichier json, est dans les "properties", colonne "nom"
    fill_color='YlGnBu', 
    fill_opacity=1, 
    line_opacity=1,
    legend_name='nombre d artistes',
    smooth_factor=0).add_to(france)

# on affiche la carte
france

# ========= on peut créer une échelle de couleur et l'ajouter à la carte : 

from branca.colormap import linear

colormap = linear.YlGn_09.scale(
    df.nbartistes.min(), df.nbartistes.max()
)

print(colormap(5.0))

colormap


df_dict = df.set_index("nom")["nbartistes"]
df_dict["Ain"]

import folium

geo2 = json.load(open("/Users/leasaint-raymond/Desktop/python/France_geojson/departements-version-simplifiee.geojson"))

france = folium.Map([48.856578, 2.351828], zoom_start=5)

folium.Choropleth(
    geo_data=geo2, # le nom de l'environnement du geojson
    data=df, # le nom de l'environnement csv
    columns=['nom', 'nbartistes'], # dans le csv, [le champ d'appariement, la valeur à cartographier]
    key_on='properties.nom', # le nom du département, dans le fichier json, est dans les propriétés, colonne "nom"
    legend_name='nombre d artistes',
    style_function=lambda feature: {
        "fillColor": colormap(df_dict[feature["id"]]),
        "color": "black",
        "weight": 1,
        "dashArray": "5, 5",
        "fillOpacity": 0.9,
     },
).add_to(france)

folium.LayerControl().add_to(france)

france




# sources : 

# https://python-visualization.github.io/folium/modules.html
# https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb
# https://python-visualization.github.io/folium/quickstart.html
# https://towardsdatascience.com/choropleth-maps-with-folium-1a5b8bcdd392`
# https://python.doctor/page-apprendre-listes-list-atableaux-tableaux-liste-array-python-cours-debutant 
# https://moncoachdata.com/blog/visualisation-de-donnees-avec-python/
# https://stackoverflow.com/questions/56550313/how-to-plot-routes-between-pairs-of-starting-and-ending-geospatial-points-using







