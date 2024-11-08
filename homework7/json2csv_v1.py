import requests
import csv

directories = ["posts", "comments", "albums", "photos", "todos", "users"]
mainurl = 'https://jsonplaceholder.typicode.com/'
url = []

for singledir in directories:
    url.append(mainurl+singledir)

for fnames, singleurl in zip(directories, url):

    json_data = requests.get(singleurl).json()    #status code success deb assume qilindi
    with open(f"{fnames}.csv", 'w', newline='', encoding='utf-8') as file:
        fieldnames = json_data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        
        for singlepost in json_data:
            if 'body' in singlepost:
                singlepost['body'] = singlepost['body'].replace("\n", " ") #body multi line text ekan '\n' almashtirildi
            writer.writerow(singlepost)

print("all files saved")
