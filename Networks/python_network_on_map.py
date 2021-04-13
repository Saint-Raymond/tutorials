# ===================installing libraries =============================

# on the Terminal, write (without #) : 
# if pip doesn't work, replace by pip3

# pip install holoviz
# pip install geopandas
# pip install geoviews
# pip install leaflet
# pip install folium
# pip install pandas
# jupyter notebook

# if you don't have jupyter notebook : 
# pip install --user jupyter
# python3 -m notebook

# Other method : in jupyter notebook : 
# check that the following modules have been downloaded into jupyter notebook, without the # in front:
# !pip install holoviz
# !pip install geopandas
# !pip install geoviews
# !pip install holoviews
# !pip install leaflet
# !pip install folium

# ===============================2. Visualization ====================================

# create a basemap: 
import folium
coords = (46.539758, 2.430331)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

# open the pandas library and import the csv (it is in the Github repository)

import pandas 

# I tell python to open such csv (I copied the path), I tell it what the delimiter is, here ";"
# I mention the columns of the csv that Python will have to use
# here "id_oe", "id_a", "name", "xaddress", "yaddress", "xtitle" and "ytitle"
# I call this corpus "bdx"

bdx = pandas.read_csv('/Users/leasaint-raymond/Desktop/python/lieutitre.csv', delimiter=";",
        usecols = ["id_oe", "id_a", "nom", "xadresse", "yadresse", "xtitre", "ytitre"])
        
# I plot the nodes that will constitute the node-sources on the basemap: 

# for each line of bdx, Python places a point 
# whose coordinates correspond to xaddress and yaddress (the artist's address)
# and whose diameter is 2
# the popup corresponds to the "name" ("nom) column of the artist. 
# Be careful! All the addresses must be geolocalized ! 

for i in range(len(bdx["id_oe"])):
    folium.CircleMarker(
        location = (bdx["xadresse"][i], bdx["yadresse"][i]),
        radius = 2,
        color = 'purple',
        fill = True,
        fill_color = 'purple', 
        popup=str(bdx["nom"][i])
            ).add_to(map)

# I plot the nodes that will constitute the node-sources on the basemap: 
# here, the represented place whose coordinates are xtitre and ytitle. 

for i in range(len(bdx["id_oe"])):
    folium.CircleMarker(
        location = (bdx["xtitre"][i], bdx["ytitre"][i]),
        radius = 2,
        color = 'blue',
        fill = True,
        fill_color = 'blue',
        opacity = 0.4 
            ).add_to(map)

# Finally, I can connect the address points to the places represented: 

for i in range(len(bdx["id_oe"])):
    folium.PolyLine([[bdx["xtitre"][i], bdx["ytitre"][i]], 
                     [bdx["xadresse"][i], bdx["yadresse"][i]]],
                       color='blue', weight=1.5, opacity=0.5).add_to(map)

map


# sources : 

# https://python-visualization.github.io/folium/modules.html
# https://github.com/python-visualization/folium/blob/master/examples/GeoJSON_and_choropleth.ipynb
# https://python-visualization.github.io/folium/quickstart.html
# https://towardsdatascience.com/choropleth-maps-with-folium-1a5b8bcdd392`
# https://python.doctor/page-apprendre-listes-list-atableaux-tableaux-liste-array-python-cours-debutant 
# https://moncoachdata.com/blog/visualisation-de-donnees-avec-python/
# https://stackoverflow.com/questions/56550313/how-to-plot-routes-between-pairs-of-starting-and-ending-geospatial-points-using

