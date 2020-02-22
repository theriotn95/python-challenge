#Starting the import of the election_data.csv file

import csv
import os

# setting the output path for the election_data.csv file 

csv_PyPoll = os.path.join("Downloads","election_data.csv")

# Set up lists to store your data 

Candidate_names = []
Candidates = []
votes = 0
Candidate_votes = []
percent_won = []

# Now we open the csv file with the path we set csv_PyPoll

with open(csv_PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimter=",")
# make sure to skip header
    next(csvreader, None)

# Start the for loop to iterate through our lists

for row in csvreader:
    # get the total number of votes
    votes = votes + 1
    # set candidate names to candidates
    Candidates.append(row[2])
#Now to get indivdual candiate names create a set from our Candidates List
for a in set(Candidates):
    Candidate_names.append(a)
    # get the total number of votes per candidate with b
    b = Candidates.count(a)
    Candidate_votes.append(b)
    # get the percent of the total votes for each candidate received 
    c = (b/votes)*100
    percent_won.append(c)









