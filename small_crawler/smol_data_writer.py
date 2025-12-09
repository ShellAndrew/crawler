import csv

with open("./small_crawler/data.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['webpage'] + [''] * 8000)

