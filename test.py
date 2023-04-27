import optimalPath.pathGenerator

stringlist = "East Street , 411001 , Sarasbaug , 411030 , Shaniwar Wada , 411011 , Magarpatta city , 411013"
country = "India"
state = "Maharastra"
city = "Pune"
placeslist, orderstring, orderlist = optimalPath.pathGenerator.pathGenerator(country,state,city,stringlist)
print(placeslist)
print(orderstring)
print(orderlist)