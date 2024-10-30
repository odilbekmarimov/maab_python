mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}


key = input("Enter a key: ")

if(key in mydict.keys()):
    mydict.pop(key)
    print(mydict)
else: print("no key found")
    
