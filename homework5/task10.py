from collections import Counter
def wcount(filename):
    file = open(filename, "r")
    return Counter(file.read().split())

filename = input ("enter filename: ")
print(wcount (filename))
