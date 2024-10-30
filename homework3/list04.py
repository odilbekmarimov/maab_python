*list1,=map(int,input("enter the list (separator 'space'): ").split())
min = list1[0]

for item in list1:
    if item < min:
        min=item
print(min)