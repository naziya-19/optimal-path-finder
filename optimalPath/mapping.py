import json 

input_file=json.load(open("./response.json", "r", encoding="utf-8"))

l = input_file["route"]["geometry"]["coordinates"]
for i in range(len(l)):
    l[i][0], l[i][1] = l[i][1], l[i][0]
geojs={
     "type": "FeatureCollection",
     "features":[
           {
                "type":"Feature",
                "properties":{},
                "geometry": {
                "coordinates":l,
                "type":"LineString",
            }
         }
    ]  
 }

# Serializing json
json_object = json.dumps(geojs, indent=4)
 
# Writing to sample.json
with open("geodata.json", "w") as outfile:
    outfile.write(json_object)

