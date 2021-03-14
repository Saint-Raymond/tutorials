# Analyses de correspondances multiples sous R

#installer les packages suivants : 
install.packages(c("FactoMineR", "factoextra"))

#ouvrir les packages : 
library(FactoMineR)
library(factoextra)

# bâtir le csv de la manière la plus simple et synthétique possible
# En lignes, les individus ou les classes d'individus
# En colonnes, les variables qui nous intéressent pour "tirer" la distribution. 
# Il est important que les valeurs soient des numériques, et non des chaînes de caractères. 
# attention, pas de cellule vide : remplacer par zéro. 

# Un exemple dans le dossier Github, "annuaires.csv" : il résume l'annuaire des collectionneurs de 1925
# source : https://gallica.bnf.fr/ark:/12148/bpt6k432842p
# J'ai regroupé les objets collectionnés par grandes catégories (en ligne)
# Puis j'ai regardé quelles étaient les catégories sociales qui collectionnaient ces catégories d'objets,
# quelle était la distribution selon le genre et selon quelle la répartition géographique.


# pour importer les données, il est important de le faire dans l'Environnement, en haut à droite : 
# import dataset => From Text => sélectionner le csv => Row names => sélectionner "Use first column"
# mon fichier csv s'appelle annuaires : 

# on calcule ensuite l'ACM, que je nomme resultat1
# ici, toutes les variables comptent : 
resultat1 <- CA (annuaires, graph = FALSE)

# pour avoir le résultat chiffré : 
print(resultat1)
summary(resultat1)

# Je peux décider de diviser les variables  : garder celles qui comptent pour l'ACM et 
# projeter des variables supplémentaires sur le diagramme (qui ne comptent donc pas). 
# pour cela, je bâtis les csv en mettant les variables supplémentaires à la fin, à droite.
# On calcule la place des colonnes dans le csv. 
# dans mon csv, je garde les colonnes 1 à 10 et je considère les colonnes 11 à 17 comme variables supplémentaires : 
# J'appelle cette ACM "resultat2"
resultat2 <- CA (annuaires, col.sup = 11:17, graph = FALSE)
print(resultat2)
summary(resultat2)

# Pour visualiser l'ACM : 
fviz_ca_biplot (resultat1, repel = TRUE)
# ou, avec les variables supplémentaires, qui apparaissent dans une autre couleur : 
fviz_ca_biplot (resultat2, repel = TRUE)

# un résumé graphique : 
# les couleurs les plus chaudes sont celles qui contribuent le plus aux axes. 
fviz_ca_col (resultat1, col.col = "cos2", gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"), repel = TRUE)

# quelques calculs : le chi-2 : 
chisq <- chisq.test (annuaires)
chisq
## il faut retenir le nombre qui apparaît après X-squared : par exemple ici 1377.2
## puis on calcule les degrés de liberté, et la p-value
chi2 <- 1377.2
df <- (nrow (annuaires) - 1) * (ncol (annuaires) - 1)
pval <- pchisq (chi2, df = df, lower.tail = FALSE)
pval
# on obtient le tableau avec la quantité d’informations retenue par chaque axe. 
# calcul des valeurs propres : 
eig.val <- get_eigenvalue(resultat1)
eig.val


# =========== sources ============
# http://factominer.free.fr/factomethods/multiple-factor-analysis.html 
# http://www.sthda.com/french/articles/38-methodes-des-composantes-principales-dans-r-guide-pratique/77-afm-analyse-factorielle-multiple-avec-r-l-essentiel/
# http://www.sthda.com/french/articles/38-methodes-des-composantes-principales-dans-r-guide-pratique/74-afc-analyse-factorielle-des-correspondances-avec-r-l-essentiel/

