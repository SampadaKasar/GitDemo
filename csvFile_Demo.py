#Q3: Difference between csv.reader and csv.DictReader
#csv.reader - Returns rows as lists:

['1', 'Alice', '24']

#Example:

import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#csv.DictReader - Returns rows as dictionaries using headers:

{'id': '1', 'name': 'Alice', 'age': '24'}

#Example:

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

#How to skip header? - next(header)