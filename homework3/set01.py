set1 = {1,2,2,3} ##removes dublicates itself
set2 = {3,4,5, 5}


RESULT = set1.difference(set2).union(set2.difference(set1))
print(RESULT)

#or
set3 = set1 ^ set2
print(set3)