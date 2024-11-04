filename = input ("filename: ")
file = open (filename, "r")
wordlist = []
for line in file:
    wordlist.extend(line.strip().split())
file.close()
print(len(wordlist))