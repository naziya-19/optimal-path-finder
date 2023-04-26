import optimalPath.geoCode2
import optimalPath.distanceMatrix
import optimalPath.matrixMlrose
import optimalPath.TSP

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

dMatrix = [[0, 6481, 4909], [5188, 0, 7105], [4335, 7052, 0]]

mlroseMatrix = optimalPath.matrixMlrose.mlroseform(dMatrix)

print(mlroseMatrix)
n = 3
places = ['MG Road', 'Kondhwa', 'Sarasbaug']
codes = "18.5121648, 73.8787887; 18.4712065, 73.8890164; 18.500494850000003, 73.85290370572457"
codesList = [['18.5121648', '73.8787887'], ['18.4712065', '73.8890164'], ['18.500494850000003', '73.85290370572457']]

bestState, bestfitness = optimalPath.TSP.path(mlroseMatrix,n)

print(bestState)
orderlist = str(codesList[0][0])+", "+str(codesList[0][1])+"; "
for i in bestState:
    print(places[i])
    orderlist = orderlist + str(codesList[i][0])+", "+str(codesList[i][1])+"; "

orderlist = orderlist[:(len(orderlist)-2)]

print(orderlist)
print(bestfitness)


