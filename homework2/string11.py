a = input ("input the text: ")
test = input ("input the test character: ")

print(f"position of first occurance of '{test}' is:", a.index(test))
#or
print(f"position of first occurance of '{test}' is:", a.find(test))
