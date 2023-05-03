import optimalPath.geoCode2
import optimalPath.distanceMatrix
import optimalPath.matrixMlrose
import optimalPath.TSP
import optimalPath.stringToList
import optimalPath.pathGenerator

#Places,Pincode,City,State,Country

# country=input("Enter the country: ")
# state = input("Enter State:")
# city=input("Enter City: ")
# n = int(input("Enter the number of places: "))
# places=[]
# pincodes=[]
# for i in range(n):
#     places.append(input("Place: "))
#     pincodes.append(input("Pincode: "))

# print(places)
# print(pincodes)

# codes, codesList  = optimalPath.geoCode2.geoCode(places,pincodes,city,state,country)

# print(codes)
# print(codesList)

# dMatrix = optimalPath.distanceMatrix.distanceMatrix(codes)

# print(dMatrix)

stringlist = "Kondhwa , 411048"
country = "India"
state = "Maharastra"
city = "Pune"
# places, pincodes=optimalPath.stringToList.stringToList(stringlist)
# print(places," ",pincodes)

# print(optimalPath.geoCode2.geoCode(["Kondhwa"],['411048'],city,state,country))
# places, pincodes=optimalPath.stringToList.stringToList(stringlist)

optimalPath.pathGenerator.pathGenerator(country,state,city,stringlist)

