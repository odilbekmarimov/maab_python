*list1,=map(int,input("enter the list (separator 'space'): ").split())

sum = 0
for item in list1:
    sum += item
    
print(sum)