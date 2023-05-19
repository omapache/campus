""" import csv

with open('cotizaciones.csv', newline='') as File:  

    reader = csv.reader(File)

    for row in reader:

        print(row)
 """
import csv
with open('pepito.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            print(row['first_name'], row['last_name'])
