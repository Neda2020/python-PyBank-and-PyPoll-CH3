import pandas as pd
import os
from pathlib import Path

# Path to collect data from the Resources folder
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = Path(current_directory, "Resources", "election_data.csv")   
analysis_textfile = os.path.join(current_directory, "analysis", "financial_analysis.txt")

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

# Write the results to a text file
with open(analysis_textfile, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidate_votes.index:
        file.write(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")