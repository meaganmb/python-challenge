import os
import csv

csvfile = "PyBank/Resources/budget_data.csv"
# textfile = "python-challenge/PyBank/analysis/budget_analysis.txt"

counter = 0
previous_values = 0
current_values = 0
diff_values = []
months = []

# Open and read csv
with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        counter += 1
        current_values = current_values + int(row[1])
        months.append(row[0])
# print(counter)
# print(current_values)

            if row[0] == "Jan-2010":
                previous_values = (int(row[1]))

            else:
                diff_values.append(int(row[1]) - previous_values)
        # previous_values = (int(row[1]))
            print(diff_values)
        # def bank_test():
        # total_difference_list = []