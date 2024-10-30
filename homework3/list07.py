*list1,=map(int,input("enter the list (separator 'space'): ").split())

if len(list1)>0:
    print(f"last element is: {list1[len(list1)-1]}")
else:
    print("list is empty")