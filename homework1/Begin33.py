x = float(input("Enter the weight (kg) (x): "))
a = float(input("Enter the cost (a): "))
y = float(input("Enter the additional weight in kg (y): "))

perkg = a / x

total_cost = perkg * y

print("cost of one kg is:", perkg)
print(f"the cost of {y} kg is: {total_cost:.2f}")