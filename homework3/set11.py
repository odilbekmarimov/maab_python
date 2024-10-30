set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set() 

v1 = set1.symmetric_difference(set2)

#v2
for item in set1:
    if item not in set2:
        result.add(item)

for item in set2:
    if item not in set1:
        result.add(item)
        
print(v1)
print(result)
