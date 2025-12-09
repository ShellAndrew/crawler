import csv

with open("./test/test_queue.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)