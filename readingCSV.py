import csv 

with open("emailautomation\emailstosend.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        