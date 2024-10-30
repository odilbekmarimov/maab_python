*list1,=map(int,input("enter the list (separator 'space'): ").split())
num = int (input ("enter test number: "))

for i in range (len(list1)): 
    if list1[i] == num:
        print(f"index: {i}\t")
print("\nend of all accurances \n")
        