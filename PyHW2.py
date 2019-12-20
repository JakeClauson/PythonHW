import os
import csv
dictionary = {}
votes = 0
#create variables for counting canidates

# create a path to the file
csvpath = os.path.join('../Resources', 'election_data.csv')
# Open the CSV
with open(csvpath, newline='', encoding="utf8") as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    # skip header
    csvheader = next(csvreader)

    for row in csvreader:
        votes += 1

        if row[2] not in dictionary:
            dictionary[row[2]] = 0

        dictionary[row[2]] = dictionary[row[2]] + 1

winner = max(dictionary.keys(), key=(lambda k: dictionary[k]))


# display total
print("Election Results")
print("--------------------")
print(f'Total Votes: {votes}')
print("--------------------")
for key,value in dictionary.items():
    print(f'{key} {value} {(value/votes)*100:.2f}%')
print("--------------------")
print(f'Winner: {winner}')

# Specify the file to write to
output_path = os.path.join("PyPoll.txt")
with open(output_path, "w", newline="") as f:
        
    f.write("Election Results\n")
    f.write("--------------------\n")
    f.write(f'Total Votes: {votes}''\n')
    f.write("--------------------\n")
    for key,value in dictionary.items():
        f.write(f'{key} {value} {(value/votes)*100:.2f}%''\n')
    f.write("--------------------\n")
    f.write(f'Winner: {winner}''\n')