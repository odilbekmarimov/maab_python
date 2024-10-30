list1 = list(map(int, input("Enter the list (separator 'space'): ").split()))
e2find = int(input("element to find: "))


index = -1

for i in range(len(list1)):
    if list1[i] == e2find:
        index = i
        break  

if index == -1:
    print("not in the list.")
else:
    print(f"{e2find} is at {index}")
    
#v2

print(list1.index(e2find))

    