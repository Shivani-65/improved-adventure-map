import folium
import pandas
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elev=list(data["ELEV"])

def color_producer(elevation):
     if elevation<1000:
          return 'green'
     elif 1000<elevation<=3000:
          return 'darkblue'
     else:
          return 'red'


map = folium.Map(location=[38.58,-99.09], zoom_start=6 )

fgv=folium.FeatureGroup(name="volcanoes")

for lt,ln,nm,el in zip(lat,lon,name,elev):
     fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=8,popup=nm,
     fill_color=color_producer(el),color='red',fill_opacity=0.7))


fgp=folium.FeatureGroup(name="Population")



fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow' if x ['properties']['POP2005']<10000000
                            else 'green' if 10000000<=x ['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")