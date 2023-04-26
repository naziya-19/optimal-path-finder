import asyncio
import http.client, urllib.parse
import json
import time

def gh(Places,City,State):
    conn = http.client.HTTPConnection('api.positionstack.com')

    Codes=""
    

    for i in range(len(Places)):
        
        params = urllib.parse.urlencode({
            'access_key': 'f7a30777205b862cb0dfe067ba2edd86',
            'query': [Places[i]+" "+City,],
            'region': State,
            'limit': 1,
            },
            )

        conn.request('GET', '/v1/forward?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        d = json.loads(data.decode())["data"]
        latitude=d[0]["latitude"]
        longitude = d[0]["longitude"]
        Codes = Codes + str(latitude)+", "+str(longitude)+"; "

        print(data.decode('utf-8'))
        print(latitude)
        print(longitude)

    print(Codes[0:(len(Codes)-2)])
    Codes = Codes[0:(len(Codes)-2)]
    return Codes

state = "Maharastra"
city = "Pune"
#Places = ["MG Road","Empress Botanical Garden","Sarasbaug","Shaniwar Wada"]
places = ["East Street", "Empress Botanical Garden"]


