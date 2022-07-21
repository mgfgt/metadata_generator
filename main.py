import json
import os

BASE_URL = input("Enter the base url of the images hosted on IPFS: ")
COLLECTION_NAME = input("Enter the name of the collection: ")
COLLECTION_DESCRIPTION = input("Enter the description of the collection: ")

def get_number_from_filename (filename): 
    number = int(filename.split(".")[0])
    return number

path = "./input"

directory = os.listdir(path)

sorted_files = sorted(directory, key=get_number_from_filename)

for filename in sorted_files:
    number = get_number_from_filename(filename)
    data = {
        "name": "%s #%d" % (COLLECTION_NAME, number),
        "description": COLLECTION_DESCRIPTION,
        "image": "%s/%s" % (BASE_URL, filename),
    }
    with open("./output/%d.json" % number, 'w') as outfile:
        json.dump(data, outfile)
   