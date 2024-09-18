import pandas as pd
import os

# Path to collect data from the Resources folder
file_path = r'D:\AssignmentsUOFT\python-PyBank-and-PyPoll-CH3\PyPoll\Resources\election_data.csv'

# Load the election_data.csv file using the correct file path
election_data = pd.read_csv(file_path)

# Calculate the total number of votes
total_votes = election_data['Ballot ID'].nunique()

# Calculate the total number of votes for each candidate
candidate_votes = election_data['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
candidate_percentage = (candidate_votes / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes.index:
    print(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
