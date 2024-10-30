from copy import copy

*list1,=map(int,input("enter the list (separator 'space'): ").split())

list2 = copy(list1)

print(list2)