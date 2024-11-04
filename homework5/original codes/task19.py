file = open("demo.txt", "r")
text = file.read()

text = text.replace(',', ' ')
print ("lenth is: ", len(text.split()))