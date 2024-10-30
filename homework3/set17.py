main_set = {1,2,3,4,5,6,7}
odd_set = set()
for item in main_set:
    if item%2 != 0:
        odd_set.add(item)
print(odd_set)