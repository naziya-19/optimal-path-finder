import folium
import os

def mapping(Orderlist,Orderplaces):

    orderlist = Orderlist
    orderplaces = Orderplaces

    map = folium.Map(location=orderlist[0], zoom_start=15)

    walkdata = os.path.join('geodata.json')
    folium.GeoJson(walkdata,smooth_factor=0.5).add_to(map)

    for i in range(len(orderlist) - 1):
        if i == 0:
            folium.Marker(orderlist[i], popup=(str(i+1)+". "+orderplaces[i]), icon=folium.Icon(icon='1',prefix='fa', color='red')).add_to(map)
            continue;
        folium.Marker(orderlist[i], popup=(str(i+1)+". "+orderplaces[i]), icon=folium.Icon(icon=str(i + 1),prefix='fa', color='green')).add_to(map)

    map.save("./templates/map.html")