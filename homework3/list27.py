*list1,=map(int,input("enter the list (separator 'space'): ").split())
start = int (input ("enter start index of sublist: "))
end = int (input ("enter end index of sublist: "))
max = max (list1 [start:end+1])
print(max)