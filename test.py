import optimalPath.pathGenerator

stringlist = "MG Road , 411003 , Sarasbaug , 411030 , Shaniwar Wada , 411011 , Magarpatta city , 411013"
country = "India"
state = "Maharastra"
city = "Pune"
placeslist, orderstring, orderlist = optimalPath.pathGenerator.pathGenerator(country,state,city,stringlist)
print(placeslist)
print(orderstring)
print(orderlist)