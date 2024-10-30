mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}

value = input ("enter value: ")
count = list(mydict.values()).count(value) 
print(count)