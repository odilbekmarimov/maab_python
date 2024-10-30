mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}

key1 = input (": ")
if key1 in mydict:
    pair = (key1, mydict[key1])
    print(pair)
else: print("not found")
