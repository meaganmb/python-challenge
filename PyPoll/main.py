import os
import csv

csvfile = "PyPoll/Resources/election_data.csv"
textfile = "PyPoll/analysis/election_analysis.txt"

counter = 0
all_candidates = {}

# Open and read csv
with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        counter += 1 
        specific_candidate = str(row[2])
        # check if candidate is in dictionary
        if specific_candidate in all_candidates.keys():
        # if so, add 1
            all_candidates[specific_candidate] += 1
        else:
        # if not or else, add candidate to dictionary and set their total votes to 1 
            all_candidates[specific_candidate] = 1
print(all_candidates)

# finding the highest vote count in the poll
highest_vote = max(all_candidates.values())

# open file in w (write) mode
with open(textfile, "w") as text_file:
    text_file.write("Election Results\n"
                    "--------------------\n"
                    f"Total Votes: {counter}\n"
                    "--------------------\n")
# creating a for loop to show results of all candidates  
    for i in all_candidates.keys():
        percent = (all_candidates[i]/counter)*100
        round_percent= round(percent, 4)
        text_file.write(f"{i}: {round_percent}% ({all_candidates[i]})\n")
        text_file.write("--------------------\n"

        # attempting to find winner, i.e key of the highest value in all_candidates dictionary... not going so well
        text_file.write(f"Winner:{all_candidates.keys(highest_vote)}\n"
                        "--------------------")
    
    # listOfKeys = [key  for (key, value) in all_candidates.items() if value == highest_vote]
    
    # #Iterate over the list of keys
    # for key  in listOfKeys:
          
                    