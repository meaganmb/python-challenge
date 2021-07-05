import os
import csv

csvfile = "PyPoll/Resources/election_data.csv"
textfile = "PyPoll/analysis/election_analysis.txt"
#textfile = os.path.join("analysis", "election_analysis.txt")

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
highest_vote = max(all_candidates.values())

# highest_vote_key = getKeysByValue(all_candidates, highest_vote)

# print(highest_vote)
# print(all_candidates.values())
# open file in w (write) mode
with open(textfile, "w") as text_file:
    text_file.write("Election Results\n"
                    "--------------------\n"
                    f"Total Votes: {counter}\n"
                    "--------------------\n")
    
    for i in all_candidates.keys():
        percent = (all_candidates[i]/counter)*100
        round_percent= round(percent, 4)
        text_file.write(f"{i}: {round_percent}% ({all_candidates[i]})\n")
        # all = print(f"{all_candidates[i]} {round_percent}%")
        # (all_candidates[i]/counter)*100

    # text_file.write(f"{i}: {all_candidates[i]} {round_percent}%\n") undo if doesn't work
    #text_file.write(f"{i}: {all_candidates[i]}")
    # text_file.write(f"{i}: {all_candidates[i]}")
#print([i],all_candidates[i]) (dictionary value for each candidate)
    text_file.write("--------------------\n"

        # def winner(max_vote): 
        #     for winner in all_candidates.items(): 
        #         if max_vote == max_vote: 
        #             return text_file.write(f"Winner: {Winner}\n")
    listOfKeys = [key  for (key, value) in all_candidates.items() if value == highest_vote]
    
    #Iterate over the list of keys
    for key  in listOfKeys:
        text_file.write(f"Winner: {key}\n")  
                    # "Winner:\n"
                    "--------------------\n")