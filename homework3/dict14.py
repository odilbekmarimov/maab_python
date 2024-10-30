mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}

value_to_find = input("enter value to find: ")
keys_with_value = [k for k, v in mydict.items() if v == value_to_find] 
