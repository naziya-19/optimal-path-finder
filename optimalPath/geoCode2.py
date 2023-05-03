import json
import requests

def geoCode(Places,Pincode,City,State,Country):
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

    Codes=""
    CodesList=[]
    for i in range(len(Places)):
        querystring = {"street":Places[i],"city":City,"state":State,"postalcode":Pincode[i],"country":Country,"accept-language":"en","polygon_threshold":"0.0"}

        headers = {
            "X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
            "X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)[0]
        longitude = data['lon']
        latitude = data['lat']
        Codes = Codes + str(latitude)+", "+str(longitude)+"; "
        CodesList.append([latitude,longitude])

    Codes = Codes[0:(len(Codes)-2)]
    return Codes, CodesList
