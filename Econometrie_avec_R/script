# installer les packages suivants : 
install.packages("DAAG")
install.packages("plm")

#================== 1. Econométrie simple sous R ================================


# préparer les données :
# Les nombres doivent être écrits avec des virgules, pas des points. 
# corpus utilisé ici : ventes aux enchères publiques d'objets provenant du Palais d'Eté
# disponible ici : https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0COI5J
# mais transformé avec des virgules (j'ai mis le fichier dans le dossier de ce répertoire)

library (DAAG)

#on importe le csv, ici testasie.csv, en sélectionnant le chemin dans Edition=> maintenir alt => copier en tant que nom de chemin
# si read.csv2 ne fonctionne pas, essayer read.csv
# on peut également passer, sur R, par Environnement => import Dataset
asie <- read.csv2("/Users/leasaint-raymond/Desktop/auctionsasie.csv", header=T, as.is=T)

# pour visualiser les données (attention : View avec majuscule)
View(asie)

# code pour une régression linéaire : 
# je donne un nom à ma régression, par exemple regression1
# dans la formule suivante : regression1<-lm(y ~ x1 + x2 , data=mesdonnees)
# y = la variable à expliquer : ici, je remplace par le prix d'adjudication noté "prix"
# x1, x2 etc : les variables explicatives : ici, "palaisete", "datation", "chine", "broner", "ancien", "nbcaracteres"
regression1<-lm(prix 
                ~ 
                  palaisete + 
                  datation + 
                  chine +
                  bronze +
                  porcelaine +
                  ancien +
                  nbcaracteres, 
                                data=asie)
# enfin, je visualise le tableau de sortie : 
summary(regression1)

# Le tableau de sortie apparaît dans la console : 

# d'abord une description des résidus (minimum, maximum, 1e, 2e et 3e quartiles)
#Residuals:
#    Min      1Q  Median      3Q     Max 
#-2216.0  -162.6   -48.2    62.6 14005.3 


#ensuite le tableau de régression : 
# estimate : le coefficient de régression
# Std. Error : l'écart-type : 
# si celui-ci est "petit" par rapport au coefficient, alors le coefficient est "significatif"
# pour le tester, on regarde la p-value : si Pr(>|t|) est très petit, alors le coefficient est significatif
# on résume la significativité avec des étoiles : 
# *** = significatif à 99,9%
# ** = significatif à 99%
# * : significatif entre 99 et 99%

#Coefficients:
#              Estimate Std. Error t value Pr(>|t|)    
#(Intercept)   -92.6812    16.8271  -5.508 3.78e-08 ***
#palaisete      -2.0099    26.6191  -0.076  0.93982    
#datation       49.4130    57.9966   0.852  0.39425    
#chine          48.2950    16.8869   2.860  0.00425 ** 
#bronze       -158.6022    25.4448  -6.233 4.88e-10 ***
#porcelaine   -117.2871    16.6612  -7.040 2.15e-12 ***
#ancien        -24.4391    25.7465  -0.949  0.34255    
#nbcaracteres    3.3136     0.1038  31.935  < 2e-16 ***
---
#Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

#Residual standard error: 562.3 on 5945 degrees of freedom
#  (1 observation deleted due to missingness)
#Multiple R-squared:  0.1649,	Adjusted R-squared:  0.1639 
#F-statistic: 167.7 on 7 and 5945 DF,  p-value: < 2.2e-16




#===================== 2. Econométrie plus avancée ===============================
  
library(plm)

# on peut transformer une variable en autant de variables indicatrices (dummy variables)
# par exemple, il y aura autant de variables indicatrices que d'individus différents. 
# ici, je vais ventiler la variable "lugt" en autant de variables indicatrices.
# Lugt correspond aux catalogues de vente (un identifiant = un catalogue)
# donc je vais créer autant de variables indicatrices qu'il y a de catalogues de vente dans mon corpus. 
# Dans la formule, j'écris donc factor(lugt)
# j'appelle "regression2" mon deuxième modèle. 
regression2<-lm(prix ~ nbcaracteres + bronze + palaisete + datation + factor(lugt), data=asie)
summary(regression2)


# On peut réaliser une régression avec des effets fixes (ici, un effet-fixe catalogue)
# comme si on réalisait chaque régression à l'intérieur d'un même catalogue. 
# on interprète les coefficients "toutes choses par ailleurs et pour un catalogue donné". 
# Concrètement, dans le code, on utilise la fonction "plm" au lieu de "lm"
# et on indique par index=c("variable") la variable qui va servir d'effet fixe, ici "lugt"
regression3<-plm(prix~nbcaracteres + bronze + palaisete + datation, index=c("lugt"),model="within",data=asie)
summary(regression3)


#============= sources =====================
# https://rstudio-pubs-static.s3.amazonaws.com/372492_3e05f38dd3f248e89cdedd317d603b9a.html
# http://olivier.godechot.free.fr/hopfichiers/Econometrie_panels.pdf

