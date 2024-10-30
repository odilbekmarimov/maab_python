*list1,=map(int,input("enter the list (separator 'space'): ").split())
a = int (input ("enter the number to replace: "))
b = int (input ("enter the value to replace with: "))

list1[list1.index(a)]=b

print(list1)