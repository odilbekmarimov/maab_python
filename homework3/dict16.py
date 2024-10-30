mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   key : value
}
has_nested = False
for v in mydict.values():
    if isinstance(v, dict): 
        has_nested = True  
        break  
    
print(has_nested)