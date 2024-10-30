mydict = {
    "brand": "Ford",
    "model": "Mustang"
}

dict1 = {
    "model": "Civic",
    "year": 2020
}

common_keys = set()
for key in mydict.keys():
    if key in dict1: 
        common_keys.add(key)
print(common_keys)
