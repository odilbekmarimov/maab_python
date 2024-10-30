main_set = {1,2,3,4,5,6,7}
item = int (input(":"))

if item not in main_set:
    main_set.add(item)
    print("\nsuccess\t", main_set)
else:
    print("item is present")