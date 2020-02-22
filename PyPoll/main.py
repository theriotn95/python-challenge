#Starting the import of the election_data.csv file

import csv
import os

# setting the path for the election_data.csv file 

csv_PyPoll = os.path.join("Downloads","election_data.csv")

# Set up lists to store your data 

Candidate_names = []
Candidates = []
count = 0
candidate_vote = []
percent_won = []

# Now we open the csv file with the path we set csv_PyPoll

with open(csv_PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimter=",")
    csv_header = next(csvreader)

