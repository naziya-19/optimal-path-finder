
def stringToList(str):
# str = "MG Road , 411003 , Sarasbaug , 411067 , Shaniwar Wada , 411008 , Magarpatta , 411098"
    places = []
    pin = []
    l = [i.strip() for i in str.split(',') ]
    for i in range(0,len(l),2):
        places.append(l[i])
        pin.append(l[i+1])
    
    return places,pin
    