list1 = list(map(int, input("Enter the list (separator 'space'): ").split()))
unique_list = []

for item in list1:

    if item not in unique_list:
        unique_list.append(item)

print(unique_list)