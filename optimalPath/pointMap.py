import folium 
import os

def pointMap(Orderlist,Orderplaces):
    orderlist = Orderlist
    orderplaces = Orderplaces
    map = folium.Map(location=orderlist[0], zoom_start=17)
    folium.Marker(orderlist[0], popup=(str(1)+". "+orderplaces[0]), icon=folium.Icon(icon='1',prefix='fa', color='red')).add_to(map)
    map.save("./templates/map.html")