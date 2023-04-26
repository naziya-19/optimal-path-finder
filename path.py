import requests
import json
import folium
import os


url = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"

querystring = {"stops":"18.5121648, 73.8787887; 18.51938255, 73.85535656171828; 18.500494850000003, 73.85290370572457; 18.5143103, 73.9199827; 18.5121648, 73.8787887																						AX "}

headers = {
	"X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
	"X-RapidAPI-Host": "trueway-directions2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
with open('response.json', 'wb') as outf:
    outf.write(response.content)

