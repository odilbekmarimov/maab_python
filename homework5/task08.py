filename = input ("filename: ")
file = open (filename, "r")
wordlist = []
for line in file:
    wordlist.extend(line.strip().split())
file.close()
longest_word = max(wordlist, key=len)
print(longest_word)