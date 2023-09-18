with open("/home/yakub/langHandson/pcc/myfile.txt", 'r') as f:
    line1 = f.readline()
    print(line1)

with open("pcc/file.png", "rb") as pix:
    pix = pix.read()
    print(pix[:25])

cred = '''export stage =  PROD
export TABLE_ID=token-storage-1234
'''

with open("./.envrc", "a") as data:
    data.write(cred)

import pathlib
file_path = pathlib.Path("pcc/myoutputfile.txt")
# print (file_path.read_text())

# To work with the json file
'''#1: use the conventional readlines()
with open("pcc/iam_policy.json", "r") as policy:
    iam = policy.readlines()
# print(iam)

#2: use json module
import json
with open("pcc/iam_policy.json", "r") as policy:
    iam = json.load(policy)
# print (iam)

from pprint import pprint
# pprint.pprint(iam)

iam["Statement"]["Resource"]  = "S3"
iam["Statement"]["Effect"] = "Denied"

# iam["Statement"] = {"Resource": "S3", "Effect": "Denied"}

pprint(iam)

# write a Python dictionary as a JSON file by using the json.dump
with open("pcc/iam_policy.json", "w") as policy:
    new_policy = json.dump(iam, policy)
'''
# working with yaml
import yaml; from pprint import pprint

with open("pcc/playbook.yml", "r") as play:
    new_file = yaml.safe_load(play)
pprint(new_file)

with open("pcc/playbook.yml", "w") as opened_file:
    yaml.safe_dump(new_file, opened_file)

# Working with csv file

import csv
doc_path = "/home/yakub/langHandson/pcc/py_devops/file.csv"
with open(doc_path, newline='') as csv_file:
    new_doc = csv.reader (csv_file, delimiter=',')
    for i in range(10):
        print(next(new_doc))

# Working with panda
"""
Pandas is a powerful data manipulation and analysis library in Python. 
It provides a wide range of functions and methods for working with structured data, 
primarily in the form of dataframes. 
"""
import pandas as pd
