import csv

star_1 = []
star_2 = []

with open('stars.csv',"r") as r:
    reader = csv.reader(r)
    for col in reader:
        star_1.append(col)

with open('dwarf_stars.csv',"r") as r:
    reader = csv.reader(r)
    for col in reader:
        star_2.append(col)

header1 = star_1[0]
star_data_1 = star_1[1:]

header2 = star_2[0]
star_data_2 = star_2[1:]

header = header1 + header2
standard_star_data = []

for index,datarow in enumerate(standard_star_data):
    standard_star_data.append(star_data_1[index] + star_data_2[index])

with open('StarBook.csv','a+') as create:
    creater = csv.writer(create)
    creater.writerow(header)
    creater.writerows(standard_star_data)