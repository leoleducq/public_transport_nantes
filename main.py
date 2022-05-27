import folium #Bibliotheque pour la carte
import pandas as pd #Bibliotheque pour le CSV des arrêts de bus
from random import randint #Pour générer des couleurs aléatoires
m = folium.Map(location=[47.218371,-1.553621], zoom_start=11) #Objet folium localisation Nantes
df_stop = pd.read_csv("txt/stops.txt", sep=",",header=0) #Récupère les données des arrêts
df_lines = pd.read_csv("txt/shapes.txt", sep=",",header=0) #Récupère les données des lignes
#Tracé des lignes sur la map
df_shapes_id = list(df_lines.iloc[:,0].unique()) #Enlève les doublons des lignes
for i in range(len(df_shapes_id)):
  colors = '#%06X' % randint(0, 0xFFFFFF)#Couleurs aléatoires
  df_filter = df_lines[df_lines['shape_id'] == df_shapes_id[i]] #Filtre sur le nom de shape_id
  line = [(df_filter.iloc[i,1], df_filter.iloc[i,2]) for i in range(len(df_filter))] #Ajout des coordonnées des lignes dans la liste
  folium.PolyLine(line,color=colors,weight=2.5, opacity=1).add_to(m)
#Tracé des arrêts sur la map
stop = df_stop.drop_duplicates(subset=['stop_name']) #Enlève les doublons des arrêts
for i in range(0,len(stop)):
  folium.Marker(
    location=[stop.iloc[i]['stop_lat'], stop.iloc[i]['stop_lon']],
    popup=stop.iloc[i]['stop_name']
    ).add_to(m)
#Sauvegarder la map
m.save("index.html")