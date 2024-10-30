mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


firstval = None

for key, value in mydict.items():
    firstval = (key, value)  
    break  


print(firstval )