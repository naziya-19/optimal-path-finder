import folium
import os

def mapping(Points,Orderlist,Orderplaces):

    points = Points
    orderlist = Orderlist
    orderplaces = Orderplaces

    map = folium.Map(location=orderlist[0], zoom_start=15)

    walkdata = os.path.join('geodata.json')
    folium.GeoJson(walkdata,smooth_factor=0.5).add_to(map)

    for i in range(len(orderlist) - 1):
        folium.Marker(orderlist[i], popup=orderplaces[i]).add_to(map)

    map.save("./templates/map.html")