import csv

with open('./Data/trade_data.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    for row in reader:
        print(row['first_name'])

