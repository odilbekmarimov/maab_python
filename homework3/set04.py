main_set = {1,2,3,4,5,6,7}
sub1_set = {2,3,4}

print("v1")
contains = False 

for element in sub1_set:
    if element in main_set:
        contains = True  
        break 
print(contains)
print("v2")
print(sub1_set<=main_set)