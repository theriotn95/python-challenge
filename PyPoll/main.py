#Starting the import of the election_data.csv file

import csv
import os

# setting the path for the election_data.csv file 

csv_PyPoll = os.path.join("Desktop","Downloads","election_data.csv")

# Set up lists to store your data 

candidate_names = []
candidates = []
votes = 0
candidate_votes = []
percent_won = []

# Now we open the csv file with the path we set csv_PyPoll

with open(csv_PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# make sure to skip header
    next(csvreader, None)

# Start the for loop to iterate through our lists

    for row in csvreader:
        # get the total number of votes
        votes = votes + 1
        # set candidate names to candidates
        candidates.append(row[2])
    #Now to get indivdual candidate names create a set from our Candidates List
    for a in set(candidates):
        candidate_names.append(a)
        # get the total number of votes per candidate with b
        b = candidates.count(a)
        candidate_votes.append(b)
        # get the percent of the total votes for each candidate received 
        c = (b/votes)*100
        percent_won.append(c)

#Prepare to print to terminal and determine the winner

winner_vote_count = max(candidate_votes)
winner = candidate_names[candidate_votes.index(winner_vote_count)]


print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
for v in range(len(candidate_names)):
            print(candidate_names[v] + ": " + str(percent_won[v]) + "% (" + str(candidate_votes[v])+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#Got the results now time to write them to a txt file 

with open ('PyPoll_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(votes) + "\n")
    text.write("-------------------------\n")
    for v in range(len(set(candidate_names))):
        text.write(candidate_names[v] + ": " + str(percent_won[v]) + "% (" + str(candidate_votes[v])+ ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("-------------------------\n")   




