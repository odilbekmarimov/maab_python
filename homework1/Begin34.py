x = float(input("Enter the weight of confetti: "))
a = float(input("Enter the cost of confetti: "))
y = float(input("Enter the weight of chocolate: "))
b = float(input("Enter the cost of chocolate: "))

perkgCHOC = b / y
perkgCON = a / x

print ("difference in price per kg is: ", perkgCHOC-perkgCON)