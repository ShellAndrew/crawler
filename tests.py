from collections import defaultdict, deque
import matplotlib.pyplot as plt
import csv


with open("data.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    col_info = ['title']
    padded_row = col_info + [''] * 30000
    row = ['hello'] + [''] * (30000)
    writer.writerow(padded_row)
    writer.writerow(row)

