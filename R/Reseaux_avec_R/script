# ========================= 1. Bâtir le réseau =======================================

install.packages("RColorBrewer") 
install.packages("png")
install.packages("ggraph")
install.packages("networkD3")
install.packages("animation")
install.packages("maps")
install.packages("geosphere")

# 
# on nettoie l'espace de travail
rm(list = ls()) 


# On dit à R où sont les fichiers sur lesquels on va travailler :
# il faut copier le chemin du dossier, avec édition => alt : "copier XX en tant que nom de chemin"

setwd("/Users/leasaint-raymond/Desktop/COURS/réseaux R/auctions") 

# j'ouvre ma librairie pour les réseaux
library("igraph")

# je dis quel est le fichier qui décrit les sommets, avec tous les attributs
# comme j'ai défini le dossier, je donne simplement le nom du csv
# et je dis que ce fichier correspond à "nodes". 
# selon le format du csv, on écrit read.csv ou read.csv2
# si l'on saute l'étape setwd, on peut directement copier le chemin complet de chaque fichier à cette étape:
nodes <- read.csv2("./auctionnodes.csv", header=T, as.is=T)
# idem pour les liens, que j'appelle "links" ici. 
links <- read.csv2("./auctionlinks.csv", header=T, as.is=T)
# on peut examiner les données ici : 
head(nodes)
head(links)

# On construit le graphe. Attention, le fichier des liens doit être construit comme ceci : 
# 1 ligne = 1 lien entre les deux sommets qui sont écrits en colonne1 colonne 2. 
# les autres colonnes sont interprétées comme des attributs. 
#ici le réseau est dirigé,  on l'appelle par exemple "net". 

net <- graph_from_data_frame(d=links, vertices=nodes, directed=T) 

# Pour examiner le réseau : 
class(net)
net 
# E(net) correspond aux informations des liens, V(net) à celles des sommets
E(net)
V(net)

# On peut dessiner la matrice d'adjacence, avec un attribut
# ici, dans le fichier auctionlinks, j'avais rajouté un champ "fréquence"
# qui correspondait au nombre de fois où un commissaire-priseur et un expert étaient liés. 
as_edgelist(net, names=T)
as_adjacency_matrix(net, attr="frequence")

#métriques globales  du réseau, que j'ai appelé "net" dans cet exemple. 
gorder(net) # nombre de sommets
gsize(net) # nombre d'arêtes
diameter(net, directed=F) # diamètre du graphe
diameter(net, directed = T, unconnected = TRUE, weights = NULL) # diamètre sans pondération ni orientation)
mean_distance(net) #moyenne des longueurs des chemins
edge_density(net) # densité du graphe
reciprocity(net) # réciprocité pour des graphes dirigés. 


# Pour dessiner le réseau (hyperbrut) : 
plot(net)


# ========================== 2. Visualiser le réseau ==============================

# pour avoir la documentation sur une fonction, il faut l'écrire avec un ? devant :
# ici, on a l'ensemble des fonctionnalités de R, pour la visualisation de réseaux :  
?igraph.plotting
# voir également ici : https://igraph.org/r/doc/plot.common.html
# ou https://igraph.org/r/doc/ 

# on peut calculer des centralités de degré : 
deg <- degree(net, mode="all")

# Partition des noeuds : 
# On peut décider de la couleur des sommets en amont, par exemple colorer tous les noeuds en orange :
vertex_attr(net)$color<-rep("#FF9C0B", length(V(net))) 
# Ou bien faire une partition en fonction de l'attribut "type" qui est dans le fichier des noeuds : 
# ici, tous les noeuds sont orange (voir supra) mais les experts sont en vert et les "marchands en bleu : 
vertex_attr(net)$color[grep(pattern = "expert", vertex_attr(net)$type)]<-"#1C912C"
vertex_attr(net)$color[grep(pattern = "marchand", vertex_attr(net)$type)]<-"blue"

# une fois la partition définie (si on souhaite une partition), on dessine le réseau. 

# Pour cela, on rajoute des arguments dans la commande plot(net)
plot(net,
     layout=layout.fruchterman.reingold(net), #la spatialisation, ici Fruchterman Reingold mais on peut également écrire =layout_in_circle(net) etc
     edge.arrow.size=0, # la taille de la flèche : 0 si pas de flèche
     edge.color="gray80", # la couleur des liens ; ou = rgb(.1, .1, .1, .8) c'est-à-dire (valeur de rouge, valeur de vert, valeur de bleu, transparence)
     # pour ne garder que des labels de noeuds, sans le noeuds, écrire vertex.shape="none"
     edge.width=E(net)$frequence*2, # je fais varier l'épaisseur du lien par rapport à la fréquence, mise à l'échelle ici 
     # pour une épaisseur lien fixe, écrire edge.width=10, par exemple
     edge.curved=0.3, # la courbure des liens entre 0 et 1 : 0 si lignes droites 
     vertex.frame.color=NA,# la couleur de la bordure des sommets : ici NA : pas de bordure. Ecrire ="black" pour une bordure noire.
     vertex.size=deg*10, # cela veut dire que la grosseur du sommet est proportionnelle au degré (échelle x10)
     #pour une grosseur proportionnelle à un attribut quantitatif, comme le salaire, on écrit vertex.size=V(net)$salaire*0.04
     vertex.label=V(net)$individu, 
     # pour donner un attribut à l'étiquette, par exemple la ville, on écrit vertex.label=V(net)$ville 
     # on peut également donner comme attribut le nom "complet" du sommet,
     vertex.label.family="Helvetica", # la police des étiquettes de sommets
     vertex.label.cex=.5, # la taille des étiquettes. Pour une proportionnalité, écrire =V(net)$salaire*0.0004, ici proportionnellement à l'attribut "salaire"
     vertex.label.color="black", # la couleur des étiquettes de sommets.
     main="Réseau des ventes", #titre du réseau
     sub="entre commissaires-priseurs et experts" #sous-titre
) 


# Pour montrer des communautés (analyse structurale de réseau) 
# on fait de "grosses patates" autour des noeuds : 
clp <- cluster_label_prop(net)
class(clp)
plot(clp, net)

# On peut également montrer des communautés en modifiant la couleur des noeuds selon un nombre fixe de classes : 
V(net)$community <- clp$membership
colrs <- adjustcolor( c("gray50", "tomato", "gold", "yellowgreen"), alpha=.6)
plot(net, vertex.color=colrs[V(net)$community])
# ou bien rajouter cette spécification de couleurs dans notre "joli" réseau, en remplaçant l'argument vertex.color
plot(net,
     layout=layout.fruchterman.reingold(net), #la spatialisation, ici Fruchterman Reingold mais on peut également écrire =layout_in_circle(net) etc
     edge.arrow.size=0, # la taille de la flèche : 0 si pas de flèche
     edge.color="gray80", # la couleur des liens ; ou = rgb(.1, .1, .1, .8) c'est-à-dire (valeur de rouge, valeur de vert, valeur de bleu, transparence)
     # pour ne garder que des labels de noeuds, sans le noeuds, écrire vertex.shape="none"
     edge.width=E(net)$frequence*2, # je fais varier l'épaisseur du lien par rapport à la fréquence, mise à l'échelle ici 
     # pour une épaisseur lien fixe, écrire edge.width=10, par exemple
     edge.curved=0.3, # la courbure des liens entre 0 et 1 : 0 si lignes droites 
     vertex.frame.color=NA,# la couleur de la bordure des sommets : ici NA : pas de bordure. Ecrire ="black" pour une bordure noire.
     vertex.size=deg*10, # cela veut dire que la grosseur du sommet est proportionnelle au degré (échelle x10)
     #pour une grosseur proportionnelle à un attribut quantitatif, comme le salaire, on écrit vertex.size=V(net)$salaire*0.04
     vertex.label=V(net)$individu, 
     # pour donner un attribut à l'étiquette, par exemple la ville, on écrit vertex.label=V(net)$ville 
     # on peut également donner comme attribut le nom "complet" du sommet,
     vertex.label.family="Helvetica", # la police des étiquettes de sommets
     vertex.label.cex=.5, # la taille des étiquettes. Pour une proportionnalité, écrire =V(net)$salaire*0.0004, ici proportionnellement à l'attribut "salaire"
     vertex.color=colrs[V(net)$community],
     main="Réseau des ventes", #titre du réseau
     sub="entre commissaires-priseurs et experts" #sous-titre
) 


# Pour finaliser le réseau, on rajoute la légende sur Inkscape.
# aller dans le menu => Plots => Save as Image => en SVG

# pour nettoyer le plan de travail : 
dev.off()

# ================ 3. Coupler un réseau avec une carte ================

# Dans mon fichier csv qui définit les noeuds, j'ai ajouté deux colonnes correspondant aux coordonnées
# c'est-à-dire "latitude" et "longitude". 
# Ces coordonnées sont écrites avec des VIRGULES. 

install.packages('maps') 
install.packages('geosphere')
library('maps') 
library('geosphere')
library("igraph")

# Je dis quels sont les noeuds (ici, officiers : les points de la carte) et les liens (ici : ventes)
# si read.csv2 ne fonctionne pas au moment de la cartographie, essayer read.csv
officiers <- read.csv2("/Users/leasaint-raymond/Desktop/COURS/réseaux R/auctions/auctionnodes.csv", header=TRUE)
ventes <- read.csv2("/Users/leasaint-raymond/Desktop/COURS/réseaux R/auctions/auctionlinks.csv", header=TRUE, as.is=TRUE)


# Je construis le fond de carte
  map(
      "france", 
      # ici, mes données sont françaises donc je choisis un fond de carte français
      # plusieurs fonds sont disponibles (pas tous les pays) : regarder la documentation ?map
      # pour un fond mondial, remplacer "france" par "world", par exemple map("world", col="skyblue",  border="gray10", fill=TRUE, bg="gray30")
      # pour les Etats-Unis, écrire par exemple map("usa", col="tomato",  border="gray10", fill=TRUE, bg="gray30")
      # resp. "italy" pour l'Italie,   map("italy", col="tomato",  border="gray10", fill=TRUE, bg="gray30",lwd=0.6)
      col="grey50", # la couleur du fond de carte, ici gris
      fill=TRUE, 
      border="gray10", # la couleur des frontiières externes et internes
      bg="white", # la couleur de l'arrière plan, ici noir
      # on peut rajouter l'argument lwd=0.6, pour un effet de transparence, entre 0 et 1
      )
 
# J'ajoute les points sur la carte
# Attention à bien construire ses csv. 
# Les noeuds sont dans "officiers" : le csv doit présenter les coordonnées dans 2 colonnes séparées
# les coordonnées doivent être écrites avec des virgules. 
# je dis que mon x correspond à la colonne "longitude" de "officiers" (resp. pour y, "latitude)
# la grosseur du point correspond à cex : ici, je la rends proportionnelle au salaire de l'officier, divisé par 800. 
# si les points ne s'affichent pas, remplacer read.csv par read.csv2 ou inversement
points(x=officiers$longitude, y=officiers$latitude, pch=19, 
       cex=officiers$salaire/800, col="orange")

#On peut modifier des couleurs ici : 
col.1 <- adjustcolor("orange red", alpha=0.4)
col.2 <- adjustcolor("orange", alpha=0.4)
edge.pal <- colorRampPalette(c(col.1, col.2), alpha = TRUE) 
edge.col <- edge.pal(100)

# Pour calquer le réseau sur la carte, il faut tracer des arcs en disant quelle est le noeud-source et le noeud-destination.
  for(i in 1:nrow(ventes))  {
    node1 <- officiers[officiers$individu == ventes[i,]$cp,] 
    #la source est ma colonne "cp" dans le fichier des liens (ici, ventes)
    # elle correspond au champ "individu" dans le fichier des noeuds (ici, officiers)
    node2 <- officiers[officiers$individu == ventes[i,]$expert,]
    #la destination est ma colonne "expert" dans le fichier des liens (ici, ventes)
    # elle correspond au champ "individu" dans le fichier des noeuds (ici, officiers)
    arc <- gcIntermediate( c(node1[1,]$longitude, node1[1,]$latitude), 
                           c(node2[1,]$longitude, node2[1,]$latitude), 
                           n=1000,
                           addStartEnd=TRUE )
    edge.ind <- round(100*ventes[i,]$frequence / max(ventes$frequence) 
                      #variable quantitative pour l'épaisseur des liens
                      # calculée à partir du champ "fréquence" de mon fichier de liens (ici, ventes)
                      )
    
    lines(arc, col=edge.col[edge.ind], lwd=edge.ind/30)
  }


# ==================================================================================
# sources : 
# https://rstudio-pubs-static.s3.amazonaws.com/337696_c6b008e0766e46bebf1401bea67f7b10.html 
# Sébastien Plutniak. L’analyse de graphes avec R : un aperçu avec igraph. École thématique Analyse de réseaux et complexité, Sep 2018, Cargèse, France. hal-01885485
# www.kateto.net/sunbelt2019  (adapté au cas français)

