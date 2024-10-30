tuple1 = (5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0)

list1 = []

for item in tuple1:
    if item not in list1:
        list1.append (item)


tuple2 = tuple(list1)

print(tuple2)
