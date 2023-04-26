import json
import requests

url = "https://trueway-matrix.p.rapidapi.com/CalculateDrivingMatrix"

querystring = {"origins":"18.471564, 73.894519;18.476708, 73.896847;18.485499, 73.888876;18.498109, 73.899828","destinations":"18.471564, 73.894519;18.476708, 73.896847;18.485499, 73.888876;18.498109, 73.899828"}

headers = {
	"X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
	"X-RapidAPI-Host": "trueway-matrix.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
distancematrix = json.loads(response.text)['distances']
print(distancematrix)