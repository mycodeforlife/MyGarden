import csv

file_data = open("data.csv", 'r')

print(list(csv.DictReader(file_data)))

'''
for data in csv.DictReader(file_data):
    print(data)
'''
