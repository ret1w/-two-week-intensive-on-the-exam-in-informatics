import csv
import time

count = {}

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    skip = True
    for row in reader:
        date = row[2]
        if skip:
            skip = False
            continue
        if time.strptime(date, '%m/%d/%Y %I:%M:%S %p').tm_year == 2015:
            primaryType = row[5]
            if primaryType in count:
                count[primaryType] += 1
            else:
                count[primaryType] = 0
print(count)