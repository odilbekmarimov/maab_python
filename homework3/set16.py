main_set = {1,2,3,4,5,6,7}
even_set = set()
for item in main_set:
    if item%2 == 0:
        even_set.add(item)
print(even_set)