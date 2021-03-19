# ouvrir un gazetteer en format texte, avec une ligne = 1 entrée
# ici des noms de lieux

with open('/Users/leasaint-raymond/Desktop/python/NERtitres/lieux_gazetier.txt') as f:
    allKeywords = f.read().lower().split("\n")

print(allKeywords)
print(len(allKeywords))

# importer un fichier csv dans lequel on fera tourner le gazetteer : 
# ici, les titres d'oeuvres exposées
# le titre apparaît en colonne 1 (la colonne 0 : un identifiant)

with open('/Users/leasaint-raymond/Desktop/ExtractingKeywordSets/titres_bdx.csv') as f:
    allTexts = f.read().lower().split("\n")
l = []

for entry in allTexts[1:]:
    l.append(entry.split(';'))
    
# on vérifie que le fichier a bien été transformé en minuscules
print(l[1])

# On apparie le gazetteer avec le fichier csv transformé : 

d = dict()
for key in allKeywords:
    d[key] = []
    for item in l:
        if key in item[1]:
            d[key].append(item)
            
print(d)

# on exporte les sorties dans un fichier csv : 

import pandas as pd
pd.DataFrame.from_dict(data=d, orient='index').to_csv('dict_file.csv', header=False)

import csv 
file =csv.DictReader('dict_file.csv')
print(file)

# Sources 
# le talent de Victor Blanchi (ENS-PSL)
# https://programminghistorian.org/en/lessons/extracting-keywords
# https://atcoordinates.info/tag/gazetteer/
