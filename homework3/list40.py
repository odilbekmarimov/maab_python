*list1,=map(int,input("enter the list (separator 'space'): ").split())
list2 = []

for element in list1: ## instructions not clear, transfers dublicates as unique values
    if element not in list2:
        list2.append(element)

print(list2)

