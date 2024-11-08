import requests
import csv

directories = ["posts", "comments", "albums", "photos", "todos", "users"]
mainurl = 'https://jsonplaceholder.typicode.com/'
url = []

for singledir in directories:
    url.append(mainurl + singledir)

def flatten_dict(dict1:dict, parent_key='', sep='_') -> dict: #parent key is false 
    items = []
    for key1, value1 in dict1.items():
        new_key = f"{parent_key}{sep}{key1}" if parent_key else key1
        if isinstance(value1, dict):
            items.extend(flatten_dict(value1, new_key, sep=sep).items()) #parent key = new key
        else:
            items.append((new_key, value1))    
    return dict(items)

for fnames, singleurl in zip(directories, url):
    json_data = requests.get(singleurl).json() 
    with open(f"{fnames}.csv", 'w', newline='', encoding='utf-8') as file:
        flattened_data = [flatten_dict(item) for item in json_data]
        if flattened_data:
            fieldnames = flattened_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(flattened_data)

print("All files saved")
