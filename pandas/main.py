with open("pandas\sample_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


import csv

with open("pandas\sample_data.csv") as data_file:
    data = csv.reader(data_file)
    names = []
    for row in data:
        if row[0] != "Name":
            names.append(row[0])
    
    print(names)