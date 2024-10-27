a = int (input("enter a number: "))

#v1
print("is number divisible by 3 and 5:", a%3 == 0 and a%5 == 0 )

#v2
print("is number divisible by 3 and 5:", a%15 == 0 ) # 15 is least common multiple
