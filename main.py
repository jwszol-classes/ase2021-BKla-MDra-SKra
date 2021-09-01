import csv

# csv file name
filename = "..//yellow_tripdata_2020-05.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names:' + ', '.join(field for field in fields))

max_distance = 0

for row in rows:
    if float(row[4]) > max_distance:
        max_distance = float(row[4])
        print(row[4], "\n")
