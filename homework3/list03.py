*list1,=map(int,input("enter the list (separator 'space'): ").split())
max = list1[0]

for item in list1:
    if item > max:
        max=item
print(max)