import os
import csv

csvfile = "PyBank/Resources/budget_data.csv"
textfile = "PyBank/analysis/budget_analysis.txt"

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

        if row[0] == months[0]:
            previous_values = (int(row[1]))
        else:
            diff_values.append(int(row[1]) - previous_values)
        
        previous_values = (int(row[1]))

        # print(diff_values)
    # Calculating average, minimum profit and maximum profit
    average = sum(diff_values) / (len(months) - 1)
    round_average = round(average, 2)
    min_diff = min(diff_values)
    max_diff = max(diff_values)

    # find month of greatest decrease
    min_index = diff_values.index(min_diff)
    min_month = months[(min_index + 1)]

    # find month of greatest increase
    max_index = diff_values.index(max_diff)
    max_month = months[(max_index + 1)]


# open file in w (write) mode
with open(textfile, "w") as text_file:
    text_file.write("Financial Analysis\n"
                    "----------------------------\n"
                    f"Total Months: {counter}\n"
                    f"Total: {current_values}\n"
                    f"Average Change: ${round_average}\n"
                    f"Greatest Increase in Profits: {max_month} (${max_diff})\n"
                    f"Greatest Decrease in Profits: {min_month} (${min_diff})\n")