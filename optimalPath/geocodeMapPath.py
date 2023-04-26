import requests
import json
import folium
import os


def geoCodeMapPath(stoplist):
    url = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"

    querystring = {"stops":stoplist}

    headers = {
        "X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
        "X-RapidAPI-Host": "trueway-directions2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    with open('response.json', 'wb') as outf:
        outf.write(response.content)

