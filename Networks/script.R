# ========================= 1. Building the network =======================================

install.packages("RColorBrewer") 
install.packages("png")
install.packages("ggraph")
install.packages("networkD3")
install.packages("animation")
install.packages("maps")
install.packages("geosphere")

# 
# clean the workspace
rm(list = ls()) 


# Tell R where the files you are going to work on are:
# you need to copy the path of the folder, with edit => alt: "copy XX as pathname"

setwd("/Users/leasaint-raymond/Documents/GitHub/tutorials/Networks") 

# open the R-library related to for networks
library("igraph")

# tell what is the file that describes the vertices, with all their attributes
# as you already defined the folder, you simply give the name of the csv
# and you tell that this file corresponds to "nodes". 
# but if you skipped the setwd step, you can directly copy the full path of each file at this step.
# Depending on the format of the csv, the command line is read.csv or read.csv2
nodes <- read.csv2("./auctionnodes.csv", header=T, as.is=T)

# Do the same for the links file, that we call "links", here:. 
links <- read.csv2("./auctionlinks.csv", header=T, as.is=T)

# you can examine the data here (and check that the files have been imported)
head(nodes)
head(links)

# Let's build the graph.
# The file of the links must be built like this: 
# 1 row = 1 link between the two vertices which are written in column1 column 2. 
# the other columns are interpreted as attributes. 
# here the network is directed, we call it for example "net"
net <- graph_from_data_frame(d=links, vertices=nodes, directed=T) 


# ========================== 2. Statistics and Metrics ==============================

class(net)
# E(net) corresponds to the information of the links, V(net) to those of the vertices
E(net)
V(net)

# We can draw the adjacency matrix, with an attribute
# here, in the auctionlinks file, I had added a "frequency" field
# which corresponded to the number of times an auctioneer and an expert were linked.  
as_edgelist(net, names=T)
as_adjacency_matrix(net, attr="frequency")

# Here are some global network metrics of our network (called "net", here)
gorder(net) # number of vertices
gsize(net) # number of edges
# diameter of the graph (maximum distance between two vertices): 
diameter(net, directed = T, unconnected = TRUE, weights = NULL) 
mean_distance(net) # average path length
edge_density(net) # graph density
reciprocity(net) # reciprocity for directed graphs.. 


# ========================== 3. Network Visualization ==============================

# Let's draw our (raw!) network:
plot(net)

# If you want to get the documentation on a function, you can write it with a ? at the beginning:
# here, you get all the functionalities of R, for the visualization of networks:  
?igraph.plotting
# see also here : https://igraph.org/r/doc/plot.common.html
# or https://igraph.org/r/doc/ 

# Here, you compute degree centralities: 
deg <- degree(net, mode="all")

# Partition of nodes: 
# You can decide the color of the vertices, for example color all the nodes in orange
vertex_attr(net)$color<-rep("#FF9C0B", length(V(net))) 
# You can also make a partition according to the "type" attribute which is in the nodes file: 
# here, all the nodes are orange (see above) but the experts are in green and the dealers in blue
vertex_attr(net)$color[grep(pattern = "expert", vertex_attr(net)$type)]<-"#1C912C"
vertex_attr(net)$color[grep(pattern = "dealer", vertex_attr(net)$type)]<-"blue"

# Once the partition is defined (if you want a partition), let's draw the network. 

# To do so, you will add arguments to the plot command: 
plot(net,
     
     #choose your spatialization, here Fruchterman Reingold 
     # but you can also write =layout_in_circle(net) 
     layout=layout.fruchterman.reingold(net), 
     
     edge.arrow.size=0, # the size of the arrow : 0 if no arrow
     
     # Now, choose the color of the edges:
     edge.color="gray80", 
     # or write = rgb(.1, .1, .1, .8) i.e. (red value, green value, blue value, transparency)
     # If you want to keep only node labels, write vertex.shape="none
     
     # Now, choose the thickness of the link:
     # here, the size of the edge depends on the "frequency", with a scale
     # but you can also set a fixed size, e.g. edge.width=10
     edge.width=E(net)$frequency*2, 
     
     edge.curved=0.3, # the curvature of the links between 0 and 1 (0 if straight lines) 
     
     # Now, choose the color of the border of the vertices : here NA means no border. 
     # but you can also write "black" for a black border. 
     vertex.frame.color=NA,
     
     # Now, choose the size of the vertices. 
     # Here, size of the vertex is proportional to the centrality degree (see above), with a scale x10
     # If you want to set a size proportional to a quantitative attribute, like the "wage" in this example,
     # you write vertex.size=V(net)$wage*0.04
     vertex.size=deg*10,
     
     # Now, you set the labels of your vertices. 
     # Here, I choose the "name" attribute of my nodes, 
     # but I can also choose the "city" and write vertex.label=V(net)$city 
     vertex.label=V(net)$name, 
     
     vertex.label.family="Helvetica", # the font of the labels for the vertices
     
     # Choose the size of the labels. 
     # For proportionality to an attribute, e.g. "wage", write =V(net)$wage*0.0004
     vertex.label.cex=.5, 
     
     vertex.label.color="black", # the color of the labels for the vertices
     
     main="Network of the auction sales", #title of your network
     sub="in Paris, linking auctioneers and experts" #subtitle
) 


# To show communities (structural network analysis) 
# you can draw "big potatoes" around the nodes:
clp <- cluster_label_prop(net)
class(clp)
plot(clp, net)

#  You can also show communities by changing the color of the nodes, 
# according to a fixed number of classes:
V(net)$community <- clp$membership
colrs <- adjustcolor( c("gray50", "tomato", "gold", "yellowgreen"), alpha=.6)
plot(net, vertex.color=colrs[V(net)$community])

# or add this color specification in our "nice" network, by replacing the vertex.color argument
plot(net,
     layout=layout.fruchterman.reingold(net), 
     edge.arrow.size=0, #
     edge.color="gray80",
     edge.width=E(net)$frequency*2, 
     edge.curved=0.3, 
     vertex.frame.color=NA,
     vertex.size=deg*10, 
     vertex.label=V(net)$name, 
     vertex.label.family="Helvetica", 
     vertex.label.cex=.5, 
     vertex.color=colrs[V(net)$community], # here is the change!
     main="Réseau des ventes", 
     sub="entre commissaires-priseurs et experts"
) 


# To finalize the network, you can add the legend on Inkscape.
# Go to Plots => Save as Image => in SVG

# Let's clean up the workspace : 
dev.off()

# ================ 4. Matching a network and a map ===============================

install.packages('maps') 
install.packages('geosphere')
library('maps') 
library('geosphere')
library("igraph")


# In the csv file that defines the nodes, you can added two columns corresponding to the coordinates
# here, the columns "latitude" and "longitude" of the auctionnodes.csv file. 
# These coordinates are written with commas.

# I keep the same example (see step 1 for the files) for the nodes and links. 


# Let's build the basemap:
  map(
      "france", 
      # here, my data are French so I choose a French basemap
      # several basemaps are available (but not all countries): 
      # check the ?map documentation. 
      # For a world basemap, replace "france" by "world",
      # For the USA, eplace "france" by "usa", resp. "italy" for Italy. 
      
      col="white", # the color of the basemap, here white. Or col="skyblue" or col="tomato"
      fill=TRUE, 
      
      border="gray10", # the color of the external and internal borders
      
      bg="white", #the color of the background, here white. 
      # we can add the argument lwd=0.6, for a transparency effect, between 0 and 1 
      )
 
  
# Now, you need to add the points on the basemap (here, the nodes of the network)
# Be careful when you build your csv: 
# the csv of the nodes must present the coordinates in 2 separate columns, written with commas. 
# Here, you say that your x correspond to the "longitude" columns of the node file
# resp. y for the latitude. 
# the size of the point corresponds to cex: here, I make it proportional to the wage, divided by 800. 
# if the points are not displayed, replace read.csv by read.csv2 or inversely
points(x=nodes$longitude, y=nodes$latitude, pch=19, 
       cex=nodes$wage/800, col="orange")

# You can change colors here, for the links:
col.1 <- adjustcolor("orange red", alpha=0.4)
col.2 <- adjustcolor("orange", alpha=0.4)
edge.pal <- colorRampPalette(c(col.1, col.2), alpha = TRUE) 
edge.col <- edge.pal(100)

# To trace the network on the map, it is necessary to draw arcs 
# saying which is the source-node and the destination-node.
# Here, the sources are the nodes whose "name" is "auctioneer" (see the csv file)
# and the destinations, the nodes whose "name" is "expert". 
  for(i in 1:nrow(links))  {
    node1 <- nodes[nodes$name == links[i,]$auctioneer,] 
    node2 <- nodes[nodes$name == links[i,]$expert,]
    # now, I tell R where are the coordinates.
    arc <- gcIntermediate( c(node1[1,]$longitude, node1[1,]$latitude), 
                           c(node2[1,]$longitude, node2[1,]$latitude), 
                           n=1000,
                           addStartEnd=TRUE )
    edge.ind <- round(100*links[i,]$frequency / max(links$frequency) 
                      #finally, I set the size of the edge / arc
                      # here, the field "frequency" of the links file. 
                      )
    lines(arc, col=edge.col[edge.ind], lwd=edge.ind/30)
  }


# ==================================================================================
# sources : 
# https://rstudio-pubs-static.s3.amazonaws.com/337696_c6b008e0766e46bebf1401bea67f7b10.html 
# Sébastien Plutniak. L’analyse de graphes avec R : un aperçu avec igraph. École thématique Analyse de réseaux et complexité, Sep 2018, Cargèse, France. hal-01885485
# www.kateto.net/sunbelt2019  (adapté au cas français)

