
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}

checkkey = input("checkkey: ")
print(mydict.get(checkkey, "not found"), )