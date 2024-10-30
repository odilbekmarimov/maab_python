mydict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}
mydict1 = {
  "brand1": "Ford1",
  "model1": "Mustang1",
  "year1": 1964
#   key : value
}

mydict3 ={ **mydict2, **mydict1}

print(mydict3)