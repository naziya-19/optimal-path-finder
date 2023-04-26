import json
import requests

url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

querystring = {"street":"Undri Chowk","city":"Pune","state":"Maharastra","postalcode":"411060","country":"India","accept-language":"en","polygon_threshold":"0.0"}

headers = {
	"X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
	"X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
data = json.loads(response.text)[0]
longitude = data['lon']
latitude = data['lat']
print(str(longitude) + " "+str(latitude))