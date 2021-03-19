# sur le terminal, écrire (sans le #) : 

# pip install geopy 
# pip install GeoNames
# pip install geocoder
# jupyter notebook

# si pip ne fonctionne pas, remplacer par pip3

# si vous n'avez pas de jupyter notebook : 
# pip install --user jupyter
# python3 -m notebook

# aller sur le site de GeoNames, s'enregistrer, et en-dessous de GeoNames Change Password, 
# cliquer sur "Click here to enable" (sinon, bugs à répétition garantis !)

import geopy
import geocoder

# avec GeoNames, on peut avoir des informations sur un lieu
# par exemple ici, Roques-sur-Garonne


# avec GeoNames, on peut avoir des informations sur un lieu
# par exemple ici, Roques-sur-Garonne

geo = geocoder.geonames('roques sur garonne', key='MY_USERNAME') # bien mettre son pseudo de geonames ici 

geo.address

geo.geonames_id

geo.description
# je précise que "fourth-order administrative division", c'est faux !
# Roques-sur-Garonne est une métropole de premier ordre !!! 
# la preuve, avec le nombre d'habitants : 

geo.population

# pour donner le lien vers la page wikipédia de cette ville : 
# (écrire sans le #)
#geo.wikipedia 
# il n'y a pas de page wikipedia, pour Roques, et c'est un oubli honteux.






# on peut aussi avoir des informations sur une adresse avec Nominatim : 

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MY_USERNAME") 
# on utilise le même username que pour geonames. 

location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)


# Nominatim permet un géoréférencement à l'envers : des coordonnées vers le lieu. 

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MY_USERNAME")
location = geolocator.reverse("48.842295, 2.3442717")
print(location.address)


# Nominatim permet de géoréférencer des adresses à la louche (dans une limite raisonnable)

import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MY_USERNAME")

monfichier = open('/Users/leasaint-raymond/Desktop/python/mesadressestest.csv')
csv = csv.reader(monfichier, delimiter=',')

# ici, mon csv séparé par des virgules se présente ainsi : 
# colonne 0 : un identifiant
# colonne 1 : la ville
# colonne 2 : le pays

# je vais dire à Python de me regrouper les colonnes 1 et 2 dans un champ "adresse"
# puis de géoréférencer cette adresse
# les coordonnées s'afficheront automatiquement
# attention, dès que le géocodeur n'arrive pas à trouver les coordonnées, le script s'arrête
# Adrien VH utilise des instructions try/except/finally pour régler ce problème
# https://blog.adrienvh.fr/2015/01/18/geocoder-en-masse-plusieurs-milliers-dadresses-avec-python-et-nominatim/

for ligne in csv:
    adresse = ligne[1] + ", " + ligne[2]
    location = geolocator.geocode(adresse)
    print((location.latitude, location.longitude))


# sources : 
# https://medium.com/analytics-vidhya/reverse-geocoding-with-geonames-in-python-3b5bb176a26c
# https://geocoder.readthedocs.io/providers/GeoNames.html 
# https://geopy.readthedocs.io/en/stable/
# https://blog.adrienvh.fr/2015/01/18/geocoder-en-masse-plusieurs-milliers-dadresses-avec-python-et-nominatim/





