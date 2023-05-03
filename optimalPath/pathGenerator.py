import optimalPath.geoCode2
import optimalPath.distanceMatrix
import optimalPath.matrixMlrose
import optimalPath.TSP
import optimalPath.stringToList
import optimalPath.geocodeMapPath
import optimalPath.jsonToGeojson
import optimalPath.mapping   
import optimalPath.pointMap                                                                                                                                                                                                                                                                                                                                           

#Places,Pincode,City,State,Country

def pathGenerator(Country,State,City,placesString):
    country=Country
    state = State
    city=City
    places, pincodes=optimalPath.stringToList.stringToList(placesString)
    codes, codesList  = optimalPath.geoCode2.geoCode(places,pincodes,city,state,country)

    if len(places) == 1:
        orderList=[[float(codesList[0][0]),float(codesList[0][1])]]
        optimalPath.pointMap.pointMap(orderList,places)
        return "","",""
    
    if len(places) == 2:
        orderstring = str(codesList[0][0])+", "+str(codesList[0][1])+"; " +str(codesList[1][0])+", "+str(codesList[1][1])+"; " + str(codesList[0][0])+", "+str(codesList[0][1])+"; " 
        orderList=[[float(codesList[0][0]),float(codesList[0][1])],[float(codesList[1][0]),float(codesList[1][1])],[float(codesList[0][0]),float(codesList[0][1])]]
        optimalPath.geocodeMapPath.geoCodeMapPath(orderstring)
        optimalPath.jsonToGeojson.jsonToGeojson()
        optimalPath.mapping.mapping(orderList,places)
        return "","",""
    # print(codes)
    # print(codesList)

    dMatrix = optimalPath.distanceMatrix.distanceMatrix(codes)

    # print(dMatrix)

    mlroseMatrix = optimalPath.matrixMlrose.mlroseform(dMatrix)

    n = len(places)
    bestState, bestfitness = optimalPath.TSP.path(mlroseMatrix,n)
    placesList = []
    orderList = []
    orderstring = "" 

    for i in bestState:
        placesList.append(places[i])
        orderList.append([float(codesList[i][0]),float(codesList[i][1])])
        orderstring = orderstring + str(codesList[i][0])+", "+str(codesList[i][1])+"; "

    orderList.append([[float(codesList[0][0]),float(codesList[0][1])]])
    orderstring = orderstring +  str(codesList[0][0])+", "+str(codesList[0][1])+"; " 

    orderstring = orderstring[:(len(orderstring)-2)]

    optimalPath.geocodeMapPath.geoCodeMapPath(orderstring)

    optimalPath.jsonToGeojson.jsonToGeojson()

    optimalPath.mapping.mapping(orderList,placesList)

    return placesList, orderstring, orderList


