*list1,=map(int,input("enter the list (separator 'space'): ").split())

if len(list1)>0:
    print(f"first element is: {list1[0]}")
else:
    print("list is empty")