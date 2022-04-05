# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.
# with open(csvwriter

# Modules

import os
import csv


# initialize list to store data
ballots =[]

candidates= []

#initialize variable
candidate = 0

#initialize dictonary
votes = {}

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# open csv 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    # * The total number of months included in the dataset
    for row in csvreader:

        # * The total number of votes cast
        ballot = row[0]
        ballots.append(ballot)

        # * A complete list of candidates who received votes
       
        candidate = str(row[2])
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 1        

         #  * The total number of votes each candidate won
        else: 
            votes[candidate] += 1

    
with open ("Analysis/answer_analysis.txt", "w") as file:

    print("Election Results")
    file.write("Election Results\n")

    print( "-----------------------------------")
    file.write("-----------------------------------\n")

    total_votes = len(ballots)
    print(f"Total Votes: {total_votes}")
    file.write(f"Total Votes: {total_votes}\n")

    print( "-----------------------------------")
    file.write("-----------------------------------\n")

    for key,value in votes.items():
        answer= (f'{key}: {round((value/len(ballots)*100),3)} % {value}')
        print(answer) 
        file.write(f'{answer}\n')

    print( "-----------------------------------")
    file.write("-----------------------------------\n")

    winner = max(votes, key=votes.get)
    print(f"Winner: {winner}")
    file.write(f'Winner: {winner}\n')
    print( "-----------------------------------")
    file.write("-----------------------------------\n")
  

