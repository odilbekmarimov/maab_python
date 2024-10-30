mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}

inverted_dict = {v: k for k, v in mydict.items()}

print (inverted_dict)
