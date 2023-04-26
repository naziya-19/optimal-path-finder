import requests
import json

def distanceMatrix(geocode):

    url = "https://trueway-matrix.p.rapidapi.com/CalculateDrivingMatrix"

    querystring = {"origins":geocode,"destinations":geocode}

    headers = {
        "X-RapidAPI-Key": "3895d9df0emsh46c2c3432d53568p1aae92jsnc1e99f7596f7",
        "X-RapidAPI-Host": "trueway-matrix.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    distancematrix = json.loads(response.text)['distances']
    return distancematrix