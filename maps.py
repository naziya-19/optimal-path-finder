import folium
import os

points = "18.5121648, 73.8787887; 18.51938255, 73.85535656171828; 18.500494850000003, 73.85290370572457; 18.5143103, 73.9199827"
orderlist = [[18.5121648, 73.8787887], [18.51938255, 73.85535656171828], [18.500494850000003, 73.85290370572457], [18.5143103, 73.9199827]]
orderplaces = ['MG Road', 'Shaniwar Wada', 'Sarasbaug', 'Magarpatta city']

map = folium.Map(location=orderlist[0], zoom_start=15)

walkdata = os.path.join('geodata.json')
folium.GeoJson(walkdata,smooth_factor=0.5).add_to(map)

for i in range(len(orderlist)):
    if i == 0:
            folium.Marker(orderlist[i], popup=(str(i+1)+". "+orderplaces[i]), icon=folium.Icon(icon='1',prefix='fa', color='red')).add_to(map)
            continue;
    folium.Marker(orderlist[i], popup=(str(i+1)+". "+orderplaces[i]), icon=folium.Icon(icon=str(i + 1),prefix='fa', color='cadetblue')).add_to(map)


map.save("index.html")