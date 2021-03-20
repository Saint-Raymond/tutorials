# installer les packages 
  install.packages('dplyr')
  install.packages('tipple')
  install.packages('tidygeocoder')

# ouvrir ces packages 
library(dplyr)
library(tibble)
library(tidygeocoder)

# créer un jeu de données avec le nom des individus et, dans une autre colonne, l'adresse :
# il faut donc préparer les données en amont dans un tableur
# en faisant bien attention de présenter ainsi : 
# le nom entre guillemets, séparation virgule, l'adresse entre guillemets et une virgule
# ne pas oublier la tilde pour les entêtes. 
  
exposbordeaux <- tribble(
    ~exposant, ~naissance, 
    "Abba (Maurice)", "Sarlat, France",
    "Abd en Nor", "Alger, Algérie",
    "Abeilhé (Augustin)", "Bordeaux, France",
    "Abougit (Marcel)", "Le Puy, France",
    "Acoquat (Louise-Marie)", "Pontivy, France",
    "Addy (Louis)", "Nérac, France",
    "Alaux (François)", "Bordeaux, France",
    "Alaux (Jean-Paul)", "Bordeaux, France",
    "Albe (Maurice)", "Sarlat, France",
    "Alde (Yvette)", "Paris, France",
    "Anite", "Paris, France",
    "Ansbert (Bertrand-Félix)", "Saint-Seurin de Cadourne, France",
    "Antral (Louis-Robert)", "Châlons-sur-Marne, France",
    "Argouet (Pierre-Albert)", "Lesparre, France",
    "Aries (Nel)", "Bordeaux, France",
    "Arp (Hans)", "Strasbourg, France",
    "Asaf (Halé)", "Constantinople, Turquie",
    "Asselin (Maurice)", "Orléans, France",
    "Aufort (Jean)", "Bordeaux, France",
    "Augonnet (Pierre)", "Farges, France",
    "Augsbourg (Gea)", "Cully, Suisse",
    "Ausquichoury (Fernand-Dominique)", "Guéthary, France",
    "Avinen (Albert-Pierre-Henri)", "Bordeaux, France",
    "Avril (Hélène)", "Montcaret, France",
    "Avril (Raphaël)", "Saint-Médard-de-Guizières, France",
    "Azéma (Louis)", "Castres, France",
    "Bach (Marcel)", "Bordeaux, France",
    "Badie (Jean)", "Bordeaux, France",
    "Bahans (Henriette)", "Bordeaux, France",
    "Balle dit André Marcy (Marcel)", "Baugé, France",
    "Ballet (Fernand)", "Bordeaux, France",
    "Banos (Aristide)", "Maurin, France",
    "Baraduc (Jeanne)", "Riom, France",
    "Barat-Levraud (Georges)", "Blois, France",
    "Barluet (Jean)", "Paris, France",
    "Barral (André)", "Lagarde, France",
    "Barrat (Gabriel)", "Bordeaux, France",
    "Barrère (André-E.)", "Talence, France",
    "Basilis (Germaine-Marie)", "Bordeaux, France",
    "Bassahon (Henri)", "Bordeaux, France",
    "Basse (Henri)", "Paris, France",
    "Bate (Juliette-Jeanne)", "Bordeaux, France",
    "Bauchant (André)", "Chateaurenaud, France",
    "Baude-Couillaud", "Bordeaux, France",
    "Baumeister (Willy)", "Stuttgart, Allemagne",
    "Bayer (Herbert)", "La Haye, Pays-Bas"
    )

# ensuite, il faut géocoder ce jeu de données, nommé "exposbordeaux" : 
# il y a trois méthoges pour géocoder : "osm", "census" et "cascade". 
# Je choisis osm. 
# je dis que le champ qui me servira à géoréférencer s'appelle "naissance" (voir supra)
# j'appelle mon tableau de sortie coordonnees
# attention, quand je fais "run", cela peut prendre du temps de géoréférencer ! 
coordonnees <- exposbordeaux %>%
  geocode(naissance, method = 'osm', lat = latitude , long = longitude)

# enfin, je visualise mon tableau de sorties, avec les coordonnées ! 
view(coordonnees)


#=================== source =======================
#https://jessecambon.github.io/tidygeocoder/
